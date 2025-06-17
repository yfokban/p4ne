from typing import reveal_type

import matplotlib
import openpyxl

from matplotlib import pyplot
from openpyxl import load_workbook

excel = load_workbook('C:\\Работка\\Python learning\\data_analysis_lab.xlsx')

sheet = excel['Data'] #Import Data sheet

columnA = sheet['A'][1:] #Import A column
columnC = sheet['C'][1:] #Import C column
columnD = sheet['D'][1:] #Import D column

#Test output
print(columnA[0].value)
print(columnC[0].value)
print(columnD[0].value)

def getvalue(x):
    return x.value

list_x = list(map(getvalue, columnA))
list_y1 = list(map(getvalue, columnC))
list_y2 = list(map(getvalue, columnD))

#Test list function
print(list_x)

#Graphic visualization
pyplot.plot(list_x, list_y1)
pyplot.plot(list_x, list_y2)

#Show our graphic
pyplot.show()
