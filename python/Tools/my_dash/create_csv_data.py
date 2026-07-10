import os
import datetime
import pandas as pd
import numpy as np
import random
import csv
import math

"""make input data"""
# random test
# for i in range(6):
#     n = random.randint(0,100)
#     print(n)


def create_csv_file(set_year, set_month):
    license = ['NASTRAN','Abaqus','Fluent','CFX']
    nagasaki = ['Sandybridge','Ivybridge', 'Ivybridge2', 'Haswell', 'Broadwell', 'Skylake']
    takasago = ['R5_Ivybridge', 'R5_Haswell2', 'R5_Broadwell', 'R5_Broadwell2', 'R5_Skylake']
    kobe = ['Cascadelake', 'Milan']

    items = []
    for item in license:
        items.append(item)
    for item in nagasaki:
        items.append(item)
    for item in takasago:
        items.append(item)
    for item in kobe:
        items.append(item)

    # set_year = 2023
    # set_month = 3
    start_day = datetime.datetime(set_year,set_month,1,0,0,0)
    dates = []
    for i in range(31*24):
        dates.append(start_day)
        start_day += datetime.timedelta(hours=1)

    # make sample datasets(availability)
    datasets = []
    headers = 'Date'
    for item in items:
        # print(item)
        headers += ','+item
    # print(headers)

    csv_datasets = []
    csv_datasets.append(headers)
    for idx_t,t in enumerate(dates):
        lines = str(t)
        _radius = idx_t/5+(set_year/100+set_month)
        for idx, item in enumerate(items):
            # lines += ',' + str(random.randint(0,100)) + '%'
            # lines += ',' + str(random.randint(0,100))
            data=math.sin(math.radians(idx*45+_radius))
            # lines += ',' + str(int(abs(data)*100))
            lines += ',' + str(int(data/3*100+50))
        # print(lines)
        csv_datasets.append(lines)


    if set_month <10:
        str_set_month = '0'+str(set_month)

    #write file
    file_name = str(set_year) + str_set_month +'.csv'
    with open(file_name, 'w') as f_out:
        for item in csv_datasets:
            f_out.writelines(item)
            f_out.write('\n')

    #check result
    for item in csv_datasets:
        print(item)

if __name__ == '__main__':
    #test datetime
    dt_now = datetime.datetime.now()
    print(dt_now.year, dt_now.month, dt_now.day)
    print(type(dt_now.year))

    create_csv_file(2023, 4)