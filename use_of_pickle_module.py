"""
Pickling vs Unpickling
    Pickling in python refers to the process of serializing objects into binary streams.
    Unpickling is the inverse of that.

Pickling is useful when you want to save state of your objects and
    reuse them at another time without losing any instace specific data.

pickle.dumps(obj)
pickle.loads(obj)

"""

import pickle
data = {'a': 1, 'b': 2}
with open('my_data.pickle', 'wb') as f:
    pickle.dump(data, f)
with open('my_data.pickle', 'rb') as f:
    data_temp = pickle.load(f)