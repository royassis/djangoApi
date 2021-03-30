import pickle

obj_to_pickle = "im a string object"

with open('mypickle.pickle', 'wb') as f:
    pickle.dump(obj_to_pickle, f)