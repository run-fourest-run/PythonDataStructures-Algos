'''
Common use of dictionaries is to count the occurences of like items in a sequence. A typical example is counting the occurences of
words in a body of text. The following code creates a dictionaries where each word in the text is used as a key and the number of occurences as it's value.



'''


def wordcount(fname):
    with open(fname) as f:
        count = dict()
        for line in f:
            words = line.split()
            for word in words:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] += 1
        return count


