import BagLearner as bl
import LinRegLearner as lrl
import numpy as np
class InsaneLearner:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.learners = []
        for i in range(20):
            self.learners.append(bl.BagLearner(learner=lrl.LinRegLearner,kwargs = {},boost = False, verbose=self.verbose,bags=20))
    def add_evidence(self, X_train, Y_train):
        for learner in self.learners:
            learner.add_evidence(X_train,Y_train)
    def query(self, X_test):
        predictions = np.zeros(X_test.shape[0])
        for learner in self.learners:
            predictions += learner.query(X_test)
        return predictions / 20
        
def author(self):
    return "jrodriguez412"
