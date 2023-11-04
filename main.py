import uuid
from datetime import datetime


def create_note():
    with open('notes.csv', 'a') as notes:
        notes.write(str(uuid.uuid4())[0:3] + ';')
        notes.write(input('Введите заголовок заметки: ') + ';')
        notes.write(input('Введите тело заметки: ') + ';')
        notes.write(str(datetime.today().strftime("%d.%m.%Y")) + '\n')
        print("Операция прошла успешна\n")


def read_notes():
    with open('notes.csv', 'r') as notes:
        for line in notes:
            print(line)
        notes.close()


def read_note(note_id):
    res = check_id(note_id)
    if res[0]:
        print("Заметки с таким id не найдено\n")
    else:
        print(res[1])


def read_note_by_date(date):
    with open('notes.csv', 'r') as notes:
        flag = True
        for line in notes:
            list_note = line.split(';')
            if date == list_note[3].strip():
                flag = False
                print(line)
        if flag:
            print("Заметок с такой датой не найдено\n")


def edit_note(note_id):
    with open('notes.csv') as notes:
        list_edit = []
        res = check_id(note_id)
        if res[0]:
            print("Заметки с таким id не найдено\n")
        else:
            for line in notes:
                if line == res[1]:
                    print('Изменение заметки: ')
                    create_note()
                    print("Заметка успешно отредактирована\n")
                else:
                    list_edit.append(line)
    with open('notes.csv', 'w') as notes:
        notes.writelines(list_edit)


def del_note(note_id):
    with open('notes.csv') as notes:
        list_del = []
        res = check_id(note_id)
        if res[0]:
            print("Заметки с таким id не найдено\n")
        else:
            for line in notes:
                if line != res[1]:
                    list_del.append(line)
            print("Заметка успешно удалена\n")
    with open('notes.csv', 'w') as notes:
        notes.writelines(list_del)


def check_id(note_id):
    with open('notes.csv') as notes:
        result = [True]
        for line in notes:
            list_line = line.split(';')
            if note_id == list_line[0]:
                result[0] = False
                result.append(line)
        return result


while True:
    match int(input('Если хотите добавить заметку, введите "1"; \n\n'
                    'Если хотите получить список заметок, введите "2"; \n\n'
                    'Если хотите вывести конкретную заметку, введите "3"; \n\n'
                    'Если хотите удалить заметку, введите "4"; \n\n'
                    'Если хотите вывести заметки за конкретную дату, введите "5"; \n\n'
                    'Если хотите редактировать заметку, введите "6"; \n\n'
                    'Если хотите выйти из программы, введите "7"; \n\n')):
        case 1:
            create_note()
        case 2:
            read_notes()
        case 3:
            read_note(input("Введите id заметки: "))
        case 4:
            del_note(input("Введите id заметки: "))
        case 5:
            read_note_by_date(input("Введите дату в формате dd.mm.yyyy: "))
        case 6:
            edit_note(input("Введите id заметки, которую вы хотите редактировать: "))
        case 7:
            break
