import torch 
import matplotlib.pyplot as plt 
import numpy as np 
import itertools 

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split 
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch import optim


# Creating Samples
X, y = make_circles(n_samples = 10000,
                    noise = 0.05,
                    random_state = 26
                    )

# Spliting Samples 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .33, random_state= 26)

# Plotting Training and Test Samples
fig, (train_ax, test_ax) = plt.subplots(ncols = 2, sharex = True, sharey = True, figsize = (10, 5))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c = y_train, cmap = plt.cm.Spectral)
train_ax.set_title("Training Samples")
train_ax.set_xlabel("Feature 0")
train_ax.set_ylabel("Feature 1")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c = y_test)
test_ax.set_title("Test Sample")
test_ax.set_xlabel("Feature 0")
test_ax.set_ylabel("Feature 1")

# Visualizing Train and Test Samples 
plt.savefig("samples.png")

class Data(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X.astype(np.float32))
        self.y = torch.from_numpy(y.astype(np.float32))
        self.len = self.X.shape[0]

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.len


batch_size = 64

train_data = Data(X_train, y_train)
train_dataloader = DataLoader(dataset = train_data, batch_size = batch_size, shuffle = True)

test_data = Data(X_test, y_test)
test_dataloader = DataLoader(dataset = test_data, batch_size = batch_size, shuffle = True)

# Create Network 
features = 2 
hidden_dim = 10 
output_dim = 1 

class NeuralNetwork(nn.Module):
    def __init__(self, features, hidden_dim, output_dim):
        super(NeuralNetwork, self).__init__()
        self.layer_1 = nn.Linear(features, hidden_dim)
        nn.init.kaiming_uniform_(self.layer_1.weight, nonlinearity = "relu")
        self.layer_2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = nn.functional.relu(self.layer_1(x))
        x = nn.functional.sigmoid(self.layer_2(x))

        return x 

model = NeuralNetwork(features, hidden_dim, output_dim)
print

# Training  Model 
learning_rate = 0.1 
loss_fn = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), learning_rate)

num_epochs = 100
loss_values = []


for epoch in range(num_epochs):
    for _, (X, y) in enumerate(train_dataloader):
        optimizer.zero_grad()

        predictedValue = model(X)
        loss = loss_fn(predictedValue, y.unsqueeze(-1))
        loss_values.append(loss.item())
        loss.backward()
        optimizer.step()


step = range(len(loss_values))
fig, ax = plt.subplots(figsize=(8,5))
plt.plot(step, np.array(loss_values))
plt.title("Step-wise Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.savefig("loss.png")

test_instances = (torch.from_numpy(y_test.astype(np.float32))).shape[0]

y_pred = []
y_test = []
correct = 0
total = 0 

with torch.no_grad():
    for X, y in test_dataloader:
        outputs = model(X)
        predicted = np.where(outputs.numpy() < 0.5, 0, 1)
        predicted = list(itertools.chain(*predicted))
        y_pred.append(predicted)
        y_test.append(y.numpy())
        total += y.size(0)
        correct += (predicted == y.numpy()).sum().item()


model_accuracy = 100 * correct // total 

print(f'The accuracy of the network on {test_instances} instances is {model_accuracy}%')