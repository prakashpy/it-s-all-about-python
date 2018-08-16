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


try:

    sql = "select my_key, my_value from table where product_id = {}".format(111)
    conn = pymssql.connect("server_name", "user_name", "password", "current_db")
    cursor = conn.cursor()
    cursor.execute(sql)

    for row in cursor:
        my_key_list.append(str(row[0]))
        my_val_list.append(str(row[1]))

    conn.commit()
    my_dummy_dict = dict(zip(my_key_list, my_val_list))

except Exception as error:
    print "my error message & {}".format(error)
    #logging.error("error occured attempting to query breed DB for germplasm Ids")
    #return