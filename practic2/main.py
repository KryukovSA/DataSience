from collections import Counter
import math
import xlrd
import matplotlib.pyplot as plt

book = xlrd.open_workbook('../Данные для Практики 2/02_Автоаварии.xls')
table = book.sheet_by_index(0) #severety=event_type

list_temperature = []#список всех показаний температуры
visibility = [] #видимость дороги
severity = [] #серьезность
visibility_on_severity = {}#словарь видимостей дороги по степени скрьезности аварии
cities = [] # список городов
distance = [] #список протяженностей участков
distance_on_cities = {} #словарь протяженностей участков дороги по городам

sample_size = table.nrows - 1

for i in range (sample_size):
    if(table.cell_value(i+1, 14) != ""): #temperature
        list_temperature.append(float(table.cell_value(i+1, 14)))
    if (table.cell_value(i + 1, 18) == ""): #visibility
        visibility.append(0.0)
    else:
        visibility.append(float(table.cell_value(i + 1, 18)))
    severity.append(int(table.cell_value(i + 1, 3)))

    if visibility_on_severity.get(table.cell_value(i+1, 3)) == None:
        visibility_on_severity[table.cell_value(i+1, 3)] = []
    visibility_on_severity[table.cell_value(i+1, 3)].append(visibility[i])

    cities.append(table.cell_value(i + 1, 10))
    distance.append((float(table.cell_value(i + 1, 6))))

    tmp = table.cell_value(i + 1, 10)
    if distance_on_cities.get(table.cell_value(i + 1, 10)) == None:
        if (str(tmp) == 'Sacramento' or str(tmp) == 'Dayton' or str(tmp) == 'San Jose' or str(tmp) == 'Columbus' or str(tmp) == 'Oakland'):
            distance_on_cities[table.cell_value(i + 1, 10)] = []
    if (distance_on_cities.get(table.cell_value(i + 1, 10)) != None) and (str(tmp) == 'Sacramento' or str(tmp) == 'Dayton' or str(tmp) == 'San Jose' or str(tmp) == 'Columbus' or str(tmp) == 'Oakland'):
        distance_on_cities[table.cell_value(i + 1, 10)].append(distance[i])


print(distance_on_cities)
cities_name_counter = Counter(cities)
print(cities_name_counter)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize = (9,6))
distance_on_cities['Sacramento'].sort()
distance_on_cities_stat_series = Counter(distance_on_cities['Sacramento'])
axes[0][0].hist(distance_on_cities['Sacramento'], bins = list(distance_on_cities_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
axes[0][0].set_title("протяженность участка дороги, задействованного при аварии в сакраменто")

distance_on_cities['Dayton'].sort()
distance_on_cities_stat_series = Counter(distance_on_cities['Dayton'])
axes[0][1].hist(distance_on_cities['Dayton'], bins = list(distance_on_cities_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
axes[0][1].set_title("протяженность участка дороги, задействованного при аварии в дайтон")

distance_on_cities['San Jose'].sort()
distance_on_cities_stat_series = Counter(distance_on_cities['San Jose'])
axes[1][0].hist(distance_on_cities['San Jose'], bins = list(distance_on_cities_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
axes[1][0].set_title("протяженность участка дороги, задействованного при аварии в сан хосе")

# distance_on_cities['Columbus'].sort()
# distance_on_cities_stat_series = Counter(distance_on_cities['Columbus'])
# axes[1][1].hist(distance_on_cities['Columbus'], bins = list(distance_on_cities_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# axes[1][1].set_title("протяженность участка дороги, задействованного при аварии в колумбусе")

distance_on_cities['Oakland'].sort()
visibility_on_severity_stat_series = Counter(distance_on_cities['Oakland'])
axes[1][1].hist(distance_on_cities['Oakland'], bins = list(visibility_on_severity_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
axes[1][1].set_title("протяженность участка дороги, задействованного при аварии в окланде")
fig.tight_layout()
plt.show()










severity_type_counter = Counter(severity)
#print(severity_type_counter)


list_temperature.sort() #вариационный ряд
temp_stat_series = Counter(list_temperature) #статический ряд

# x = plt.hist(list_temperature)
# plt.xlabel("температура в момент времени")
# plt.ylabel("количество наблюдений")
# plt.title("абсолютная частота встречаемости температуры")
# plt.show()

visibility.sort()
visibility_stat_series =Counter(visibility)
# plt.hist(visibility, bins=list(visibility_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# plt.title("Эмпирическая функция распределения видимости дороги \n в момент совершения аварии")
#plt.show()

k = int(math.log(sample_size, 2)) + 1 #кол-во промежутков Стерджеса
# plt.hist(visibility, bins=k, density=True)
# plt.title("нормированные частоты")
# plt.show()

#fig, axes = plt.subplots(nrows=2, ncols=2, figsize = (12,9))
# axes[0][0].hist(visibility_on_severity['1'], bins = int(math.log(severity_type_counter[1], 2)) + 1, density=True)
# axes[0][0].set_title("распределение видимости у аварий \n со степенью серьезности 1")
#
# axes[0][1].hist(visibility_on_severity['2'], bins = int(math.log(severity_type_counter[2], 2)) + 1, density=True)
# axes[0][1].set_title("распределение видимости у аварий \n со степенью серьезности 2")
#
# axes[1][0].hist(visibility_on_severity['3'], bins = int(math.log(severity_type_counter[3], 2)) + 1, density=True)
# axes[1][0].set_title("распределение видимости у аварий \n со степенью серьезности 3")
#
# axes[1][1].hist(visibility_on_severity['4'], bins = int(math.log(severity_type_counter[4], 2)) + 1, density=True)
# axes[1][1].set_title("распределение видимости у аварий \n со степенью серьезности 4")

# visibility_on_severity['1'].sort()
# visibility_on_severity_stat_series = Counter(visibility_on_severity['1'])
# axes[0][0].hist(visibility_on_severity['1'], bins = list(visibility_on_severity_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# axes[0][0].set_title("распределение видимости у аварий \n со степенью серьезности 1")
#
# visibility_on_severity['2'].sort()
# visibility_on_severity_stat_series = Counter(visibility_on_severity['2'])
# axes[0][1].hist(visibility_on_severity['2'], bins = list(visibility_on_severity_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# axes[0][1].set_title("распределение видимости у аварий \n со степенью серьезности 2")
#
# visibility_on_severity['3'].sort()
# visibility_on_severity_stat_series = Counter(visibility_on_severity['3'])
# axes[1][0].hist(visibility_on_severity['3'], bins = list(visibility_on_severity_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# axes[1][0].set_title("распределение видимости у аварий \n со степенью серьезности 3")
#
# visibility_on_severity['4'].sort()
# visibility_on_severity_stat_series = Counter(visibility_on_severity['4'])
# axes[1][1].hist(visibility_on_severity['4'], bins = list(visibility_on_severity_stat_series.keys()), density=True, cumulative=True, color="red", histtype='step', fill= False)
# axes[1][1].set_title("распределение видимости у аварий \n со степенью серьезности 4")






#fig.tight_layout()
#plt.show()




