import xlrd
import numpy as np
from statistics import mean
from collections import Counter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book01 = xlrd.open_workbook('../Данные для Практики 1/01_Образование_организации_01.xls')
    book02 = xlrd.open_workbook('../Данные для Практики 1/01_Образование_организации_02.xls')
    print("количество листов в докуменет 01 = ",  book01.nsheets)

    table1 = book01.sheet_by_name('Отчет')
    table2 = book02.sheet_by_name('Отчет')
    num_rows01 = table1.nrows
    num_rows02 = table2.nrows
    num_cols01 = table1.ncols
    num_cols02 = table2.ncols




    specific_region = []
    for i in range (num_rows01 - 4):
        if(table1.cell(i+4, 0).value.find('федеральный округ') == -1):
            specific_region.append( table2.row_values(i+4, 1, 2) + table1.row_values(i+4, 1, 3) + table2.row_values(i+4, 2, 3))

    for i in range(len(specific_region)):
        for j in range(4):
            if(specific_region[i][j] == ''):
                specific_region[i][j] = 0
    print(specific_region)

    yearMax = 2015 + np.argmax(specific_region, axis =1 )
    print(yearMax)
    yearCounter = Counter(yearMax)
    print(yearCounter)

    count = 0
    regionAndValueOrganization = {}
    for i in range (num_rows01 - 4):
        if(table1.cell(i+4, 0).value.find('федеральный округ') == -1):
            regionAndValueOrganization[table1.cell(i+4, 0).value] = specific_region[count]
            count+=1
    print(regionAndValueOrganization)



    for i in range(len(regionAndValueOrganization)):
        avg = mean(specific_region[i])
        if(max(specific_region[i]) == specific_region[i][0]):
            yearMaxValue = 2015
        elif(max(specific_region[i]) == specific_region[i][1]):
            yearMaxValue = 2016
        elif(max(specific_region[i]) == specific_region[i][2]):
            yearMaxValue = 2017
        else:
            yearMaxValue = 2018
        specific_region[i].append(avg)
        specific_region[i].append(yearMaxValue)

    count = 0
    regionAndValueOrganization[table1.cell(i + 4, 0).value] = specific_region[count]
    for i in range(num_rows01 - 4):
        if (table1.cell(i + 4, 0).value.find('федеральный округ') == -1):
            regionAndValueOrganization[table1.cell(i + 4, 0).value] = specific_region[count]
            count += 1
    print(regionAndValueOrganization)


    def returnFifthElem(list):
        (a, b) = list
        return b[4]

    regionSorted = sorted(regionAndValueOrganization.items(), key = returnFifthElem)
    print(regionSorted)