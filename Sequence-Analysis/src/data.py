import pandas as pd
import numpy as np


class DataAnalyser():
    """
    Support some basic operations for showing and analysing the dataset.
    """


    def __init__(self, csvdata):
        data = pd.read_csv(csvdata, parse_dates=True, encoding='utf-8', sep=',',
                           dtype={'item_id': str,
                                  'item_name': str,
                                  'user_id': str,
                                  'user_editcount': str,
                                  'user_registration': str,
                                  'rev_id': str,
                                  'rev_len': str,
                                  'rev_timestamp': str,
                                  'itemquality_prediction': str,
                                  'itemquality_A': np.str,
                                  'itemquality_B': str,
                                  'itemquality_C': str,
                                  'itemquality_D': str,
                                  'itemquality_E': str
                                  })
        self.data = data


    def quality_count(self):
        data = self.data.loc[:, ['item_id', 'rev_id', 'itemquality_prediction']]
        return data.groupby([data.item_id, data.itemquality_prediction]).agg(['count'])













