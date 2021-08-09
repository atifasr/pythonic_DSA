

import re

from re import split
from typing import List

# grouping is done by ()
# p = re.compile('\d+')

# print(p.findall('this is 8th november 1889'))

# regex = re.compile("[a-zA-Z].")

# print(regex.findall('this is awesome June 13'))


# # \d+ will match a group on [0-9], group of one or greater size
# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


# p = re.compile('a*b*c')
# print(p.findall('abcabcaaaabbbcbbc'))


# print(split('\W+', 'wordsone, words2, words3'))
# destructuring


def generators(val):
    list_ = range(1, val)
    for val in list_:
        yield val


gen_list = generators(5)
print(gen_list)
print(gen_list.__next__())
print(gen_list.__next__())
print(gen_list.__next__())
