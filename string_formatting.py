job_id = 10

# str.format()
project_path = '/tmp/jobs/{}'.format(str(job_id))

# %-formatting
print("path, %s, does not exist" %project_path)  # Output: path, /tmp/jobs/10, does not exist


# str.format()
print('Hi, my name is {1} & surname is {0}'.format("Patel", "Prakash"))  # Output: Hi, my name is Prakash & surname is Patel
print('Good {msg}'.format(msg = 'Morning'))  # Output: Good Morning


"""
Python 3's f-Strings
"""
name = "Patel Prakash"
temp_msg = "How are you?"

print(f"Hi my name is {name} & {temp_msg} is my message")  # Output: Hi my name is Patel Prakash & How are you? is my message
print(f"lower of my name:: {name.lower()}")  # Output: lower of my name:: patel prakash


# F-Strings are new and improved way to format strings in Python 3; uses __format__ protocol
# F-Strings are FASTER than % & .format()
## Reference:: https://realpython.com/python-f-strings/
