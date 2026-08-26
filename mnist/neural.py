import torch 
import numpy as np
import matplotlib.pyplot as plt 
import torchvision.datasets as datasets
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import nn
from torch import optim


# CREATE TRAIN AND TEST SAMPLES 
mnist_train = datasets.MNIST(root='./data', train = True, download = True, transform = transforms.ToTensor())
mnist_test = datasets.MNIST(root = './data', train = False, download = True, transform = transforms.ToTensor())

# LOAD TRAIN AND TEST SAMPLES WITH DATALOADER
batch_size = 128 

mnist_traindataloader = DataLoader(dataset = mnist_train, batch_size = batch_size, shuffle = True)
mnist_testdataloader = DataLoader(dataset = mnist_test, batch_size = batch_size, shuffle = False)

# CREATE NEURAL NETWORK
in_features = 784 
hidden_states = 128
output = 10 

class NeuralNetwork(nn.Module):
    def __init__(self, in_features, hidden_states, output):
        super().__init__()
        self.flatten = nn.Flatten()
        self.layer_1 = nn.Linear(in_features, hidden_states)
        nn.init.kaiming_uniform_(self.layer_1.weight, nonlinearity = 'relu')
        self.layer_2 = nn.Linear(hidden_states, output)

    def forward(self, x):
        x = self.flatten(x)
        x = nn.functional.relu(self.layer_1(x))
        x = self.layer_2(x)

        return x 


model = NeuralNetwork(in_features, hidden_states, output)

# TRAINING MODEL 
learning_rate = 0.01
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), learning_rate)

num_epochs = 10
loss_values = []

for epoch in range(num_epochs):
    for tensor, label in mnist_traindataloader:
        optimizer.zero_grad()

        predicted = model(tensor)
        loss = loss_fn(predicted, label)
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()


step = range(len(loss_values))
fig, ax = plt.subplots(figsize=(8,5))
plt.plot(step, np.array(loss_values))
plt.title("Step-wise Loss")
plt.xlabel("Training Steps")
plt.ylabel("Loss")

plt.savefig("loss.png")
 

test_instances = len(mnist_test)

# TESTING MODEL 

num_pred = []
num_target = []
correct = 0 
total = 0 



