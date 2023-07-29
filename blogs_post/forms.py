from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost,DefaltBlogPost

class BlogPostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'meta_description','meta_keywords','content','featured_image','is_publish','is_public']

        # widgets = {
        #     'title' : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'content': CKEditorWidget(),
        #     'content':forms.Textarea(attrs={'class':'form-control','rows':3}),
        #     'meta_description' : forms.Textarea(attrs={'class':'form-control','rows':3}),
        #     'meta_keywords' : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'tags': forms.MultipleChoiceField(attrs={'class':'form-check-input'}),
        #     'featured_image': forms.FileInput(attrs={'class':'form-control-files ml-3 '}),
        #     'is_publish': forms.CheckboxInput(attrs={'class':'form-check-input ml-3 '}),
        #     'is_public': forms.CheckboxInput(attrs={'class':'form-check-input ml-3 '}),
        # }

class DefaltBlogPostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = DefaltBlogPost
        fields = ['title', 'content']

        # widgets = {
        #     'title' : forms.TextInput(attrs={'class':'form-control'}),
        #     'content': CKEditorWidget(),
        # }

class BlogPostEditForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'meta_description','meta_keywords','content','featured_image','is_publish','is_public']

