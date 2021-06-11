import os
import xlrd
import datetime
from .validations import validate_has_value, validate_has_account
from .manipulation_txt import write_txt


FILENAME = 'sheet_money.xlsx'
PATH = os.path.abspath(FILENAME)
WORKBOOK = xlrd.open_workbook(PATH)
WORKSHEET_1 = WORKBOOK.sheet_by_index(0)
WORKSHEET_2 = WORKBOOK.sheet_by_index(1)
DATE = 0
VALUE = 1
ACCOUNT = 3

CLIENT = 1
INITIALS = 2

TXT = 'errors.txt'

def create_list_worksheet_records():
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
            write_txt(TXT, row, message_error, [formated_date, value, account])
        else:
            info_list.append([formated_date, value, account])
        
    return info_list

def create_list_worksheet_accounts():
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