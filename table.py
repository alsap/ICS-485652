from prettytable import PrettyTable
from data import dt
x = PrettyTable()

x.field_names = ['Підприємство', 'виду основних засобів', 'Залишок на 1.01.2018', 'Надійшло у 2018','Вибуток у 2018']

for i in range (0, len(dt)):

    x.add_rows(
    [
        dt[i]
    ]
    )

def opentable():
    print(x)