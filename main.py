import csv
import recordworks as rw

exitToMainMenu = True
while True:
    print("Главное меню\n\n1.Добавление записи\n2.Поиск/Удаление/Экспорт по выборке\n3.Вывод всего справочника и экспорт по номеру\nЛюбой другой символ - выход из программы\n")
    menuItem = input("\nВведите пункт меню: ")
    if menuItem not in ['1','2','3']:
        print("ВсегО хорошегО")
        exit()
    if menuItem == "1":
        exitToMainMenu = False
        while not exitToMainMenu:
            s0 = input("Введите номер: ")
            s1 = input("Введите фамилию: ")
            s2 = input("Теперь имя: ")
            s3 = input("И наконец, отчество: ")
            if len(s0)>0:
                res=rw.addRecord(s0,s1,s2,s3)
                if res:
                    print("Запись добавлена")
                    exitToMainMenu = True
            else:
                # вот здесь навязчиво получается
                print("Номер должен быть уникальным\nи не может быть пустым...")
    elif menuItem == "2":
        exitToMainMenu = False
        while not exitToMainMenu:
            print("\nКак будем искать?\n\n--1 по номеру телефона\n--2 по фамилии\n--3 по имени\n--4 по отчеству, ну вдруг)\nЛюбой другой символ - выход из меню")
            menuItem1 = input("\nВведите пункт подменю: ")
            searchColumn = -1 # используется в качестве флага
            if menuItem1 == "1":
                subStr = input("Введите номер или его часть: ")
                searchColumn = 0
            elif menuItem1 =="2":
                subStr = input("Введите фамилию или её часть: ")
                searchColumn = 1
            elif menuItem1 =="3":
                subStr = input("Введите имя или его часть: ")
                searchColumn = 2
            elif menuItem1 =="4":
                subStr = input("Введите отчество или его часть: ")
                searchColumn = 3
            if searchColumn>-1:
                searchResult = rw.searchBy(searchColumn,subStr)
                if searchResult:
                    print(f"\nНайдено записей: {len(searchResult)}\n\n---Начало списка---")
                    for i in searchResult:
                        print(*i)
                    print("---Конец списка---\n")
                    print("Что будем делать с выборкой?\n----1 удалить из базы\n----2 экспорт в файл\n----9 выйти в меню поиска\n----0 выйти в главное меню")
                    menuItem2 = input("\nВыберите вариант действия: ")
                    if menuItem2 == "1":
                        # Неплохо бы переспросить
                        for i in searchResult:
                            print(f"Удаляем {i[0]}")
                            rw.delRecord(i[0])
                    elif menuItem2 == "2":
                        fileName = input("Введите имя файла или нажмите ввод,\nпо умолчанию export.csv:")
                        if fileName == "":
                            fileName = "export.csv"
                        with open(fileName, "w",encoding="utf-8",newline='') as csvfile:
                            writer = csv.writer(csvfile,delimiter=';',dialect="excel")
                            for i in searchResult:
                                writer.writerow(i)
                        print(f"Экспорт в файл {fileName} произведён")
                        exitToMainMenu = True
                    elif menuItem2 == "0":
                        exitToMainMenu = True
                else:
                    print("К сожалению, ничего не найдено!")
            else:
                exitToMainMenu = True
    elif menuItem == "3":
        print("\n---Начало списка---")
        with open("phones.csv", "r",encoding="utf-8",newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            res = list()
            count = 1
            for row in reader:
                res.append(row)
                print(f"{count}\t", end="")
                print(*row)
                count+=1
        print("---Конец списка---\n")
        numStr = input("Введите номер строки или любой другой символ для выхода в меню,\nрезультат будет в export.csv:")
        validStr = ""
        for i in numStr:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                validStr +=i
        if validStr!="":
            numStr = int(validStr)-1
            if numStr>-1 and numStr<len(res):
                with open("export.csv", "w",encoding="utf-8",newline='') as csvfile:
                    writer = csv.writer(csvfile,delimiter=';',dialect="excel")
                    writer.writerow(res[numStr])
