# coding:utf-8
# import xlwings as xw
# from xlwings.constants import AxisType

# import os
# import csv
# htmlからのデータをcsvファイルに記録
# def write_csv(data):
#     datas = [data]
#     with open(os.getcwd()+'/app_folder/application/'+'data.csv','a') as f:
#         writer = csv.writer(f, lineterminator='\n')
#         writer.writerow(datas)

# coding:utf-8
import xlwings as xw
from xlwings.constants import AxisType
import numpy as np

# def deco(data):
#     global data_table
#     data_table = json.loads(data)

# htmlからのデータをcsvファイルに記録
def save(data):
    global x
    x = data

def save2(data):
    global y
    y = data

def save3(data):
    global x_uni
    x_uni = data

def save4(data):
    global y_uni
    y_uni = data

def save5(data):
    global tbl
    tablee = data
    a = len(tablee)
    b = int(a/3)
    table = np.array(tablee).reshape(b,3)

    tbl = [[0] * 2 for i in range(b-1)]
    for i in range(1,b):
        for j in range(1,3):
            tbl[i-1][j-1] = int(table[i][j].replace(",",""))

def write_csv():
        # エクセル読み込み
    wb = xw.Book()
    sht = wb.sheets[0]

    # グラフ作成
    sht.range("A1").value = tbl
    sht.range("A1").options(np.array,expand="table").value
    chart = sht.charts.add()
    chart.chart_type = "xy_scatter"
    chart.set_source_data(sht.range('A1').expand())


    # 軸目盛りを内向きに変更(xlInside=2)
    chart.api[1].Axes(AxisType.xlCategory).MajorTickMark = 2
    chart.api[1].Axes(AxisType.xlValue).MajorTickMark = 2

    # 軸ラベル
    x_label = x
    y_label = y
    x_unit = x_uni
    y_unit = y_uni

    chart.api[1].Axes(AxisType.xlCategory).HasTitle= True
    chart.api[1].Axes(AxisType.xlCategory).AxisTitle.Caption = x_label + "(" + x_unit + ")"
    chart.api[1].Axes(AxisType.xlValue).HasTitle= True
    chart.api[1].Axes(AxisType.xlValue).AxisTitle.Caption = y_label + "(" + y_unit + ")"

    # グリッド線オフ
    chart.api[1].Axes(AxisType.xlValue).HasMajorGridlines= False

    # グラフの外枠線消し
    chart.api[1].ChartArea.Format.Line.Visible = False

    # グラフの内枠(RGB=0x0>>黒)
    chart.api[1].PlotArea.Format.Line.Visible = True
    chart.api[1].PlotArea.Format.Line.ForeColor.RGB = 0x0
    chart.api[1].PlotArea.Format.Line.Weight = 0.5

    # 凡例の枠
    chart.api[1].Legend.Format.Line.Visible = True
    chart.api[1].Legend.Format.Line.ForeColor.RGB = 0x0
    chart.api[1].Legend.Format.Line.Weight = 0.5

    # 凡例消す
    chart.api[1].HasLegend = False
