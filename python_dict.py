# Dictionary is mutable
# Dictionaries are unordered. Elements are not kept in any specific order. "UNORDERED"

first_team = {'key1': 'val1', "key2": 2.0, """key3""": """3"""}
print first_team['key3']  # output: 3

# converting list of tuples to Dict
my_team = [('John','SH009'),('James','AB178'),('Larry','PQ345')]
print dict(my_team)  # output: {'James': 'AB178', 'Larry': 'PQ345', 'John': 'SH009'}

# Adding entry to existing dictionary
first_team['key4'] = 'Rocking'
print first_team  # output: {'key3': '3', 'key2': 2.0, 'key1': 'val1', 'key4': 'Rocking'}

del first_team['key3']
print first_team  # output: {'key2': 2.0, 'key1': 'val1', 'key4': 'Rocking'}

print first_team.get('key4')  # output: Rocking

# to get list of tuples containing the key value pair in dictionary
print first_team.items()  # output: [('key2', 2.0), ('key1', 'val1'), ('key4', 'Rocking')]

print first_team.keys()  # output: ['key2', 'key1', 'key4']
print first_team.values()  # output: [2.0, 'val1', 'Rocking']


first_team.clear()  # to clear dictionary

# d.popitem() ==>> removes a random, arbitrary key-value pair from d and returns it as a tuple

import pymssql
my_key_list = []
my_val_list = []


tkp = {'key1':'val1', 'key2':'val'}

for key, val in tkp.iteritems():
    print "key:", key, " & val:", val
#  output: key: key2  & val: val \n key: key1  & val: val1
for index, key in enumerate(tkp):
    print "index: ",index," &key: ",key,"&value:",tkp[key]
#  output: index:  0  &key:  key2 &value: val \n index:  1  &key:  key1 &value: val1

# item returns list of tuples with key-val --> crosscheck
for k, v in tkp.items():
    print k,v

""" 
In python 2.x the above examples using items would return a list with tuples containing the copied key-value pairs of the dictionary. 
In order to not copy and with that load the whole dictionary’s keys and values inside a list to the memory 
you should prefer the iteritems method which simply returns an iterator instead of a list. 
In Python 3.x the iteritems is removed and the items method returns view objects. 
The benefit of these view objects compared to the tuples containing copies is that every change made to the dictionary is reflected in the view objects.
"""

## <3
## Code below is the pythonic style for iterating through a dictionary
d = {"first_name": "Alfred", "last_name":"Hitchcock"}

for key,val in d.items():
    print("{} = {}".format(key, val))
