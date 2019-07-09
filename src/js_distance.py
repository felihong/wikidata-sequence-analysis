import os
import csv
from scipy.spatial.distance import jensenshannon

"""
Calculate the base 2 js-distance value of all adjacent revisions of the given dataset. 
Args:
    CSV dataset of item id, revision id, ORES probability of A,B, C, D and E.
Returns:
    A csv file of all revision ids and the respective js-distance values.
"""
class JS:

    def __init__(self, dataset):
        self.dataset= dataset

    """
    Transforming the csv input into a list of revision list
    """
    def _get_csv(self):
        with open(self.dataset) as f:
            input = csv.reader(f)
            list = []
            for index, line in enumerate(input):
                list.append(line)
        return list

    """
    Converting each ores-class probability from string into float.
    """
    def _make_float(self, dataset):
        for list in dataset[1:]:
            for i in range(2, len(list)):
                list[i] = float(list[i])
        return dataset

    """
    Check if two given sequences are in a parent-children relationship.
    """
    def _is_neighbor(self, list_p, list_q):
        return list_p[0] == list_q[0]

    """
    Compute the js-divergence value between each adjacent distributions, return the result as list of [rev, js] lists
    """
    def cal_distance(self):
        dataset = self._make_float(self._get_csv())
        result = []
        for i in range(1, len(dataset)-5):
            p, q = dataset[i], dataset[i + 1]
            if (self._is_neighbor(p, q)):
                js = jensenshannon(p[2:], q[2:], base=2)
                result.append([q[1], js])
            else:
                result.append([q[1], 0])
                i += 1
        return result

    """
    Write a list of [rev, js] lists into csv file.
    """
    def write_result(self, filename):
        result = self.cal_distance()
        file_exists = os.path.isfile(filename)
        with open(filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            if not file_exists:
                writer.writerow([
                    'rev_id',
                    'js_distance'])
            writer.writerows(result)
        csvFile.close()