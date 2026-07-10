import plotly.express as px
import plotly.graph_objects as go

from abc import ABC, abstractclassmethod
import pandas as pd
import os
import datetime
import calendar


class datasets(ABC):
    @abstractclassmethod
    def _fetch_dataset(self):
        pass


class create(ABC):
    @abstractclassmethod
    def _setting_datasets(self):
        pass


class fetch_dataset(datasets):
    def __init__(self, year='2023', month='3'):
        self._df = None
        self._year = year
        self._month = month
        self._fetch_dataset()

    def _fetch_dataset(self):
        dir_name = os.getcwd()
        if int(self._month) < 10:
            set_month = '0' + str(self._month)
        file_name = str(self._year) + set_month + '.csv'
        assets_file = dir_name + '/' + file_name
        self._df = pd.read_csv(assets_file)

    def __str__(self):
        return 'datasets'


class create_figure(create):
    # def __init__(self, datasets: datasets, area='長崎流体機', year='2023', month='01'):
    def __init__(self, datasets: datasets, items ,area, flag=[]):
        self._area = area
        self._year = datasets._year
        self._month = datasets._month
        self._title = items
        self._dates = []
        self._values = []
        self._flag = flag
        # print(flag)
        self._setting_datasets(datasets)

    def _setting_datasets(self, datasets):
        for _date in datasets._df['Date']:
            date = datetime.datetime.strptime(_date, '%Y-%m-%d %H:%M:%S')
            self._dates.append(date)

        for item in self._title:
            if item !='':
                self._values.append(datasets._df[str(item)].values)
            else:
                self._values=[]

    def create_figure(self, d_min, d_max):
        fig = go.Figure()
        # print(self._flag)
        if self._flag == ['True']:
            print(self._flag)
            dt_now = datetime.datetime.now()
            set_year = dt_now.year
            set_month = dt_now.month
            last_day = dt_now.day
            start_day = last_day - 1
        else:
            set_year = int(self._year)
            set_month = int(self._month)
            start_day = 1
            last_day = calendar.monthrange(set_year, set_month)[1]
        for index,value in enumerate(self._values):
            # fig.add_trace(go.Scatter(x=self._dates, y=value,
            #                       name=self._title[index],
            #                       opacity=0.9,mode='lines+markers'))
            fig.add_trace(go.Bar(x=self._dates, y=value,
                                  name=self._title[index],
                                  opacity=0.9))
            fig.update_xaxes(title='time',range=(datetime.date(set_year, set_month, start_day),
                                    datetime.date(set_year, set_month, last_day)))
            # fig.update_yaxes(title='availability', range=[d_min, d_max],showgrid=False)
            fig.update_yaxes(title='availability', range=[d_min, d_max])
            fig.update_layout(barmode='overlay')
            fig.update_layout(bargap=0)
        fig.update_layout(hovermode='closest')
        fig.update_layout(title=dict(text=f'<b>{self._year} 年 {self._month} 月 {self._area} 稼働率',font_color='green'))
        # fig.update_traces(marker_color='rgb(95, 158, 160)', marker_line_color='green',
        #         marker_line_width=1.5, opacity=0.6,name=self._title)
        return fig

    def __str__(self):
        return self._values


if __name__ == '__main__':

    datasets = fetch_dataset()