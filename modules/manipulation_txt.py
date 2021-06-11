import os

def verify_exists_txt(TXT):
    if os.path.exists(TXT):
        return True
    return False

def remove_txt(TXT):
    if verify_exists_txt(TXT):
        print('a')
        os.remove(TXT)

def write_txt(TXT, line, problem, content):
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