from spyre import  server
import pandas as pd
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np


class StockExample(server.App):
    title = "Inputs"

    inputs = [{   "type":'dropdown',
                  "label": 'Index  ',
                  "options" : [ {"label": "VCI", "value":"VCI"},
                                {"label": "TCI", "value":"TCI"},
                                {"label": "VHI", "value":"VHI"},],
                  "key": 'index',
                  "action_id": "update_data"},

              {"type": 'dropdown',
               "label": 'Region',
               "options": [{"label": "Vinnitsya", "value": "1"},
                           {"label": "Volyn", "value": "2"},
                           {"label": "Dnipropetrovsk", "value": "3"},
                           {"label": "Donetsk", "value": "4"},
                           {"label": "Zhytomyr", "value": "5"},
                           {"label": "Zacarpathia", "value": "6"},
                           {"label": "Zaporizhzhya", "value": "7"},
                           {"label": "Ivano-Frankivsk", "value": "8"},
                           {"label": "Kiev", "value": "9"},
                           {"label": "Kirovohrad", "value": "10"},
                           {"label": "Luhansk", "value": "11"},
                           {"label": "Lviv", "value": "12"},
                           {"label": "Mykolayiv", "value": "13"},
                           {"label": "Odessa", "value": "14"},
                           {"label": "Poltava", "value": "15"},
                           {"label": "Rivne", "value": "16"},
                           {"label": "Sumy", "value": "17"},
                           {"label": "Ternopil", "value": "18"},
                           {"label": "Kharkiv", "value": "19"},
                           {"label": "Kherson", "value": "20"},
                           {"label": "Khmelnytskyy", "value": "21"},
                           {"label": "Cherkasy", "value": "22"},
                           {"label": "Chernivtsi", "value": "23"},
                           {"label": "Chernihiv", "value": "24"},
                           {"label": "Crimea", "value": "25"}],
               "key": 'region',
               "action_id": "update_data"},

              {"input_type": "text",
               "variable_name": "year",
               "label": "Year",
               "value": 1981,
               "key": 'year',
               "action_id": "update_data"},

              {"type": 'slider',
               "label": 'First week',
               "min": 1, "max": 52, "value": 35,
               "key": 'first',
               "action_id": 'update_data'},

              {"type": 'slider',
               "label": 'Last week',
               "min": 1, "max": 52, "value": 35,
               "key": 'last',
               "action_id": 'update_data'}]


    controls = [{"type": "hidden",
                 "id": "update_data"}]

    tabs = ["Table","Plot"]

    outputs = [{"type": "table",
                "id": "table_id",
                "control_id": "update_data",
                "tab": "Table"},
               {"type": "plot",
                "id": "plot",
                "control_id": "update_data",
                "tab": "Plot"}]

    def getData(self, params):
        print("............")
        index = params['index']
        region = params['region']
        year = params['year']
        first = params['first']
        last = params['last']

        path = r"for_lab2/%s.csv" % region
        print(path)
        df = pd.read_csv(path)
        df1 = df[(df['Year'] == int(year)) & (df['Week'] >= int(first)) & (df['Week'] <= int(last))]
        df1 = df1[['Week', index]]
        return df1

    def getPlot(self, params):
        index = params['index']
        region = params['region']
        year = params['year']
        first = params['first']
        last = params['last']
        df = self.getData(params).set_index('Week')
        plt_obj = df.plot()
        plt_obj.set_ylabel(r"%s" % index)
        plt_obj.set_title('Index {index} for {year} from {first} to {last} weeks'.format(index=index,
                                                                                         year=int(year),
                                                                                         first=int(first),
                                                                                         last=int(last)))

        fig = plt_obj.get_figure()
        return fig



app = StockExample()
app.launch()
