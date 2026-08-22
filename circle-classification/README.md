## Project Title: Binary Classification with a Simple Neural Network

### Overview

The model classifies points from `sklearn.datasets.make_circles` — a synthetic dataset consisting of two concentric circles (10,000 points, with Gaussian noise) — predicting which circle (inner or outer) each point belongs to.

### Dataset

- **Source:** `sklearn.datasets.make_circles`
- **Samples:** 10,000
- **Features:** 2 (x, y coordinates)
- **Noise:** 0.05 standard deviation
- **Split:** 67% train / 33% test

### Model Architecture

A two-layer feedforward neural network:

| Layer | Type | In → Out | Activation |
|---|---|---|---|
| Layer 1 | `nn.Linear` | 2 → 10 | ReLU |
| Layer 2 | `nn.Linear` | 10 → 1 | Sigmoid |

- Layer 1 weights initialized with **Kaiming (He) uniform initialization**, matched to the ReLU activation that follows it.
- Sigmoid output layer paired with **Binary Cross-Entropy Loss (`BCELoss`)**, since the task is binary classification.

### Training Setup

- **Loss function:** `nn.BCELoss`
- **Optimizer:** SGD (`torch.optim.SGD`)
- **Learning rate:** 0.1
- **Batch size:** 64
- **Epochs:** 100

### Evaluation

The trained model is evaluated on the held-out test set:
- Predictions thresholded at 0.5 (probability ≥ 0.5 → class 1, else class 0)
- Overall accuracy computed

### How to Run

```bash
pip install torch numpy matplotlib scikit-learn 
python neural_network_circles.py
```

Running the script will:
1. Generate and visualize the train/test split (`samples.png`)
2. Train the model for 100 epochs
3. Evaluate on the test set and print accuracy report


### Key Takeaways

- How PyTorch's `nn.Module` and `__call__`/`forward` mechanism works under the hood
- Why activation functions and loss functions must be paired deliberately (sigmoid + BCELoss, softmax + CrossEntropyLoss)
- The difference between per-batch and per-epoch loss tracking
- Why `torch.no_grad()` matters during evaluation
- Choosing and justifying a classification threshold beyond the 0.5 default
