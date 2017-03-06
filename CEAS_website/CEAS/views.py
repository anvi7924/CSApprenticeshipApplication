from django.shortcuts import render,redirect,render_to_response
from django.template import RequestContext
from CEAS.forms import *
from CEAS.matching_algorithm import *
from CEAS.make_spreadsheet import *
from django.db.models import Q
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse

def home(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'CEAS/home.html')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

def about(request):
    return render(request, 'CEAS/about.html')

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)


        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:

                status = UserProfile.objects.filter(
                        user_id = user.id).values('status')[0].get('status')

                if status == 'faculty':
                    return redirect('add_project')

                elif status == 'staff':
                    return redirect('staffpage')

                else:
                    return redirect('studentform')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("You do not have permission")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        form = LoginForm()

        return render(request,'CEAS/login.html', {'form': form})

def projectlist(request):
    value = None
    value = request.GET.get('value')

    if value != None:
        project = Project.objects.filter(title = value)[0]
        return render(request, 'CEAS/project.html',{'project': project})


    project = Project.objects.all()
    return render(request, 'CEAS/projectlist.html',{'project': project})


def add_project(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = FacultyForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Run the matching algorithm at every submission
            matching()
            return redirect('projectlist')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
            return HttpResponse("Invalid form details supplied.")

    else:
        # If the request was not a POST, display the form to enter details.
        form = FacultyForm()

    return render(request, 'CEAS/add_project.html', {'form': form})


# Every time a student form is submitted we update studentproject tb
def student_proj_relation():
    last_added  = Student.objects.all().latest('id')
    s_id = last_added.id
    list_choices = list(set([last_added.firstChoice,last_added.secondChoice,\
                    last_added.thirdChoice,last_added.fourthChoice,\
                    last_added.fifthChoice]))
    for i in range(len(list_choices)):
        StudentProject(student_id=s_id,project_id=list_choices[i],priority=i).save()


    '''
    student = Student.objects.filter(full_Name = student_name)
    StudentProject(student=student,project_id=choice_1,priority=1).save()
    StudentProject(student=student,project_id=choice_2,priority=2).save()
    StudentProject(student=student,project_id=choice_3,priority=3).save()
    StudentProject(student=student,project_id=choice_4,priority=4).save()
    StudentProject(student=student,project_id=choice_5,priority=5).save()
    '''

def studentform(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            print("no !!!!!!!")
            # Save the new category to the database.
            form.save(commit=True)

            # Create relationship student and project
            student_proj_relation()

            # Run the matching algorithm at every submission
            matching()
            return redirect('.')

        else:
            print(form.errors)
            return HttpResponse("Invalid form details supplied.")

    else:
        form = StudentForm()
        value = request.GET.get('value')
        print("hey")
        if value != None:

            #project = Project.objects.filter(title = value)[0]
            return render(request, 'CEAS/studentform.html', {'form': form})


        #return render(request, 'CEAS/studentform.html', {'form': form,'project': project})

    return render(request, 'CEAS/studentform.html', {'form': form})


def staffpage(request):
    # Get the context from the request.
    context = RequestContext(request)
    # generate spreadsheet for download
    make_spreadsheet()

    if request.method == 'POST':
        #s_id = request.GET.get('s_id')
        #print('!!!! ID: ',s_id)
        s_id = request.POST.get('s_id1')
        if s_id != None:
            p_id = request.POST.get('proj_id')
            print('!!!! ID: ',s_id)
            print('!!!! ID: ',p_id)
            if matching(s_id,p_id):
                return redirect('.')
        else:
            if matching():
                return redirect('.')

            else:
                return HttpResponse("Something went wrong.")

    else:

        value = None
        value = request.GET.get('value')
        studproj = StudentProject.objects.all()
        if value != None:
            project = Project.objects.filter(title = value)[0]
            student = Student.objects.filter(Q(firstChoice = project.id)|Q(secondChoice=project.id)|\
                                   Q(thirdChoice = project.id)|Q(fourthChoice=project.id)|\
                                   Q(fifthChoice = project.id))
            return render(request, 'CEAS/projectmatrix.html',{'project': project,'student':student,'studproj':studproj})

        student = Student.objects.all()
        project = Project.objects.all()
        result_match = ResultAlgorithm.objects.all()
        return render(request, 'CEAS/staffpage.html', {'project': project,'student':student,'result_match':result_match})
