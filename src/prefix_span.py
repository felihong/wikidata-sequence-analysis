import copy
import pandas as pd
from collections import defaultdict

class PrefixSpan:

    """
    Projects a sequence according to a given prefix, as done in PrefixSpan
    Args:
        sequence: the sequence the projection is built from
        prefix: the prefix that is searched for in the sequence
        newEvent: if set to True, the first itemset is ignored
    Returns:
        If the sequence does not contain the prefix, then None.
        Otherwise, a new sequence starting from the position of the prefix, including the itemset that includes the prefix
    """
    def project_sequence(self, sequence, prefix, newEvent):
        result = None
        for i, itemset in enumerate(sequence):
            if result is None:
                if (not newEvent) or i > 0:
                    if (all(x in itemset for x in prefix)):
                        result = [list(itemset)]
            else:
                result.append(copy.copy(itemset))
        return result

    """
    Projects a dataset according to a given prefix, as done in PrefixSpan
    Args:
        dataset: the dataset the projection is built from
        prefix: the prefix that is searched for in the sequence
        newEvent: if set to True, the first itemset is ignored
    Returns:
        A (potentially empty) list of sequences
    """
    def project_database(self, dataset, prefix, newEvent):
        projectedDB = []
        for sequence in dataset:
            seqProjected = self.project_sequence(sequence, prefix, newEvent)
            if not seqProjected is None:
                projectedDB.append(seqProjected)
        return projectedDB

    """ 
    Generates a list of all items that are contained in a dataset
    """
    def generate_items(self, dataset):
        return sorted(set([item for sublist1 in dataset for sublist2 in sublist1 for item in sublist2]))

    """ 
    Computes a defaultdict that maps each item in the dataset to its support
    """
    def generate_item_supports(self, dataset, ignoreFirstEvent=False, prefix=[]):
        result = defaultdict(int)
        for sequence in dataset:
            if ignoreFirstEvent:
                sequence = sequence[1:]
            cooccurringItems = set()
            for itemset in sequence:
                if all(x in itemset for x in prefix):
                    for item in itemset:
                        if not item in prefix:
                            cooccurringItems.add(item)
            for item in cooccurringItems:
                result[item] += 1
        return sorted(result.items())

    """
    The PrefixSpan algorithm. Computes the frequent sequences in a seqeunce dataset for a given minSupport
    Args:
        dataset: A list of sequence-lists, for which the frequent (sub-)sequences are computed
        minSupport: The minimum support that makes a sequence frequent
    Returns:
        A list of tuples (s, c), where s is a frequent sequence, and c is the count for that sequence
    """
    def prefix_span(self, dataset, minSupport):
        result = []
        itemCounts = self.generate_item_supports(dataset)
        for item, count in itemCounts:
            if count >= minSupport:
                newPrefix = [[item]]
                result.append((newPrefix, count))
                result.extend(self.prefix_span_internal(self.project_database(dataset, [item], False), minSupport, newPrefix))
        return result
    """
    Convert the list result of PrefixSpan algorithm into dataframe for ease of display, which is ordered by minSupport count
    """

    def prefix_span_display(self, dataset, minSupport):
        result = []
        itemCounts = self.generate_item_supports(dataset)
        for item, count in itemCounts:
            if count >= minSupport:
                newPrefix = [[item]]
                result.append((newPrefix, count))
                result.extend(
                    self.prefix_span_internal(self.project_database(dataset, [item], False), minSupport, newPrefix))
        df = pd.DataFrame(result).sort_values(by=[1], ascending=False)
        return df

    def prefix_span_internal(self, dataset, minSupport, prevPrefixes=[]):
        result = []

        # Add a new item to the last element (==same time)
        itemCountSameEvent = self.generate_item_supports(dataset, False, prefix=prevPrefixes[-1])
        for item, count in itemCountSameEvent:
            if (count >= minSupport) and item > prevPrefixes[-1][-1]:
                newPrefix = copy.deepcopy(prevPrefixes)
                newPrefix[-1].append(item)
                result.append((newPrefix, count))
                result.extend(self.prefix_span_internal(self.project_database(dataset, newPrefix[-1], False), minSupport, newPrefix))

        # Add a new event to the prefix
        itemCountSubsequentEvents = self.generate_item_supports(dataset, True)
        for item, count in itemCountSubsequentEvents:
            if count >= minSupport:
                newPrefix = copy.deepcopy(prevPrefixes)
                newPrefix.append([item])
                result.append((newPrefix, count))
                result.extend(self.prefix_span_internal(self.project_database(dataset, [item], True), minSupport, newPrefix))
        return result