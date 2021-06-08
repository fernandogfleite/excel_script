import xlrd
import os
import datetime

FILENAME = 'sheet_money.xlsx'
PATH = os.path.abspath(FILENAME)
WORKBOOK = xlrd.open_workbook(PATH)
WORKSHEET_1 = WORKBOOK.sheet_by_index(0)
WORKSHEET_2 = WORKBOOK.sheet_by_index(1)

DATE = 0
VALUE = 1
ACCOUNT = 3

def write_txt(line, problem, content):
    file = open("errors.txt", "w")
    file.write(f"On line {line} {problem}")    


def create_list():
    info_list = []
    for row in range(1, WORKSHEET_1.nrows):
        value = 0
        date = ''
        account = ''
        error = 0
        for col in range(WORKSHEET_1.ncols):
            if col == VALUE:
                value = WORKSHEET_1.cell_value(row, col)

            elif col == DATE:
                date = WORKSHEET_1.cell_value(row,col)
                converted_date = xlrd.xldate_as_tuple(date, WORKBOOK.datemode)
                formated_date = datetime.datetime(*converted_date).strftime("%d/%m/%y")
            
            elif col == ACCOUNT:
                account = WORKSHEET_1.cell_value(row, col)
        if error == 0:
            info_list.append([formated_date, value, account])

    return info_list

print(create_list())