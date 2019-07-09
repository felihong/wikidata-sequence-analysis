from prefix_span import PrefixSpan
from js_distance import JS
from sequence_generator import sequenceGenerator
import pandas as pd


if __name__ == '__main__':

    seq = sequenceGenerator(csvfile='/Users/hongzhu/desktop/back_up.csv', jsThreshold=0.01)
    data = seq.generate_sequence()
    print(len(data))

    prex = PrefixSpan()
    result_df = prex.prefix_span_display(dataset=data, minSupport=5)
    print(result_df)












