import pickle

file_sample1 = open('sample_inner.obj', 'rb')
sample1 = pickle.load(file_sample1)
file_sample1.close()

file_sample2 = open('sample_suburban.obj', 'rb')
sample2 = pickle.load(file_sample2)
file_sample2.close()