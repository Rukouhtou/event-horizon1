import torch
import numpy as np
import pprint

sample = ' this world is an illusion.'

char_set = list(set(sample))
char_dict = {c:i for i, c in enumerate(char_set)}
pprint.pprint(char_set)
pprint.pprint(char_dict)

sample_idx = [char_dict[c] for c in sample]
x_data = [sample_idx[:-1]]
print(x_data)

# hyper parameters
input_size = len(char_set)
hidden_size = len(char_set)
learning_rate = 5e-3

x_one_hot = np.array([np.eye(input_size)[x] for x in x_data])
pprint.pprint(x_one_hot)
y_data = [sample_idx[1:]]

# input/output tensor: (batch, seq, feature)
X = torch.FloatTensor(x_one_hot)
Y = torch.LongTensor(y_data)
pprint.pprint(X)
pprint.pprint(Y)

rnn = torch.nn.RNN(input_size, hidden_size, batch_first=True)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(rnn.parameters(), learning_rate)

for i in range(500):
    optimizer.zero_grad()
    outputs, status = rnn(X)
    loss = criterion(outputs.view(-1, input_size), Y.view(-1))
    loss.backward()
    optimizer.step()
    result = outputs.data.numpy().argmax(axis=2)
    result_str = ''.join([char_set[i] for i in np.squeeze(result)])
    print(f'i loss: {loss.item()} \nprediction: \n{result}, \ntrue Y: \n{y_data}, \npredicted str: {result_str}')

