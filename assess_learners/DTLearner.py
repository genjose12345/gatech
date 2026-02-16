import numpy as np

class DTLearner:
    def __init__(self, leaf_size, verbose = False):
        self.leaf_size = leaf_size
        self.verbose = verbose

    def add_evidence(self, X_train, Y_train):
        self.X_train = X_train 
        self.Y_train = Y_train
        self.tree = self.build_tree(X_train,Y_train)
    
    def build_tree(self, X_train,Y_train):
        if X_train.shape[0] <= self.leaf_size:
            return np.array([[-1,np.mean(Y_train),-1,-1]])
        if np.all(Y_train == Y_train[0]):
            return np.array([[-1,np.mean(Y_train),-1,-1]])
        else:
            #find best feature
            best_feature = self.find_best_feature(X_train,Y_train)
            SplitVal = np.median(X_train[:,best_feature])
            #check if the lefttree and righttree are empty
            if X_train[X_train[:,best_feature] <= SplitVal].shape[0] == 0:
                return np.array([[-1,np.mean(Y_train),-1,-1]])
            if X_train[X_train[:,best_feature] > SplitVal].shape[0] == 0:
                return np.array([[-1,np.mean(Y_train),-1,-1]])
            #build lefttree and righttree
            lefttree = self.build_tree(X_train[X_train[:,best_feature] <= SplitVal],Y_train[X_train[:,best_feature] <= SplitVal])
            righttree = self.build_tree(X_train[X_train[:,best_feature] > SplitVal],Y_train[X_train[:,best_feature] > SplitVal])
            #build root
            root = np.array([[best_feature,SplitVal,1,lefttree.shape[0]+1]])
            #stack root,lefttree and righttree
            return np.vstack((root,lefttree,righttree))

    def find_best_feature(self, X_train,Y_train):
        best_feature = 0
        best_score = 0
        for feature in range(X_train.shape[1]):
            if np.std(X_train[:, feature]) == 0:
                continue
            absolute_correlation = np.abs(np.corrcoef(X_train[:,feature],Y_train)[0,1])
            if not np.isnan(absolute_correlation) and absolute_correlation > best_score:
                best_score = absolute_correlation
                best_feature = feature
        return best_feature

    def query(self, X_test):
        """
        current_row[0] = feature index
        current_row[1] = split value
        current_row[2] = left tree index
        current_row[3] = right tree index
        """
        predictions = np.zeros(X_test.shape[0])
        for i in range(X_test.shape[0]):
            node_row = 0
            current_row = self.tree[node_row]
            while int(current_row[2]) != -1:
                if X_test[i, int(current_row[0])] <= current_row[1]:
                    node_row = node_row + int(current_row[2])
                else:
                    node_row = node_row + int(current_row[3])
                current_row = self.tree[node_row]
            predictions[i] = current_row[1]
        return predictions

    def author(self):
        return "jrodriguez412"

    def study_group(self):
        return "jrodriguez412"