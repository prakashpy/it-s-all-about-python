"""


Google? How to check if no row returned pymssql python example

how to check if cursor object is empty?

Python, how to check if a result set is empty?

From <https://stackoverflow.com/questions/16561362/python-how-to-check-if-a-result-set-is-empty/16566112>

How to check if no row returned


Why would MySQL execute return None?

From <https://stackoverflow.com/questions/30421466/why-would-mysql-execute-return-none>

Step 3: Proof of concept connecting to SQL using pymssql

From <https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql>



"""


# try:
#
#     sql = "select my_key, my_value from table where product_id = {}".format(111)
#     conn = pymssql.connect("server_name", "user_name", "password", "current_db")
#     cursor = conn.cursor()
#     cursor.execute(sql)
#
#     for row in cursor:
#         my_key_list.append(str(row[0]))
#         my_val_list.append(str(row[1]))
#
#     conn.commit()
#     my_dummy_dict = dict(zip(my_key_list, my_val_list))
#
# except Exception as error:
#     print "my error message & {}".format(error)
#     #logging.error("error occured attempting to query breed DB for germplasm Ids")
#     #return