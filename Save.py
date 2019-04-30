import openpyxl


def WriteFile(info):
    file = openpyxl.load_workbook("유저정보.xlsx")
    sheet = file.active
    for i in range(1, 51):
        if sheet["A" + str(i)].value == "-" or sheet["A" + str(i)].value == info[1]:
            sheet["A" + str(i)].value = info[1]
            sheet["B" + str(i)].value = info[2]
            sheet["C" + str(i)].value = info[3]
            sheet["D" + str(i)].value = info[4]
            sheet["E" + str(i)].value = info[5]
            break
    file.save("유저정보.xlsx")


def ReadFile(info):
    file = openpyxl.load_workbook("유저정보.xlsx")
    sheet = file.active
    memory = info
    for i in range(1, 51):
        if sheet["A" + str(i)].value == memory[1]:
            xlseValue1 = sheet["A" + str(i)].value
            xlseValue2 = sheet["B" + str(i)].value
            xlseValue3 = sheet["C" + str(i)].value
            xlseValue4 = sheet["D" + str(i)].value
            xlseValue5 = sheet["E" + str(i)].value
            break


