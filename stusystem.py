import os

filename = 'students.txt'


def main():
    while True:
        menu()
        choice = int(input('Please select'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('Are you sure you want to exit? y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('Thank you for your visit!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('====================Student Information Management System====================')
    print('--------------------------------------Menu-----------------------------------')
    print('\t\t\t\t\t\t1.Enter student information')
    print('\t\t\t\t\t\t2.Search student information')
    print('\t\t\t\t\t\t3.Delete student information')
    print('\t\t\t\t\t\t4.Modification student information')
    print('\t\t\t\t\t\t5.Sort')
    print('\t\t\t\t\t\t6.Total number of students')
    print('\t\t\t\t\t\t7.Display all student information')
    print('\t\t\t\t\t\t0.Exit')
    print('-----------------------------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('Please input your id(example:1001):')
        if not id:
            break
        name = input('Please input your name:')
        if not name:
            break

        try:
            english = int(input('Please input your english score:'))
            python = int(input('Please input your python score:'))
            java = int(input('Please input your java score:'))
        except:
            print('Invalid input,not integer type,please re-enter:')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('Continue? y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    save(student_list)
    print('Student information input completed!')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('Search by id,please input 1; Search by name,please input 2:')
            if mode == '1':
                id = input('Please input id:')
            elif mode == '2':
                name = input('Please input name:')
            else:
                print('Wrong input,please re-enter!')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('Continue search? y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('There is no information!')
            return


def show_student(lst):
    if len(lst) == 0:
        print('There is no information!')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', 'Name', 'English Score', 'Python Score', 'Java Score', 'Total Score'))
    format_data = '{:^6}\t{:^12}\t{:^12}\t{:^12}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input('Please input the id of student:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'The id {student_id} has been deleted')
                    else:
                        print(f'This id {student_id} can not be found')
            else:
                print('There is no information!')
                break
            show()
            answer = input('Continue delete? y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('Please input the id of student:')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('You can modify the information now!')
                while True:
                    try:
                        d['name'] = input('Please input your name:')
                        d['english'] = input('Please input your english score:')
                        d['python'] = input('Please input your python score:')
                        d['java'] = input('Please input your java score:')
                    except:
                        print('Wrong input,please re-enter!')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('Successfully modified!')
            else:
                wfile.write(str(d) + '\n')
        answer = input('Continue modify? y/n\n')
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('Please select(0.Ascending 1.Descending):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('Wrong input,please re-enter!')
        sort()
    mode = input('Please select(1.Sort by english score '
                 '2.Sort by python score '
                 '3.Sort by java score '
                 '0.Sort by total score):')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('Wrong input,please re-enter!')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'There is {len(students)} students.')
            else:
                print('There is no information!')
    else:
        print('There is no information!')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('There is no information!')


if __name__ == '__main__':
    main()
