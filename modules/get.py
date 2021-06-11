def total_by_account(LIST_WORKSHEET_1, LIST_WORKSHEET_2):
    accounts = {}
    for account in LIST_WORKSHEET_2:
        accounts[account[1]] = 0
    
    for info in LIST_WORKSHEET_1:
        accounts[info[2]] += info[1]

    return accounts

def total_by_person(LIST_WORKSHEET_1, LIST_WORKSHEET_2):
    persons_account = {}
    persons_value = {}
    for person in LIST_WORKSHEET_2:
        if persons_account.get(person[0]):
            persons_account[person[0]].append(person[1])
        else:
            persons_account[person[0]] = [person[1]]
    for person, accounts in persons_account.items():    
        for account, value in total_by_account(LIST_WORKSHEET_1, LIST_WORKSHEET_2).items():
            if account in accounts:
                try:
                    persons_value[person] += value
                except KeyError:
                    persons_value[person] = value 
    return persons_value

def total_by_date(LIST_WORKSHEET_1):
    balance_by_date = {}
    for date in LIST_WORKSHEET_1:
        if balance_by_date.get(date[0]):
            balance_by_date[date[0]] += date[1]
        else:
            balance_by_date[date[0]] = date[1]
    return balance_by_date