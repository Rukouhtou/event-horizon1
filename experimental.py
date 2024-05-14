import numpy as np

sample1 = 'melee'

set1 = set(sample1)
dict1 = {c:i for i,c in enumerate(set1)}
print(set1)
print(dict1)
sample_idx = [dict1[c] for c in sample1]
print(sample_idx)
x_data = [sample_idx[:-1]]
print(x_data)

input_size = len(set1)

x_one_hot = np.array([np.eye(input_size)[x] for x in x_data])
print(x_one_hot)
