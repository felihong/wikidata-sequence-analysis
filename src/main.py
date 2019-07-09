import os
from prefix_span import PrefixSpan
from sequence_generator import SequenceGenerator

module_path = os.path.abspath(os.path.join('/src'))

if __name__ == '__main__':
    seq = SequenceGenerator(csvfile='~/db/csvfile.csv', jsThreshold=0.01)
    data = seq.generate_sequence()
    print(len(data))

    prex = PrefixSpan()
    result_df = prex.prefix_span_display(dataset=data, minSupport=5)
    print(result_df)
