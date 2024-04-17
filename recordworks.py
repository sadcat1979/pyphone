import csv,re

def validateNumber(strPhoneNumber):
    res = ""
    for i in strPhoneNumber:
        if i in ['+','0','1','2','3','4','5','6','7','8','9']:
            res += i
    if len(res)>0:
        return res
    return False

def addRecord(unvalidatedPhone,lastName,firstName,surName):
    phone = validateNumber(unvalidatedPhone)
    if not phone:
        print("Номер не корректен!")
        return False
    rec = searchBy(0,phone)
    if rec:
        print("Невозможно добавить, номер не уникален")
        for i in rec:
            print(*i)
        return False
    with open("phones.csv", "a",encoding="utf-8",newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter=';',dialect="excel")
        writer.writerow([phone,lastName,firstName,surName])
    return True

def searchBy(column,searchString):
    if searchString=='':
        return False
    if column not in [0,1,2,3]:
        return False
    flag = False
    with open("phones.csv", "r",encoding="utf-8",newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        res = list()
        for row in reader:
            if len(row)>0 and searchString.upper() in row[column].upper():
                res.append(row)
                flag = True
    if flag:
        return res
    return False

def delRecord(str): # творчество со Stack Overflow
    pattern = re.compile(re.escape(str)) # особенно вот это
    with open("phones.csv", 'r+', encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
