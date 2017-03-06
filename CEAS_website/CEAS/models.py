from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from CEAS.var_choices import *


class Status(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # It would be better to use status as FK but the database
    # complains about have many to one relationship
    # when I stated it was a one to one with user
    status = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.status


class StudentProject(models.Model):
    student_id = models.IntegerField()
    project_id = models.IntegerField(null=True)
    priority = models.IntegerField()

'''
class StudentProject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.IntegerField()
'''

class ResultAlgorithm(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=128 ,null=True)
    project_id = models.IntegerField()
    score = models.IntegerField()


class Student(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?[\d|-]{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. "
        "Up to 15 digits allowed.")

    full_Name = models.CharField(max_length=128 ,null=True)
    gender = models.CharField(max_length=100, choices=M_F, blank=True,null=True)
    race = models.CharField(max_length=100, choices=RACE_CHOICES, default='I do not wish to provide this information',blank=True)
    '''
    graduate_student = models.CharField(max_length=1, choices=YESNO, default='No')
    BSMS_student = models.CharField(max_length=1, choices=YESNO, default='No')
    enrolled_in_College_of_Engineering = models.CharField(max_length=1, choices=YESNO, default='No')
    can_You_Serve_the_Entire_Year = models.CharField(max_length=1, choices=YESNO, default='No')

    full_Name = models.CharField(max_length=128, default='Name')
    gender = models.CharField(max_length=1, choices=M_F, default='Female')
    race = models.CharField(max_length=1, choices=RACE_CHOICES, default='I do not wish to provide this information')
    '''
    address = models.CharField(max_length=2000, blank=True)
    phone_Number = models.CharField(max_length=128, validators=[phone_regex], blank=True, null=True,
                                                    default='+1999-999-9999')
    email = models.EmailField(default='name@email.com')
    primary_Major = models.CharField(max_length=100, choices=MAJORS, default='Computer Science')
    secondary_Major = models.CharField(max_length=100, choices=MAJORS, blank=True)
    student_ID = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')], default='000000000')
    GPA = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(4.0)])
    grade_level_as_of_next_fall = models.CharField(max_length=50, choices=GRADE_LEVEL,blank=True)
    anticipated_Graduation_Date = models.CharField(max_length=100, default='May 2017',blank=True)
    prevres = models.CharField(max_length=100, choices=YESNO, default='No',blank=True)
    previously_Applied = models.CharField(max_length=10, choices=YESNO, default='No',blank=True)

    '''
    GPA = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='0.00')
    grade_level_as_of_next_fall = models.CharField(max_length=1, choices=GRADE_LEVEL, default='Freshman')
    anticipated_Graduation_Date = models.CharField(max_length=100, default='May 2017')
    prevres = models.CharField(max_length=100, choices=YESNO, default='No')
    previously_Applied = models.CharField(max_length=1, choices=YESNO, default='No')
    goldshirt = models.CharField(max_length=1, choices=YESNO, default='No')
    '''

    feplans = models.CharField(max_length=500, blank=True)
    firstChoice = models.CharField(max_length=50,default=None)
    secondChoice = models.CharField(max_length=50,blank=True,null=True,default=None)
    thirdChoice = models.CharField(max_length=50,blank=True,null=True,default=None)
    fourthChoice = models.CharField(max_length=50,blank=True,null=True,default=None)
    fifthChoice = models.CharField(max_length=50,blank=True,null=True,default=None)
    backcheck = models.CharField(max_length=50, choices=IDK, default='Yes',blank=True)
    dhtraining = models.CharField(max_length=50, choices=IDK, default='Yes',blank=True)
    social = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], default='0000')
    skill1 = models.CharField(max_length=75, blank=True)
    skill2 = models.CharField(max_length=75, blank=True)
    skill3 = models.CharField(max_length=75, blank=True)
    resume = models.FileField(default='./resume',blank=True)
    cover_Letter = models.FileField(default='./resume',blank=True)


class Project(models.Model):
    title = models.CharField(max_length=128, default='title', null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?[\d|-]{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")

    primary_faculty_member = models.CharField(max_length=128, null=True, default='faculty name')
    # validators should be a list
    primary_faculty_phone_number = models.CharField(max_length=128, validators=[phone_regex], blank=True, null=True,
                                                    default='+1999-999-9999')
    primary_faculty_email = models.EmailField(default='Name@email.com', null=True)
    primary_faculty_department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default=department[6],
        blank=True,
        null=True,
    )

    secondary_faculty_member = models.CharField(max_length=128, default='faculty name', blank=True, null=True)
    secondary_faculty_phone_number = models.CharField(max_length=128, validators=[phone_regex], blank=True,
                                                      default='+1999-999-9999', null=True)
    secondary_faculty_email = models.EmailField(max_length=128, default='Name@email.com', blank=True, null=True)
    secondary_faculty_department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default=department[6],
        blank=True,
        null=True,
    )

    grad_post_doc_info = models.CharField(max_length=128, default='', blank=True, null=True)
    grad_post_doc_phone = models.CharField(max_length=128, validators=[phone_regex], blank=True, null=True,
                                           default='+1999-999-9999')
    grad_post_doc_email = models.EmailField(default='Name@email.com', blank=True, null=True)

    from_what_areas_do_you_wish_to_recruit_student = MultiSelectField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default=department[6],
        null=True,
    )

    special_requirements = models.CharField(max_length=1000, blank=True,  default='', null=True)
    speed_type = models.IntegerField(default=000000, blank=True, null=True)
    EDC_focus = models.BooleanField(default=True)
    number_of_applicants = models.IntegerField(default=1,null=True)
    website = models.URLField(max_length=128,
                              default='http://www.colorado.edu/activelearningprogram/discovery-learning/discovery-learning-apprenticeship-program',
                              blank=True, null=True)

    short_description = models.TextField(max_length=80, blank=True, default='', null=True)
    description = models.TextField(max_length=1200, blank=True, default='', null=True)

    supervision = models.CharField(
        max_length=128,
        choices=SUPERV_CHOICES,
        default='low',
        blank=True,
        null=True,
        )

    supervision_provided = models.CharField(
            max_length=128,
            choices=SUPERV_PROV_CHOICES,
            default='1',
            blank=True,
            null=True,
            )

    nature_work = models.CharField(
            max_length=128,
            choices=NATURE_W_CHOICES,
            default='4',
            blank=True,
            null=True,
            )

    previous_work = models.CharField(
            max_length=128,
            choices=AMOUNT_EXP_CHOICES,
            default='9',
            blank=True,
            null=True,
            )

    pref_student = models.CharField(max_length=128,null=True,blank=True)

    others = models.TextField(max_length=500, blank=True,null=True)

class Page(models.Model):
    status = models.ForeignKey(Status)
    title = models.CharField(max_length=128)
    url = models.URLField()

    def __unicode__(self):
        return self.title
