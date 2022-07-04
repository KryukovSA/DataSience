import numpy as np
import xlrd
import scipy
import  math
import matplotlib.pyplot as plt

def math_expectation1(mas_values):
    result = 0.0
    for i in mas_values:
        result += i
    return result / len(mas_values)

def selective_dispersion(mas_values):
    result = 0.0
    mean = math_expectation1(mas_values)
    for i in mas_values:
        result += (i - mean)**2
    return result / len(mas_values)

#мат ожидание температуры, видимости,  серьезности, влажности, скорости ветра
def math_expectation(mas_data):
    res_expectation = []
    for j in range(len(mas_data)):
        result = 0.0
        for i in mas_data[j]:
            result += i
        result = result / len(mas_data[j])
        res_expectation.append(result)
    return res_expectation

def covariation(mas_data):
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    res_vector = []
    for i in range(len(mas_data[0])):
        sum1 += (mas_data[0][i] - scipy.mean(mas_data[0]))*(mas_data[0][i] - scipy.mean(mas_data[0]))
        sum2 += (mas_data[0][i] - scipy.mean(mas_data[0]))*(mas_data[1][i] - scipy.mean(mas_data[1]))
        sum3 += (mas_data[1][i] - scipy.mean(mas_data[1]))*(mas_data[1][i] - scipy.mean(mas_data[1]))
    res_vector.append(sum1/len(mas_data[0]))
    res_vector.append(sum2/len(mas_data[0]))
    res_vector.append(sum2 / len(mas_data[0]))
    res_vector.append(sum3 / len(mas_data[0]))
    return res_vector

def correlation(mas_data):
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    res_vector = []
    for i in range(len(mas_data[0])):
        sum1 += (mas_data[0][i] - scipy.mean(mas_data[0]))*(mas_data[0][i] - scipy.mean(mas_data[0]))
        sum2 += (mas_data[0][i] - scipy.mean(mas_data[0]))*(mas_data[1][i] - scipy.mean(mas_data[1]))
        sum3 += (mas_data[1][i] - scipy.mean(mas_data[1]))*(mas_data[1][i] - scipy.mean(mas_data[1]))
    res_vector.append((sum1/len(mas_data[0])) / selective_dispersion(mas_data[0]))
    res_vector.append(sum2/len(mas_data[0]) / math.sqrt(selective_dispersion(mas_data[0]))  / math.sqrt(selective_dispersion(mas_data[1])))
    res_vector.append(sum2 / len(mas_data[0]) / math.sqrt(selective_dispersion(mas_data[1]))  / math.sqrt(selective_dispersion(mas_data[0])))
    res_vector.append(sum3 / len(mas_data[0]) / selective_dispersion(mas_data[1]))
    return res_vector


if __name__ == '__main__':
    book = xlrd.open_workbook('../Данные для Практики 2/02_Автоаварии.xls')
    table = book.sheet_by_index(0)  # severety=event_type

    list_temperature = []  # список всех показаний температуры
    visibility = []  # видимость дороги
    severity = []  # серьезность
    humidity = [] #влажность
    wind_speed = [] #скорость ветра
    masData5Indicators = [] #массив выборочных значений для 5 вышеобозначенных величин
    bump = [] #наличие вблизи лежачего полицейского
    crossing = []  # наличие вблизи перекрестка
    give_way = []
    junction = []
    no_exit = []
    mas_qualitives_data = [] #массив выборочных знач для качественных данных
    # visibility_on_severity = {}  # словарь видимостей дороги по степени скрьезности аварии
    # cities = []  # список городов
    # distance = []  # список протяженностей участков
    # distance_on_cities = {}  # словарь протяженностей участков дороги по городам
    # wind_speed_on_severity = {}# словарь скоростей ветра по степени серьезности аварии

    sample_size = table.nrows - 1

    for i in range(sample_size):
        if (table.cell_value(i + 1, 14) != ""):  # temperature
            list_temperature.append(float(table.cell_value(i + 1, 14)))
        else:
            list_temperature.append(0.0)

        if table.cell_value(i + 1, 18) == "":  # visibility
            visibility.append(0.0)
        else:
            visibility.append(float(table.cell_value(i + 1, 18)))

        severity.append(int(table.cell_value(i + 1, 3))) #severity

        if table.cell_value(i + 1, 20) == "":  # wind_speed
            wind_speed.append(0.0)
        else:
            wind_speed.append(float(table.cell_value(i + 1, 20)))

        if table.cell_value(i + 1, 16) == "":  # humidity
            humidity.append(0.0)
        else:
            humidity.append(float(table.cell_value(i + 1, 16)))

        if table.cell_value(i + 1, 23) == "":  # bump
            bump.append(False)
        else:
            bump.append(table.cell_value(i + 1, 23))

        if table.cell_value(i + 1, 24) == "":  # crossing
            crossing.append(False)
        else:
            crossing.append(table.cell_value(i + 1, 24))
        give_way.append(table.cell_value(i + 1, 25))
        junction.append(table.cell_value(i + 1, 26))
        no_exit.append(table.cell_value(i + 1, 27))
        #
        # if visibility_on_severity.get(table.cell_value(i + 1, 3)) == None:
        #     visibility_on_severity[table.cell_value(i + 1, 3)] = []
        # visibility_on_severity[table.cell_value(i + 1, 3)].append(visibility[i])
        #
        # if wind_speed_on_severity.get(table.cell_value(i + 1, 3)) == None:
        #     wind_speed_on_severity[table.cell_value(i + 1, 3)] = []
        # wind_speed_on_severity[table.cell_value(i + 1, 3)].append(wind_speed[i])

masData5Indicators.append(list_temperature);
masData5Indicators.append(visibility);
masData5Indicators.append(severity);
masData5Indicators.append(humidity);
masData5Indicators.append(wind_speed);


mas_qualitives_data.append(bump)
mas_qualitives_data.append(crossing)
mas_qualitives_data.append(give_way)
mas_qualitives_data.append(junction)
mas_qualitives_data.append(no_exit)

types = ['температура', 'visibility', 'severity', 'humidity', 'wind_speed']
types_qualitative = ['лежач полиц', 'перекресток', 'уступи дорогу', 'вблизи развязки', 'нет выхода']
math_exp_data=[]
for i in range(len(masData5Indicators)):
    math_exp_data.append(np.mean(masData5Indicators[i]))

#print(str(correlation(masData5Indicators)) + "=" + str(np.corrcoef(masData5Indicators[:2])))

# fig, axes = plt.subplots(len(masData5Indicators), len(masData5Indicators), figsize= (3*len(masData5Indicators), 3*len(masData5Indicators)) )
# for i in range(len(masData5Indicators)):
#     for j in range(len(masData5Indicators)):
#         if(i == j):
#             axes[i][j].annotate(types[i], (0.5, 0.5), ha = 'center')
#             axes[i][j].xaxis.set_visible(False)
#             axes[i][j].yaxis.set_visible(False)
#         else:
#             axes[i][j].scatter(masData5Indicators[i], masData5Indicators[j])
# plt.show()
colors = ["red", "blue", "green", "red", "blue", "green"]
fig, axes = plt.subplots(len(types_qualitative), figsize= (20, 12))

for j in range(len(types_qualitative)):
            axes[j].scatter(masData5Indicators[2], mas_qualitives_data[j], c = colors[j])
            axes[j].set_xlabel(types[2])
            axes[j].set_ylabel(types_qualitative[j])
plt.show()