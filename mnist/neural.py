import torch 
import numpy 
import torchvision.datasets as datasets
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import nn


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

        return x 


model = NeuralNetwork(in_features, hidden_states, output)


