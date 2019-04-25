import csv
import matplotlib.pyplot as plt
import data_analyser


class ActivityAnalyser():

    def _check_improvement(df, index, level):
        tag = 'itemquality_' + level
        if ((df.iloc[index]['item_id'] == df.iloc[index - 1]['item_id']) and
                (df.iloc[index][tag] > df.iloc[index - 1][tag])):
            return True


    # ToDo: This fuction needs to be better grouped
    def activity_iterator(self, df):
        for group_key, group_value in df.groupby(('itemquality_prediction')):
            print(group_key)
            print(group_value['comment_simplified'])


    def key_activity(self, df, pred_level, succ_level):
        ''' This function shows all the activities leading to the given level change and the amount of that. '''
        counter = 0
        for i in range(len(df) - 1):
            if (df.iloc[i]['item_id'] == df.iloc[i + 1]['item_id']) and (
                    (df.iloc[i]['itemquality_prediction'] == pred_level) and (
                    df.iloc[i + 1]['itemquality_prediction'] == succ_level)):
                counter += 1
                print('%s => %s: %s' % (pred_level, succ_level, df.iloc[i + 1]['comment_simplified']))
        return counter
