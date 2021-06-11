from modules.manipulation_txt import remove_txt
from modules.creation_worksheet import create_list_worksheet_records, create_list_worksheet_accounts
from modules.view import print_dictionary, print_menu
from modules.get import total_by_account, total_by_date, total_by_person
TXT = 'errors.txt'

def main():
    remove_txt(TXT)
    BALANCE_BY_PERSON = 1
    BALANCE_BY_ACCOUNT = 2
    BALANCE_BY_DATE = 3
    EXIT = 4
    choice = 0
    LIST_WORKSHEET_RECORDS = create_list_worksheet_records()
    LIST_WORKSHEET_ACCOUNTS = create_list_worksheet_accounts()
    while True:
        print_menu()
        choice = int(input())
        if choice == EXIT:
            break

        if choice == BALANCE_BY_PERSON:
            print_dictionary(total_by_person(LIST_WORKSHEET_RECORDS, LIST_WORKSHEET_ACCOUNTS))
        
        elif choice == BALANCE_BY_ACCOUNT:
            print_dictionary(total_by_account(LIST_WORKSHEET_RECORDS, LIST_WORKSHEET_ACCOUNTS))
        
        elif choice == BALANCE_BY_DATE:
            print_dictionary(total_by_date(LIST_WORKSHEET_RECORDS))
if __name__ == '__main__':
    main()