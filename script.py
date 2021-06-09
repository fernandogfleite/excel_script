import xlrd
import os
import datetime

FILENAME = 'sheet_money.xlsx'
PATH = os.path.abspath(FILENAME)
WORKBOOK = xlrd.open_workbook(PATH)
WORKSHEET_1 = WORKBOOK.sheet_by_index(0)
WORKSHEET_2 = WORKBOOK.sheet_by_index(1)
TXT = 'errors.txt'

DATE = 0
VALUE = 1
DESCRIPTION = 2
ACCOUNT = 3

CLIENT = 1
INITIALS = 2

def verify_exists_txt(TXT):
    if os.path.exists(TXT):
        return True
    return False

def write_txt(line, problem, content):
    file = None
    contentTXT = []
    if verify_exists_txt(TXT):
        file = open(TXT, "r")
        contentTXT = file.readlines()

    file = open(TXT, "w")
    contentTXT.append(f"Line {line+1}\n")
    contentTXT.append(f'{problem}\n')
    information = ''
    for work in content:
        information += f'{work} '
    contentTXT.append(f'{information} \n\n') 
    file.writelines(contentTXT)
    file.close()

def validate_has_value(value):
    value = value
    if value == "":
        raise ValueError("")
    return value

def validate_has_account(account):
    account = account
    if account == "":
        raise ValueError("Has no account")
    return account

def create_list_worksheet1():
    info_list = []
    for row in range(1, WORKSHEET_1.nrows):
        value = 0
        date = ''
        account = ''
        error = 0
        message_error = ''
        for col in range(WORKSHEET_1.ncols):
            if col == VALUE:
                try:
                    value = validate_has_value(WORKSHEET_1.cell_value(row, col))
                except ValueError as e:
                    error += 1
                    value = e
                    message_error = 'Has no value'
            elif col == DATE:
                date = WORKSHEET_1.cell_value(row,col)
                converted_date = xlrd.xldate_as_tuple(date, WORKBOOK.datemode)
                formated_date = datetime.datetime(*converted_date).strftime("%d/%m/%y")
            
            elif col == ACCOUNT:
                try:
                    account = validate_has_account(WORKSHEET_1.cell_value(row, col))
                except ValueError as e:
                    error += 1
                    account = WORKSHEET_1.cell_value(row, col)
                    message_error = 'Has no account'
        if error > 0:
            write_txt(row, message_error, [formated_date, value, account])
        else:
            info_list.append([formated_date, value, account])
        
    return info_list

def create_list_worksheet2():
    info_list = []
    for row in range(1, WORKSHEET_2.nrows):
        client = ''
        initials = ''
        for col in range(WORKSHEET_2.ncols):
            if col == CLIENT:
                client = WORKSHEET_2.cell_value(row,col)
            elif col == INITIALS:
                initials = WORKSHEET_2.cell_value(row, col)
        info_list.append([client, initials])
    return info_list

def total_by_account():
    accounts = {}
    for account in create_list_worksheet2():
        accounts[account[1]] = 0
    
    for info in create_list_worksheet1():
        accounts[info[2]] += info[1]

    return accounts

def total_by_person():
    persons_account = {}
    persons_value = {}
    for person in create_list_worksheet2():
        if persons_account.get(person[0]):
            persons_account[person[0]].append(person[1])
        else:
            persons_account[person[0]] = [person[1]]
    for person, accounts in persons_account.items():    
        for account, value in total_by_account().items():
            if account in accounts:
                try:
                    persons_value[person] += value
                except KeyError:
                    persons_value[person] = value 
    return persons_value

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: R${value}')

def print_menu():
    print("""
    Escolha uma das opções abaixo
    1 - Saldo total por cliente
    2 - Saldo total por conta
    3 - Sair
    """)

def main():
    BALANCE_BY_PERSON = 1
    BALANCE_BY_ACCOUNT = 2
    EXIT = 3
    choice = 0
    while True:
        print_menu()
        choice = int(input())
        if choice == EXIT:
            break

        if choice == BALANCE_BY_PERSON:
            if verify_exists_txt(TXT):
                os.remove(TXT)
            print_dictionary(total_by_person())
        
        elif choice == BALANCE_BY_ACCOUNT:
            if verify_exists_txt(TXT):
                os.remove(TXT)
            print_dictionary(total_by_account())

if __name__ == '__main__':
    main()