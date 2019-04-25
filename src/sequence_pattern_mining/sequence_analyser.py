import os
import pandas as pd
import data_analyser
import activity


os.chdir('../../data')
data_analyser = data_analyser.DataAnalyser('article_sample.csv')
data = data_analyser.data

activity_analyser = activity.ActivityAnalyser()
print(activity_analyser.key_activity(df=data, pred_level='B', succ_level='A'))







