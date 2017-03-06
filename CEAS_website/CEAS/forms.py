from django import forms
from CEAS.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import CheckboxSelectMultiple

def get_my_choices():

    projects = ()
    for i in range(len(Project.objects.all())):
        project_id = Project.objects.all()[i].id

        projects += (('{0}'.format(project_id),Project.objects.all()[i].title),)
    print(projects)
    return projects


class StudentForm(forms.ModelForm):


    firstChoice = forms.CharField(label = 'First Choice',widget=forms.Select(choices=get_my_choices()))
    secondChoice = forms.CharField(required=False,label = 'Second Choice',widget=forms.Select(choices=get_my_choices()))
    thirdChoice = forms.CharField(required=False,label = 'Third Choice',widget=forms.Select(choices=get_my_choices()))
    fourthChoice = forms.CharField(required=False,label = 'Fourth Choice',widget=forms.Select(choices=get_my_choices()))
    fifthChoice = forms.CharField(required=False,label = 'Fifth Choice',widget=forms.Select(choices=get_my_choices()))

    '''
    graduate_student = forms.ChoiceField(label = 'Are you a graduate student?', required=True,
    widget=forms.RadioSelect(), choices=YESNO)
    BSMS_student = forms.ChoiceField(label = 'Are you a BS/MS student?', required=True,
    widget=forms.RadioSelect(), choices=YESNO)
    enrolled_in_College_of_Engineering = forms.ChoiceField(label = 'Are you enrolled in the College of Engineering?', required=True,
    widget=forms.RadioSelect(), choices=YESNO)
    can_You_Serve_the_Entire_Year = forms.ChoiceField(label = 'Are you able to serve the entire year?', required=True,
    widget=forms.RadioSelect(), choices=YESNO)
    '''

    race = forms.ChoiceField(required=False, widget=forms.RadioSelect(), choices=RACE_CHOICES)
    address = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows':'3', 'cols': '20'}))
    previously_Applied = forms.ChoiceField(label= 'Have you applied to this program before?', required=True,
    widget=forms.RadioSelect(), choices=YESNO)
    prevres = forms.ChoiceField(label = 'Do you have previous research experience?', required=False,
    widget=forms.RadioSelect(), choices=YESNO)
    backcheck = forms.ChoiceField(label = 'Have you had a background check at CU?', required=False,
     widget=forms.RadioSelect(), choices=IDK)
    dhtraining = forms.ChoiceField(label = 'Have you had Discrimination and Harassment Awareness training at CU?', required=True,
     widget=forms.RadioSelect(), choices=IDK)
    social = forms.CharField(label= 'Last four digits of your social security number', max_length=4)
    #goldshirt = forms.ChoiceField(label = 'Are you a member of the Goldshirt program?', required=True,
    #widget=forms.RadioSelect(), choices=YESNO)
    feplans = forms.CharField(label = 'If have current fall employment plans please describe them here', max_length=500,
     widget = forms.Textarea(attrs={'rows':'3', 'cols': '20'}))


    class Meta:
        model = Student
        fields = "__all__"

    class Media:
        css = {
            'all': ('CEAS_website.css')
        }


class AdminForm():
    class Meta:
         model= User
         fields = 'status'

class FacultyForm(forms.ModelForm):

    supervision = forms.ChoiceField(choices=SUPERV_CHOICES, widget=forms.RadioSelect())
    supervision_provided = forms.ChoiceField(choices=SUPERV_PROV_CHOICES, widget=forms.RadioSelect())
    nature_work = forms.ChoiceField(choices=NATURE_W_CHOICES, widget=forms.RadioSelect())
    previous_work = forms.ChoiceField(choices=AMOUNT_EXP_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Project
        fields = '__all__'



class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        fields = ('title', 'url', 'views')
