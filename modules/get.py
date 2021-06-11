from modules.creation_worksheet import ACCOUNT, INITIALS

PERSON = 0
DATE = 0
INITIALS = 1
VALUE = 1
ACCOUNT = 2

def total_by_account(LIST_WORKSHEET_1, LIST_WORKSHEET_2):
    accounts = {}
    for account in LIST_WORKSHEET_2:
        accounts[account[INITIALS]] = 0
    
    for records in LIST_WORKSHEET_1:
        accounts[records[ACCOUNT]] += records[VALUE]

    return accounts

def total_by_person(LIST_WORKSHEET_RECORDS, LIST_WORKSHEET_ACCOUNTS):
    persons_account = {}
    persons_value = {}
    for accounts in LIST_WORKSHEET_ACCOUNTS:
        if persons_account.get(accounts[PERSON]):
            persons_account[accounts[PERSON]].append(accounts[INITIALS])
        else:
            persons_account[accounts[PERSON]] = [accounts[INITIALS]]
    for person, initials in persons_account.items():    
        for account, value in total_by_account(LIST_WORKSHEET_RECORDS, LIST_WORKSHEET_ACCOUNTS).items():
            if account in initials:
                try:
                    persons_value[person] += value
                except KeyError:
                    persons_value[person] = value 
    return persons_value

def total_by_date(LIST_WORKSHEET_1):
    balance_by_date = {}
    for record in LIST_WORKSHEET_1:
        if balance_by_date.get(record[DATE]):
            balance_by_date[record[DATE]] += record[VALUE]
        else:
            balance_by_date[record[DATE]] = record[VALUE]
    return balance_by_date