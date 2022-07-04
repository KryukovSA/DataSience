from collections import Counter
import math
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy import stats


def math_expectation(mas_values):
    result = 0.0
    for i in mas_values:
        result += i
    return result / len(mas_values)

def selective_dispersion(mas_values):
    result = 0.0
    mean = math_expectation(mas_values)
    for i in mas_values:
        result += (i - mean)**2
    return result / len(mas_values)

def initial_moment(mas_values, order):
    result = 0.0
    for i in mas_values:
        result += i ** order
    return result / len(mas_values)

def central_moment(mas_values, order):
    result = 0.0
    mean = math_expectation(mas_values)
    for i in mas_values:
        result += (i-mean) ** order
    return result / len(mas_values)

def median(mas_values):
    mas_values.sort()
    result = 0
    if (len(mas_values)%2 == 1):
        result = mas_values[(len(mas_values) - 1)/2 + 1]
    else:
        result = (mas_values[int((len(mas_values))/2)] + mas_values[int((len(mas_values))/2 + 1)])/2
    return result

def trimmed_mean(mas_values, share):
    tmp = []
    result = 0.0
    mas_values.sort()
    count_nums = int(len(mas_values)*share)
    if (count_nums%2 == 1):
        not_contained_from_beginning:int = (count_nums - 1)/2
        not_contained_from_end:int = count_nums - not_contained_from_beginning
        tmp = mas_values[int(not_contained_from_beginning):int(len(mas_values) - not_contained_from_end)]
    else:
        not_contained_from_beginning = count_nums/ 2
        not_contained_from_end = count_nums - not_contained_from_beginning
        tmp = mas_values[int(not_contained_from_beginning):int(len(mas_values) - not_contained_from_end)]
    for i in tmp:
        result += i
    return result/len(tmp)

def calculation_quantile(mas_values, share):
    mas_values.sort()
    count_nums = int(len(mas_values) * share)
    result = mas_values[count_nums-1]
    return result

qlevels = [0.05, .1, .25, .5, .75, .9, .95]



if __name__ == '__main__':
    book = xlrd.open_workbook('../Данные для Практики 2/02_Автоаварии.xls')
    table = book.sheet_by_index(0)  # severety=event_type

    list_temperature = []  # список всех показаний температуры
    visibility = []  # видимость дороги
    severity = []  # серьезность
    visibility_on_severity = {}  # словарь видимостей дороги по степени скрьезности аварии
    cities = []  # список городов
    distance = []  # список протяженностей участков
    distance_on_cities = {}  # словарь протяженностей участков дороги по городам
    wind_speed_on_severity = {}# словарь скоростей ветра по степени серьезности аварии
    wind_speed = [] #скорость ветра
    sample_size = table.nrows - 1

    for i in range(sample_size):
        if table.cell_value(i + 1, 18) == "":  # visibility
            visibility.append(0.0)
        else:
            visibility.append(float(table.cell_value(i + 1, 18)))
        severity.append(int(table.cell_value(i + 1, 3)))

        if table.cell_value(i + 1, 20) == "":  # wind_speed
            wind_speed.append(0.0)
        else:
            wind_speed.append(float(table.cell_value(i + 1, 20)))

        if visibility_on_severity.get(table.cell_value(i + 1, 3)) == None:
            visibility_on_severity[table.cell_value(i + 1, 3)] = []
        visibility_on_severity[table.cell_value(i + 1, 3)].append(visibility[i])

        if wind_speed_on_severity.get(table.cell_value(i + 1, 3)) == None:
            wind_speed_on_severity[table.cell_value(i + 1, 3)] = []
        wind_speed_on_severity[table.cell_value(i + 1, 3)].append(wind_speed[i])




#print(str(np.quantile(visibility, 0.1)) + "=" + str(calculation_quantile(visibility, 0.1)))
    print(wind_speed_on_severity)

    # fig, axes = plt.subplots(nrows=2, ncols=2, figsize = (18,10))
    # meanDynamics = []
    # trimMeanDynamics = []
    # medianDynamics = []
    # for severity_ in visibility_on_severity.keys():
    #     meanDynamics.append(np.mean(visibility_on_severity[severity_]))
    #     trimMeanDynamics.append(stats.trim_mean(visibility_on_severity[severity_], 0.1))
    #     medianDynamics.append(np.median(visibility_on_severity[severity_]))
    #     print(visibility_on_severity.keys(),meanDynamics )
    # axes[0][0].plot(visibility_on_severity.keys(), meanDynamics)
    # axes[0][1].plot(visibility_on_severity.keys(), trimMeanDynamics)
    # axes[1][0].plot(visibility_on_severity.keys(), medianDynamics)
    #
    # axes[0][0].legend(title = 'среднее', loc= 2)
    # axes[0][1].legend(title = 'усеч. среднее', loc= 2)
    # axes[1][0].legend(title='медиана', loc=2)
    # plt.show()

    #возвращает массив квантилей для данных  скорости ветра при выбранной категории аварии
    def quantiles(severity_):
        res = []
        for q in qlevels:
            res.append(np.quantile(wind_speed_on_severity[severity_], q))
        return res


    # plt.figure(figsize = (9, 5))
    # plt.plot(quantiles('1'), qlevels, label = 'severity 1')
    # plt.plot(quantiles('2'), qlevels, label='severity 2')
    # plt.plot(quantiles('3'), qlevels, label='severity 3')
    # plt.plot(quantiles('4'), qlevels, label='severity 4')
    # plt.legend(title = 'серьезность')
    # plt.show()

    def trimTails(severity_):
        data = wind_speed_on_severity[severity_]
        data.sort()
        data = data[0:-1]
        return data


    # plt.figure(figsize=(9, 5))
    # plt.boxplot([trimTails('1'), trimTails('2'), trimTails('3'), trimTails('4')], showmeans=True)
    # plt.xticks(np.arange(1, 5, step = 1), labels = [ 1, 2, 3, 4])
    # plt.title("коробчатая диаграмма дял распределения")
    # plt.ylabel("скорость")
    # plt.show()

    #моды
    print("мода = " + str(statistics.mode(round(x) for x in wind_speed_on_severity['2'])))
    print("мода = " + str(statistics.mode(round(x) for x in wind_speed_on_severity['1'])))
    print("мода = " + str(statistics.mode(round(x) for x in wind_speed_on_severity['4'])))
    print("мода = " + str(statistics.mode(round(x) for x in wind_speed_on_severity['3'])))