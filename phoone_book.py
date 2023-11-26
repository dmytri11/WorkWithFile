def show_all(file_name:str):
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))


def remove(file_name:str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(s)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)
        

def modify(file_name:str):
 
    
    old_data = find_by_attribute(file_name, True)
    
    print("Введите новые данные:\n")
    last_name_ = input('Введите фамилию: ')
    first_name_ = input('Введите имя: ')
    patronymic_ = input('Введите отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'
        
    with open(file_name, 'w',encoding='utf-8') as f:\
        f.writelines(data)


def find_by_attribute(file_name:str,option: bool):
    
    c = input("Введите 1 для поиска по фамилии, 2 для поиска по имени")
    
        
    opt = 0
    if c == '1':
        opt = 0
    elif c == '2':
        opt = 1
        
    attr = input("Введите имя/фамилию для поиска")
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя: ")
        return data[int(id)-1]
    
        
def copy(file_name: str, second_file: str):
   
    
    with open(file_name, 'r', encoding='utf-8') as f, open(second_file, 'w', encoding='utf-8') as s:
        data = f.readlines()
       
        for i, v in enumerate(data, 1):
            print(i,v)
        str_num = int(input("Введите строку пользователя: "))
        for i, v in enumerate(data, 1):
            if i == str_num:
                data2 = v
        s.writelines(data2)





def add_new(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    
    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')

 
def main():
    file_name = 'phonebook.txt'
    second_file = 'phonebook2.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск записи по имени/фамилии')
        print('6 - копирование записей в новый справочник')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_attribute(file_name,False))
        elif answer == '6':
            copy(file_name, second_file)
        elif answer == 'x':
            flag_exit = True

if __name__ == '__main__':
    main()
    