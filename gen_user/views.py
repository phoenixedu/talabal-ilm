from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,DetailView,UpdateView
from django.contrib.auth.views import LoginView
from .models import GenUser
from django.contrib.auth.models import User 
from .form import GenUserForm,CustomAuthenticationForm,editUserInfoGenUser
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .emailconformation import send_confirmation_email
from django.contrib import messages
# error
from django.http import Http404
from django.core.exceptions import PermissionDenied,ValidationError,SuspiciousOperation
# Models from All Apps 
from edu.models import xEduInstitution,userEdu

@login_required
def index(request):
    template_name = 'index.html'
    if request.user.is_authenticated:
        in_edu = userEdu.objects.filter(user=request.user,current=True)
    contx = {
        'in_edu' : in_edu
    }
    return render(request,template_name,contx)
    
class registerGenUser(View):
    model = GenUser
    form_class = GenUserForm
    template_name = 'registration/register.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            gen_user = form.save(commit=False)  # Create GenUser instance without saving to the database yet
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password1'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
            )
            gen_user.user = user  # Assign the user to the GenUser instance
            gen_user.save()  # Save the GenUser instance to the database
            send_confirmation_email(user,request) 
            login(request, user)  # Log in the user
            return redirect('home')
        return render(request,self.template_name, {'form': form})

class UserRestrictedQuerysetMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user)
    
class GenUserProfile(LoginRequiredMixin,UserRestrictedQuerysetMixin,DetailView):
    model = GenUser
    template_name= 'gen/profile.html'
    context_object_name = 'genuser'

    def get(self, request,username):
        genuser = get_object_or_404(GenUser , username=username)
        try:
            edu = xEduInstitution.objects.get(OwnerOfX=request.user)
        except xEduInstitution.DoesNotExist:
            edu = None
        return render(request, self.template_name,{self.context_object_name:genuser,'edu':edu})
    
    def post(self,request,username):
        genuser = get_object_or_404(GenUser , username=username)
        pictureUp = request.FILES.get('picture')
        if pictureUp:
            genuser.picture = pictureUp
            genuser.save()
            return redirect(request.path)
        return render(request, self.template_name, {self.context_object_name: genuser})

class profileUpdateGenUser(LoginRequiredMixin,UserRestrictedQuerysetMixin,UpdateView):
    model = GenUser
    template_name = "gen/updateprofile.html"
    form_class = editUserInfoGenUser
    context_object_name = "genuser"    

    def get(self,request,username):
        user = get_object_or_404(GenUser,username=username)
        Cruentuser = request.user.genuser.pk_key
        if Cruentuser == user.pk_key:
            form = self.form_class(instance=user)
            contx ={
                'form':form,
                self.context_object_name:user,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('genProfile', username=Cruentuser)
    def post(self,request,username):
        user = get_object_or_404(GenUser,username=username)
        Cruentuser = request.user.genuser.pk_key
        if Cruentuser == user.pk_key:
            form = self.form_class(request.POST,request.FILES,instance=user)
            if form.is_valid:
                form.save()
                return redirect('genProfile',username=user.username)
        else:
            contx ={
                'form':form,
                self.context_object_name:user,
            }
            return render(request,self.template_name,contx)

class customUserLogin(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class profileSetting(LoginRequiredMixin,UserRestrictedQuerysetMixin,View):
    model = GenUser
    template_name = "gen/genSettings.html"
    context_object_name = 'genuser'
    
    def get(self,request,username):
        genuser = get_object_or_404(GenUser , username=username)
        contx = {
            self.context_object_name: genuser,
        }
        return render(request, self.template_name, contx)
    def post(self,request,username):
        genuser = get_object_or_404(GenUser , username=username)
        mailSend = request.POST.get('sendMl')
        if mailSend == 'mailsend':
            send_confirmation_email(genuser,request)
        else:
            pass
        return redirect(request.path)

class emailVerification(LoginRequiredMixin,UserRestrictedQuerysetMixin,View):
    model = GenUser
    template_name = 'registration/email_confirmed.html'
    def get(self, request,token):
        try:
            user = self.model.objects.get(email_verification_token=token)
            if not user.emailConformation:
                user.emailConformation = True
                user.save()
                return render(request, self.template_name)
            elif token != user.email_verification_token:
                messages.error(request, 'Token is expired')
                return redirect(request.path)
            elif token not in user.email_verification_token:
                messages.error('Token is expired')
                return redirect(request.path)
            else:
                return render(request, 'registration/invalid_token.html')
        except (TypeError, ValueError, OverflowError,ValidationError, User.DoesNotExist) as e:
            return render(request, 'registration/invalid_user.html')   
    
class ChangePasswordView(LoginRequiredMixin,UserRestrictedQuerysetMixin,View):
    template_name = 'registration/pwReset.html'
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if request.user != user:
            return redirect('home')
        return render(request, self.template_name, {'user': user})

    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        pwlen = len(confirm_password)
        try :
            if request.user == user:
                if password == confirm_password and pwlen >= 8:
                    user.set_password(password)
                    user.save()
                    return redirect('login')
                elif pwlen <= 7:
                    messages.error(request, 'Your password must containt atlest 8 words.')
                    return redirect(request.path)
                elif password != confirm_password:
                    messages.error(request, 'Passwords do not match.')
                    return redirect(request.path)
                else:
                    messages.error(request, 'There is something wrong pleas do it later.')
                    return redirect(request.path)
        except:
            pass

class ErrorHandlingView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            # Pass the error details to the error template
            context = self.get_error_context(request, e)
            return render(request, 'error.html', context, status=self.get_error_status(e))

    def get_error_context(self, request, exception):
        # Return a dictionary containing error details
        return {
            'error_name': type(exception).__name__,
            'error_message': str(exception),
        }

    def get_error_status(self, exception):
        # Determine the HTTP status code based on the exception type
        if isinstance(exception, Http404):
            return 404
        elif isinstance(exception, PermissionDenied):
            return 403
        elif isinstance(exception, SuspiciousOperation):
            return 400
        else:
            return 500
