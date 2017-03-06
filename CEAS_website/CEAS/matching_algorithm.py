import operator
from CEAS.models import *

map_score = {'Female':10,'ssr':100,'sr':100,'jr':50,'so':20,'ai':10,\
 'bl':10, 'nh':10, 'asi':10}

def calculate_score(student_dic, pref_student,*args):
    score = 0
    if len(args) != 0:
        return 10000
    if pref_student == student_dic['full_Name']:
        return 2000
    values = student_dic.values()
    for criteria in map_score.keys():
        if criteria in values:
            score += map_score[criteria]

    return score


def matching(*args):

    selected_students = 3

    try:
        # Reset table for new computation
        ResultAlgorithm.objects.all().delete()

        # Get all needed objects
        project_list = Project.objects.all()
        student_list = Student.objects.all()
        student_proj = StudentProject.objects.all()

        for p in project_list:
            # Key is student_id, value is score

            student_score_dic = {}
            student_for_proj = student_proj.filter(project_id = p.id)
            #print("For project: ",p.id," these are the students: ",)

            i = 0
            for s in student_for_proj:
                student_id = s.student_id
                #print(student_id)
                student_dic = student_list.filter(id = student_id).values()[0]
                if len(args) != 0:

                    if int(args[1]) == p.id and int(args[0]) == student_id:
                        score = calculate_score(student_dic,p.pref_student,args[0],args[1])
                    else:
                        score = calculate_score(student_dic,p.pref_student)
                else:
                    score = calculate_score(student_dic,p.pref_student)

                if i<selected_students and student_id not in student_score_dic:
                    student_score_dic[student_id] = score
                    i += 1

                else:
                    lowest_score_accepted = min(student_score_dic.values())
                    key_lowest = min(student_score_dic, key=student_score_dic.get)

                    #print(student_score_dic)
                    if score > lowest_score_accepted:
                        #print('Pop score: ',lowest_score_accepted, 'for ',key_lowest)
                        #print('Use score: ',score, 'for ',student_id)
                        student_score_dic[student_id] = student_score_dic.pop(key_lowest)
                        student_score_dic[student_id] = score


            ss_sorted = sorted(student_score_dic.items(), key=operator.itemgetter(1), reverse=True)
            #print(ss_sorted)
            for i in ss_sorted:
                # Store in database
                ResultAlgorithm(student_id= i[0],project_id=p.id,score=i[1]).save()

        return True

    except BaseException as e:
        print('Failed to upload to ftp: ',str(e))
        return False
