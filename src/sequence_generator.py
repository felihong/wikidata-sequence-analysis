import pandas as pd

class sequenceGenerator:

    def __init__(self, csvfile, jsThreshold):
        self.datafile = csvfile
        self.jsThreshold = jsThreshold

    """
    Convert the input csv file into dataframe
    """
    def _csv2df(self):
        return pd.read_csv(self.datafile, dtype={'item_id':int, 'user_id':str})

    """
    Generate database by selecting the non-null sequences satisfying the js-distance threshold
    """
    def generate_db(self):
        db = self._csv2df()[['item_id', 'user_id', 'edit_type', 'rev_timestamp', 'js_distance']].sort_values(by=['item_id','rev_timestamp'])
        filter = db.loc[db['js_distance'] >= self.jsThreshold][['item_id', 'user_id', 'edit_type']]
        return filter[filter.user_id.notnull()]

    """
    Generate the sequence database by integrating all edits conducted upon one article in a list, where
    the serial edits from the same editor are collapsed into one sub-list
    Args: 
        csv file of scheme: article_id : int
                            editor_id : int 
                            edit_type : string  
    Return:
        A list of list [[a], [b]], where a and b are collapsed edit types    
    """
    def generate_sequence(self):
        db = self.generate_db()
        df = db.groupby(['item_id','user_id']).agg({'edit_type': list})
        return df.values.tolist()
