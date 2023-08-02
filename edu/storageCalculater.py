import sys
from django.db import models

def calculate_storage_usage(instance):
    total_storage_bytes = 0
    field_sizes_bytes = {}

    for field in instance._meta.get_fields():
        field_value = getattr(instance, field.name, None)
        if field_value is not None:
            field_size_bytes = sys.getsizeof(field_value)
            total_storage_bytes += field_size_bytes
            field_sizes_bytes[field.name] = field_size_bytes

    total_storage_bytes = round(total_storage_bytes, 5)
    field_sizes_bytes = {field_name: round(size_bytes, 5) for field_name, size_bytes in field_sizes_bytes.items()}

    return total_storage_bytes, field_sizes_bytes

'''
///// ----- EDU:--------/////
Total storage size: 1047 bytes
Field sizes:
edu_storage: 48 bytes
group_of_teachers: 48 bytes
group_of_admins: 48 bytes
group_of_students: 48 bytes
GroupOfHeadOfDeparment: 48 bytes
InchargeOfClassGroup: 48 bytes
HeadOfInstetude: 48 bytes
GroupOfSubHeadOfInstetude: 48 bytes
id: 28 bytes
OwnerOfX: 48 bytes
name: 61 bytes
typeOfInstitution: 48 bytes
uuid: 56 bytes
email: 74 bytes
country: 48 bytes
phone: 62 bytes
address: 64 bytes
picture: 48 bytes
registration_date: 32 bytes
pk_key: 66 bytes
active: 28 bytes
///// ----- depts:--------/////
Total storage size: 277 bytes
Field sizes:
id: 28 bytes
edu: 48 bytes
name: 57 bytes
location: 64 bytes
picture: 48 bytes
dateOfcreation: 32 bytes
Total storage size: 276 bytes
Field sizes:
id: 28 bytes
edu: 48 bytes
name: 56 bytes
location: 64 bytes
picture: 48 bytes
dateOfcreation: 32 bytes
///// ----- edu cls:--------/////
Total storage size: 497 bytes
Field sizes:
online_class_edu_class: 48 bytes
id: 28 bytes
edu: 48 bytes
course: 48 bytes
semister: 48 bytes
department: 48 bytes
name: 57 bytes
capacity: 28 bytes
location: 64 bytes
picture: 48 bytes
dateOfcreation: 32 bytes

///
Total storage size: 561 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 63 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 78 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 561 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 63 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 78 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 545 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 54 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 71 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 549 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 56 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 73 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 602 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 85 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 97 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 543 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 53 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 70 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 602 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 85 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 97 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 550 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 57 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 73 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes
.....................................................
Total storage size: 537 bytes
Field sizes:
lectures: 48 bytes
student_att: 48 bytes
InchargeOfEclass: 48 bytes
id: 28 bytes
Eclass: 48 bytes
name: 50 bytes
incharge: 48 bytes
createDateTime: 48 bytes
uuid: 56 bytes
cls_key: 67 bytes
studentsOfclass: 48 bytes


'''
