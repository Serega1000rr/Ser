from collections import OrderedDict, defaultdict
import zoo as menagerie
menagerie.hours()
plain ={'a':1, 'b':2,'c':3}
print(plain)
fancy = OrderedDict(plain)
print(fancy)
dict_of_lists=defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists)