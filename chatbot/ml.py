ml = [
    (
        r"(?:what is|explain) (?:machine learning|ml)[?.! ]*",
          "Machine learning learns patterns from data to make predictions or decisions on new inputs."
    ),
    (
        r"(?:what is|explain) supervised learning[?.! ]*", 
          "Supervised learning trains on examples that include both features and known target labels."
    ),
    (
        r"(?:what is|explain) unsupervised learning[?.! ]*", 
           "Unsupervised learning looks for structure in unlabeled data, such as clusters."
    ),
    (
        r"(?:what is|explain) reinforcement learning[?.! ]*", 
           "Reinforcement learning trains an agent through actions, rewards, and interaction with an environment."
    ),
    (
        r"(?:what is|explain) (?:a )?feature[?.! ]*", 
            "A feature is an input variable used by a model to make a prediction."
    ),
    (
        r"(?:what is|explain) (?:a )?label[?.! ]*", 
            "A label is the known output or target associated with a training example."
    ),
    (
        r"(?:what is|explain) classification[?.! ]*", 
            "Classification predicts a discrete category, such as spam or not spam."
    ),
    (
        r"(?:what is|explain) regression[?.! ]*", 
           "Regression predicts a continuous value, such as a price or temperature."
    ),
    (
        r"(?:what is|explain) overfitting[?.! ]*", 
           "Overfitting happens when a model learns training details too closely and performs poorly on unseen data."
    ),
    (
        r"(?:what is|explain) underfitting[?.! ]*", 
          "Underfitting happens when a model is too simple or insufficiently trained to capture useful patterns."
    ),
    (
        r"(?:what is|explain) data leakage[?.! ]*", 
           "Data leakage occurs when training uses information unavailable at prediction time, making evaluation misleading."
    ),
    (
        r"(?:what is|explain) (?:a )?train(?:ing)?[ /-]test split[?.! ]*", 
           "A train-test split reserves some data for evaluation after the model has been trained on the rest."
    ),
    (
        r"(?:what is|explain) (?:a )?validation set[?.! ]*", 
           "A validation set helps tune model choices without using the final test set."
    ),
    (
        r"(?:what is|explain) cross[ -]?validation[?.! ]*", 
           "Cross-validation rotates validation across folds to estimate performance more reliably."
    ),
    (
        r"(?:what is|explain) accuracy[?.! ]*", 
           "Accuracy is the fraction of all predictions that are correct; it can hide poor performance on a rare class."
    ),
    (
        r"(?:what is|explain) precision[?.! ]*", 
           "Precision is true positives divided by all predicted positives; it measures how often positive predictions are right."
    ),
    (
        r"(?:what is|explain) recall[?.! ]*", 
           "Recall is true positives divided by all actual positives; it measures how many positives were found."
    ),
    (
        r"(?:what is|explain) f1(?: score)?[?.! ]*", 
           "F1 is the harmonic mean of precision and recall; it balances the two measures."
    ),
    (
        r"(?:what is|explain) (?:a )?confusion matrix[?.! ]*", 
            "A confusion matrix counts true positives, false positives, true negatives, and false negatives."
    ),
    (
        r"(?:what is|explain) (?:a )?baseline(?: model)?[?.! ]*", 
           "A baseline is a simple reference result that a more complex model should improve upon."
    ),
    (
        r"(?:what is|explain) regularization[?.! ]*", 
          "Regularization discourages overly complex models, often improving generalization."
    ),
    (
        r"(?:what is|explain) (?:a )?hyperparameter[?.! ]*", 
          "A hyperparameter is set before training, such as learning rate or tree depth."
    ),
    (
        r"(?:what is|explain) (?:the )?learning rate[?.! ]*", 
           "The learning rate controls the size of each parameter update during optimization."
    ),
    (
        r"(?:what is|explain) (?:an )?epoch[?.! ]*", 
            "An epoch is one pass through the training dataset."
    ),
    (
        r"(?:what is|explain) (?:a )?batch[?.! ]*", 
           "A batch is a subset of training examples processed together in one update."
    ),
    (
        r"(?:what is|explain) (?:a )?loss function[?.! ]*", 
            "A loss function measures prediction error and provides a signal for model training."
    ),
    (
        r"(?:what is|explain) gradient descent[?.! ]*", 
            "Gradient descent adjusts parameters in the direction that reduces the loss."
    ),
    (
        r"(?:what is|explain) (?:a )?neural network[?.! ]*", 
            "A neural network combines trainable layers and nonlinear functions to learn representations."
    ),
    (
        r"(?:what is|explain) (?:an )?activation function[?.! ]*", 
            "An activation function adds nonlinearity, allowing a neural network to model complex relationships."
    ),
    (
        r"(?:what is|explain) (?:a )?embedding[?.! ]*", 
            "An embedding represents an item, such as a word or document, as a vector of numbers."
    ),
    (
        r"(?:what is|explain) (?:a )?vectorizer[?.! ]*", 
            "A vectorizer converts text into numeric features a model can process."
    ),
    (
        r"(?:what is|explain) (?:a )?countvectorizer[?.! ]*", 
            "CountVectorizer builds a vocabulary and represents documents by token counts."
    ),
    (
        r"(?:what is|explain) tf[ -]?idf[?.! ]*", 
            "TF-IDF weights words by their frequency in a document and their rarity across documents."
    ),
    (
        r"(?:what is|explain) naive bayes[?.! ]*", 
            "Naive Bayes is a probabilistic classifier that assumes features are conditionally independent given the class."
    ),
    (
        r"(?:what is|explain) (?:model )?drift[?.! ]*", 
            "Model drift describes performance changes as real-world data or its relationship to labels changes."
    ),
    (
        r"(?:what is|explain) (?:a )?model registry[?.! ]*", 
            "A model registry tracks model versions, metadata, and promotion to production."
    ),
]
