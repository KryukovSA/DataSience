from turtle import pd

import numpy as np
import xlrd
import scipy
import  math
import matplotlib.pyplot as plt
import sklearn as skl
import sklearn.model_selection
# Press the green button in the gutter to run the script.
from sklearn import model_selection
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression


def dataByType(data, type):
    res = []
    for rec in data:
        res.append(rec[type])
    return res


def getPartOfData(data, type):
    res = []
    for rec in data:
        res.append(rec[1:3])
    return res

def polynomicSample(data, degree):
    res = []
    for rec in data:
        for every in rec:
            for d in range(degree):
                res.append(every**(d+1))
    res = np.reshape(res, (len(data), -1))
    return res

if __name__ == '__main__':
    book = xlrd.open_workbook('../05_Зачисление.xls')
    table = book.sheet_by_index(0)

    serial_no = []
    gre_score = []
    toefl_score = []
    university_rating = []
    sop = []
    lor = []
    cgpa = []
    research= []
    chance_of_admit = []

    sample_size = table.nrows - 1

    for i in range(sample_size):
        serial_no.append(int(table.cell_value(i + 1, 0)))
        gre_score.append(int(table.cell_value(i + 1, 1)))
        toefl_score.append(int(table.cell_value(i + 1, 2)))
        university_rating.append(int(table.cell_value(i + 1, 3)))
        sop.append(float(table.cell_value(i + 1, 4)))
        lor.append(float(table.cell_value(i + 1, 5)))
        cgpa.append(float(table.cell_value(i + 1, 6)))
        research.append(int(table.cell_value(i + 1, 7)))
        chance_of_admit.append(float(table.cell_value(i + 1, 8)))

    print(serial_no)
    masDataIndicators = [] #массмв величин по которым будем оценивать шанс поступления
    masDataIndicators.append(gre_score)
    masDataIndicators.append(toefl_score)
    masDataIndicators.append(university_rating)
    masDataIndicators.append(sop)
    masDataIndicators.append(lor)
    masDataIndicators.append(cgpa)

    # fig, axes = plt.subplots(3, 2, figsize= (3*len(masDataIndicators), 3*len(masDataIndicators)))
    # count = 0
    # for i in range(3):
    #     for j in range(2):
    #             axes[i][j].scatter(masDataIndicators[count], chance_of_admit)
    #             count+=1
    # plt.show()

    magistratura_data = [] #все данные о поступающих
    for i in range(1, table.nrows):
        magistratura_data.append(table.row_values(i, 0, table.ncols))

    magistrTrain, magistrValidation = model_selection.train_test_split(magistratura_data, test_size=0.2, train_size=0.8)
    #прогноз шанса поступления на основе gre- независимая

    # добавим к независимым toifl
    exlist = []
    for i in range(len(dataByType(magistrTrain, 1))):
        tmp = []
        tmp.append(dataByType(magistrTrain, 1)[i])
        tmp.append(dataByType(magistrTrain, 2)[i])
        exlist.append(tmp)

    #exlist = exlist[:320]
    X = np.array(exlist)
    #print(len(X))

    X = np.reshape(X, (-1, 2))
    linR = LinearRegression().fit(X, dataByType(magistrTrain, 8))
    a = linR.coef_
    b = linR.intercept_
    print("Построена зависимость: Y = " + str(a[0]) + "X + " + str(b))

    Y_predict = linR.predict(np.reshape(dataByType(magistrValidation, 1), (-1, 1)))
    r2_1 = r2_score(dataByType(magistrValidation, 8), Y_predict)
    print("коэф детерминации = " + str(r2_1))

    mse_1 = mean_squared_error(dataByType(magistrValidation, 8), Y_predict)
    print("MSE = " + str(mse_1))
    print(dataByType(magistrValidation, 8))
    a = dataByType(magistrValidation, 8)
    a = np.array(a, dtype=np.float64)
    #rss_1 = ((a - Y_predict)**2).sum()

    #print("RSS остаточная сумма квадратов = " + str(rss_1))
    plt.scatter(dataByType(magistrValidation, 1), dataByType(magistrValidation, 8))
    plt.plot(dataByType(magistrValidation, 1), Y_predict, color = 'red')
    plt.title("модель множественной линейной регрессии")
    plt.xlabel("GRE score")
    plt.ylabel("шанс поступить")
    plt.show()

#добавим к независимым toifl


# plts = []
# plt.figure(figsize=(7,10))
# plt.scatter(dataByType(magistrValidation, 1), dataByType(magistrValidation, 8))
# plt.plot(dataByType(magistrValidation, 1), Y_predict, color = 'red')
# plts.append(plt.scatter(dataByType(magistrValidation, 1), Y_predict, color = 'red', label = "1"))
# plt.title("модель полиномиальной регрессии")
# plt.xlabel("GRE score")
# plt.ylabel("шанс поступить")
#
# r2 =[]
# r2.append(r2_1)
# er = []
# er.append(mse_1)
# rss =[]
# rss.append(rss_1)
#
# сolors = ["green", "blue", "black"]
# for d in [2, 3, 4]:
#     squareSample = polynomicSample(np.reshape(dataByType(magistrTrain, 1), (-1, 1)), d)
#     linR = linear_model.LinearRegression().fit(squareSample, dataByType(magistrTrain, 8))
#     Y_predict = linR.predict(polynomicSample(np.reshape(dataByType(magistrValidation, 1), (-1, 1)), d))
#     r2.append(r2_score(dataByType(magistrValidation, 8), Y_predict))
#     er.append(mean_squared_error(dataByType(magistrValidation, 8), Y_predict))
#     tmp = np.array(dataByType(magistrValidation, 8), dtype=np.float64)
#     rss.append(((tmp - Y_predict)**2).sum())
#
#     plts.append(plt.scatter(dataByType(magistrValidation, 1), Y_predict, color = сolors[d-2], label = str(d)))
# plt.legend(title = "Степень полинома:", handles = plts, labels = ["1", "2", "3", "4"])
# plt.show()
#
# print("%18s %12s %18s %18s" % ("Степень полинома", "R2", "MSE", "RSS"))
# models = [1,2,3,4]
# for i in range(len(r2)):
#     print("%18s %12s %18s %18s" % (models[i], r2[i], er[i], rss[i]))



