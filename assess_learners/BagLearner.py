import numpy as np

class BagLearner:
    def __init__(self, learner, kwargs, bags,boost = False, verbose = False):
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        self.learners = []
        for i in range(self.bags):
            learner = self.learner(**self.kwargs)
            self.learners.append(learner)

    def add_evidence(self, X_train, Y_train):
        self.X_train = X_train 
        self.Y_train = Y_train
        for learner in self.learners:
            indices = np.random.randint(0,X_train.shape[0],size=X_train.shape[0])
            X_train_bag = X_train[indices]
            Y_train_bag = Y_train[indices]
            learner.add_evidence(X_train_bag,Y_train_bag)

    def query(self, X_test):
        predictions = np.zeros(X_test.shape[0])
        for learner in self.learners:
            predictions += learner.query(X_test)
        return predictions / self.bags

def author():
    return "jrodriguez412"

def study_group():

    return "jrodriguez412"