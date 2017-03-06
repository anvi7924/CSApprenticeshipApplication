# -------------- StudentForm
yes = 'Yes'
no = 'No'
dnr = 'I do not wish to provide this information'
dnk = 'Do not know'
IDK = ((yes, 'Yes'), (no, 'No'), (dnk, 'Do not know'))
YESNO = ((yes, 'Yes'), (no, 'No'))
Project1 = 1
Project2 = 2
Project3 = 3
male = 'Male'
female = 'Female'
M_F = ((male , 'Male'), (female, 'Female'), (dnr, 'I do not wish to provide this information'))
race = ['ai', 'bl', 'nh', 'asi', 'wh', 'ot']
RACE_CHOICES = ((race[0], 'American Indian or Alaskan'), (race[1], 'Black or African American'), (race[2], 'Native Hawaiian or other Pacific Islander'),
(race[3], 'Asian'), (race[4], 'White'), (race[5], 'Other'), (dnr, 'I do not wish to provide this information'))
major = ['asp', 'am', 'ae', 'ce', 'cbe', 'cve', 'cs', 'ee', 'ece', 'ep', 'enve', 'epl', 'me', 'tam']
MAJORS = ((major[0], 'Aerospace Engineering'), (major[1], 'Applied Mathematics'), (major[2], 'Architectural Engineering'),
(major[3], 'Chemical Engineering'), (major[4], 'Chemical and Biological Engineering'), (major[5], 'Civil Engineering'),
(major[6], 'Computer Science'), (major[7], 'Electrical Engineering'), (major[8], 'Electrical and Computer Engineering'),
(major[9], 'Engineering Physics'), (major[10], 'Environmental Engineering'), (major[11], 'Engineering Plus'),
(major[12], 'Mechanical Engineering'), (major[13], 'Technology, Arts, and Media'))
levels = ['fr', 'so', 'jr', 'sr', 'ssr']
GRADE_LEVEL = ((levels[0], 'Freshman'), (levels[1], 'Sophomore'), (levels[2], 'Junior'),
    (levels[3], 'Senior'), (levels[4], 'Fifth Year Senior'))
month = ['j', 'f', 'm', 'ap', 'my', 'ju', 'jy', 'ag', 's', 'o', 'n', 'd']
MONTHS = ((month[0], 'January'), (month[1], 'February'), (month[2], 'March'),
        (month[3], 'April'), (month[4], 'May'), (month[5], 'June'), (month[6], 'July'),
        (month[7], 'August'), (month[8], 'September'), (month[9], 'October'),
        (month[10], 'November'), (month[11], 'December'))
year = [17, 18, 19, 20, 21, 22, 23]
YEARS = ((year[0], '2017'), (year[1], '2018'), (year[2], '2018'),
    (year[3], '2020'), (year[4], '2021'), (year[5], '2022'), (year[6], '2023'))




# -------------- Faculty

department = ['ASP', 'AM', 'AE', 'CE', 'CBE', 'CVE', 'CS', 'EE', 'ECE', 'EP', 'ENVE', 'EPL', 'ME']
DEPARTMENT_CHOICES = ((department[0], 'Aerospace Engineering'), (department[1], 'Applied Mathematics'), (department[2], 'Architectural Engineering'),
(department[3], 'Chemical Engineering'), (department[4], 'Chemical and Biological Engineering'), (department[5], 'Civil Engineering'),
(department[6], 'Computer Science'), (department[7], 'Electrical Engineering'), (department[8], 'Electrical and Computer Engineering'),
(department[9], 'Engineering Physics'), (department[10], 'Environmental Engineering'), (department[11], 'Engineering Plus'),
(department[12], 'Mechanical Engineering'))

SUPERV_CHOICES=(
    ('low','Very little supervision; student will need to work largely independently'),
    ('moderate','Moderate amount of supervision and interaction with others'),
    ('good','Good deal of supervision; student will work as an integral part of a research team')
)

SUPERV_PROV_CHOICES=(
    ('1','Supervision primarily by faculty supervisor'),
    ('2','Supervision primarily by graduate students'),
    ('3','Supervision primarily a combination of faculty and graduate students')
)

NATURE_W_CHOICES=(
    ('4','Nature of work is primarily theoretical, most work on paper/electronic medium'),
    ('5','Nature of work is primarily experimental, requiring hands-on work in a lab'),
    ('6','Nature of work is primarily field based, requiring hands-on work in the field'),
    ('7','Nature of work is primarily computer-related, involving coding/analysis'),
    ('8','Nature of work is a combination of several types of work.')
)

AMOUNT_EXP_CHOICES=(
    ('9','No prior work; student will be starting from basic idea'),
    ('10','Some prior work; student will build on work of others'),
    ('11','Well-established body of work; student will refine/improved upon efforts of others')
)
