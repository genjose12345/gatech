""""""  		  	   		 		  			  		 			     			  	 
"""  		  	   		 		  			  		 			     			  	 
Test a learner.  (c) 2015 Tucker Balch  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 		  			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 		  			  		 			     			  	 
All Rights Reserved  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 		  			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 		  			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 		  			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 		  			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 		  			  		 			     			  	 
or edited.  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 		  			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 		  			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 		  			  		 			     			  	 
GT honor code violation.  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 		  			  		 			     			  	 
"""  		  	   		 		  			  		 			     			  	 
	  			  		 			     			  	 
import math  		  	   		 		  			  		 			     			  	 
import sys  		  	   		 		  			  		 			     			  	 
import matplotlib.pyplot as plt	   		 		  			  		 			     			  	 
import numpy as np  		  	   		 		  			  		 			     			  	 
import DTLearner as dt
import BagLearner as bl
import RTLearner as rt 
import time as time	  	   		 		  			  		 			     			  	 
import LinRegLearner as lrl  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
if __name__ == "__main__":  		  	   		 		  			  		 			     			  	 
    if len(sys.argv) != 2:  		  	   		 		  			  		 			     			  	 
        print("Usage: python testlearner.py <filename>")  		  	   		 		  			  		 			     			  	 
        sys.exit(1)  		  	   		 		  			  		 			     			  	 
    inf = open(sys.argv[1])  		  	   		 		  			  		 			     			  	 
    data = np.array(  		  	   		 		  			  		 			     			  	 
        [list(map(float, s.strip().split(",")[1:])) for s in inf.readlines()[1:]]  		  	   		 		  			  		 			     			  	 
    )  		  	   		 		  			  		 			     			  	 


    # compute how much of the data is training and testing  		  	   		 		  			  		 			     			  	 
    train_rows = int(0.6 * data.shape[0])  		  	   		 		  			  		 			     			  	 
    test_rows = data.shape[0] - train_rows  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
    # separate out training and testing data  		  	   		 		  			  		 			     			  	 
    train_x = data[:train_rows, 0:-1]  		  	   		 		  			  		 			     			  	 
    train_y = data[:train_rows, -1]  		  	   		 		  			  		 			     			  	 
    test_x = data[train_rows:, 0:-1]  		  	   		 		  			  		 			     			  	 
    test_y = data[train_rows:, -1]  

    """
    Research and discuss overfitting as observed in the experiment. (Use the dataset Istanbul.csv with DTLearner). 
    Support your assertion with graphs/charts. (Do not use bagging in Experiment 1). At a minimum, the following question(s)
    that must be answered in the discussion:  
    Does overfitting occur with respect to leaf_size?  
    For which values of leaf_size does overfitting occur? 
    Indicate the starting point (a.k.a., optimal hyperparameter setting) and the direction of overfitting
    (e.g., the range over which overfitting occurs beginning with the optimal hyperparameter setting). 
    Support your answer in the discussion or analysis. Use RMSE as your metric for assessing overfitting.
    Include a discussion of what overfitting is, why it occurs, why it is important, and how it is mitigated. 
    """
    root_mean_squared_error_in = []
    root_mean_squared_error_out = []
    # leaf_sizes = [1, 5, 10, 20, 5]
    for leaf_size in range(1, 51):
        learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
        learner.add_evidence(train_x,train_y)
        predictions_in = learner.query(train_x)
        predictions_out = learner.query(test_x)
        root_mean_squared_error_in.append(math.sqrt(((train_y - predictions_in) ** 2).sum() / train_y.shape[0]))
        root_mean_squared_error_out.append(math.sqrt(((test_y - predictions_out) ** 2).sum() / test_y.shape[0]))
    plt.plot(range(1, 51), root_mean_squared_error_in, label='In Sample')
    plt.plot(range(1, 51), root_mean_squared_error_out, label='Out Sample')
    plt.xlabel('Leaf Size')
    plt.ylabel('Root Mean Squared Error')
    plt.title('Root Mean Squared Error vs Leaf Size')
    plt.grid(True)
    plt.legend()
    plt.savefig("experiment_1_overfitting_leaf_size.png")
    plt.close()

    bag_sizes = [5, 10, 15, 20]
    for bag_size in bag_sizes:
        root_mean_squared_error_in = []
        root_mean_squared_error_out = []
        for i in range(1, 51):
            learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": i}, bags=bag_size, boost=False, verbose=False)
            learner.add_evidence(train_x,train_y)
            predictions_in = learner.query(train_x)
            predictions_out = learner.query(test_x)
            root_mean_squared_error_in.append(math.sqrt(((train_y - predictions_in) ** 2).sum() / train_y.shape[0]))
            root_mean_squared_error_out.append(math.sqrt(((test_y - predictions_out) ** 2).sum() / test_y.shape[0]))
        print(f"plotting {bag_size} bags")
        plt.plot(range(1, 51), root_mean_squared_error_in, label='In Sample')
        plt.plot(range(1, 51), root_mean_squared_error_out, label='Out Sample')
        plt.xlabel('Leaf Size')
        plt.ylabel('Root Mean Squared Error')
        plt.grid(True)
        plt.title(f'BagLearner ({bag_size} bags) DTLearner: RMSE and Leaf Size')
        plt.legend()
        plt.savefig(f"experiment_2_bagging_DTLearner_bags_{bag_size}.png")
        plt.close()

    time_DTLearner = []
    time_RTLearner = []
    for i in range(1, 51):
        start_time = time.time()
        learner = dt.DTLearner(leaf_size=i,verbose=False)
        learner.add_evidence(train_x,train_y)
        end_time = time.time()
        time_DTLearner.append(end_time - start_time)

    for i in range(1, 51):
        start_time = time.time()
        learner = rt.RTLearner(leaf_size=i,verbose=False)
        learner.add_evidence(train_x,train_y)
        end_time = time.time()
        time_RTLearner.append(end_time - start_time)
    plt.plot(range(1, 51), time_DTLearner, label='DTLearner')
    plt.plot(range(1, 51), time_RTLearner, label='RTLearner')
    plt.xlabel('Leaf Size')
    plt.ylabel('Time')
    plt.title('Time vs Leaf Size for DTLearner and RTLearner')
    plt.grid(True)
    plt.legend()
    plt.savefig("experiment_3_DTLearner_vs_RTLearner_time.png")
    plt.close()

    absolute_mean_squared_error_DTLearner = []
    absolute_mean_squared_error_RTLearner = []
    for i in range(1, 51):
        learner = dt.DTLearner(leaf_size=i,verbose=False)
        learner.add_evidence(train_x,train_y)   
        predictions_out = learner.query(test_x)
        absolute_mean_squared_error_DTLearner.append(np.mean(np.abs(test_y - predictions_out)))
    for i in range(1, 51):
        learner = rt.RTLearner(leaf_size=i,verbose=False)   
        learner.add_evidence(train_x,train_y)
        predictions_out = learner.query(test_x)
        absolute_mean_squared_error_RTLearner.append(np.mean(np.abs(test_y - predictions_out)))
    plt.plot(range(1, 51), absolute_mean_squared_error_DTLearner, label='DTLearner')
    plt.plot(range(1, 51), absolute_mean_squared_error_RTLearner, label='RTLearner')
    plt.xlabel('Leaf Size')
    plt.ylabel('Absolute Mean Squared Error')
    plt.title('Absolute Mean Squared Error vs Leaf Size for DTLearner and RTLearner')
    plt.grid(True)
    plt.legend()
    plt.savefig("experiment_3_DTLearner_vs_RTLearner_absolute_mean_squared_error.png")
    print("completed")
    # print(f"{test_x.shape}")  		  	   		 		  			  		 			     			  	 
    # print(f"{test_y.shape}")  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
    # create a learner and train it  		  	   		 		  			  		 			     			  	 
    learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner  		  	   		 		  			  		 			     			  	 
    learner.add_evidence(train_x, train_y)  # train it  		  	   		 		  			  		 			     			  	 
    # print(learner.author())  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
    # evaluate in sample  		  	   		 		  			  		 			     			  	 
    pred_y = learner.query(train_x)  # get the predictions  		  	   		 		  			  		 			     			  	 
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])  		  	   		 		  			  		 			     			  	 
    # print()  		  	   		 		  			  		 			     			  	 
    # print("In sample results")  		  	   		 		  			  		 			     			  	 
    # print(f"RMSE: {rmse}")  		  	   		 		  			  		 			     			  	 
    c = np.corrcoef(pred_y, y=train_y)  		  	   		 		  			  		 			     			  	 
    # print(f"corr: {c[0,1]}")  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
    # evaluate out of sample  		  	   		 		  			  		 			     			  	 
    pred_y = learner.query(test_x)  # get the predictions  		  	   		 		  			  		 			     			  	 
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])  		  	   		 		  			  		 			     			  	 
    # print()  		  	   		 		  			  		 			     			  	 
    # print("Out of sample results")  		  	   		 		  			  		 			     			  	 
    # print(f"RMSE: {rmse}")  		  	   		 		  			  		 			     			  	 
    c = np.corrcoef(pred_y, y=test_y)  		  	   		 		  			  		 			     			  	 
    # print(f"corr: {c[0,1]}")  		  	   	 		  			  		 			     			  	 
