import os
import django

def populate():

    # Set up faculty
    faculty_status = add_status('Faculty')

    add_page(
        status=faculty,
        title="FacultyForm",
        url="http://docs.python.org/2/tutorial/")

    # Set up student
    student_status = add_status("Student")

    add_page(
        status=student,
        title="StudentForm",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/"
        )


    # Print out what we have added to the user.
    for s in Status.objects.all():
        for p in Page.objects.filter(status=s):
            print("- {0} - {1}".format(str(s), str(p)))

def add_page(status, title, url, views=0):
    p = Page.objects.get_or_create(status=status, title=title, url=url)[0]
    return p

def add_status(name):
    s = Status.objects.get_or_create(name=name)[0]
    return s

# Start execution
if __name__ == '__main__':

    print("Starting CEAS population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CEAS_website.settings')
    django.setup()

    from CEAS.models import Status, Page
    populate()
