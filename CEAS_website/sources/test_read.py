import numpy as np
import xlrd


def get_student_info(filename='SampleDLAMatrix.xlsx'):
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_index(0)

    # Change this depending on how many header rows are present
    # Set to 0 if you want to include the header data.
    offset = -1

    rows = []
    for i, row in enumerate(range(worksheet.nrows)):
        if i <= offset:  # (Optionally) skip headers
            continue
        r = []
        for j, col in enumerate(range(worksheet.ncols)):
            r.append(worksheet.cell_value(i, j))
        rows.append(r)

    student_project = np.array(rows)

    student_info = np.concatenate((student_project[11:184:1, 0:13:1], student_project[11:184:1, 120:132:1]), axis=1)
    return student_info


def get_project_info(filename='SampleDLAMatrix.xlsx'):
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_index(0)

    # Change this depending on how many header rows are present
    # Set to 0 if you want to include the header data.
    offset = -1

    rows = []
    for i, row in enumerate(range(worksheet.nrows)):
        if i <= offset:  # (Optionally) skip headers
            continue
        r = []
        for j, col in enumerate(range(worksheet.ncols)):
            r.append(worksheet.cell_value(i, j))
        rows.append(r)

    student_project = np.array(rows)

    project_info = student_project[0:11:1, 14:118:1]
    return project_info


if __name__ == '__main__':
    student_info = get_student_info()
    project_info = get_project_info()
    print(student_info[0, :])

    print(project_info[:, 0])
