# TODO решить с помощью list comprehension и распечатать его
import pprint


def makeDict(i):
    dictionary = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    return dictionary


myList = [makeDict(i) for i in range(16)]

pprint.pprint(myList)
