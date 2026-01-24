""""""  		  	   		 		  			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
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
  		  	   		 		  			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 		  			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 		  			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 		  			  		 			     			  	 
"""  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
import numpy as np  		  	   		 		  			  		 			     			  	 
import matplotlib.pyplot as plt  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
def author():  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    :return: The GT username of the student  		  	   		 		  			  		 			     			  	 
    :rtype: str  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    return "tb34"  # replace tb34 with your Georgia Tech username.  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
def gtid():  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 		  			  		 			     			  	 
    :rtype: int  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    return 900897987  # replace with your GT ID number  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 		  			  		 			     			  	 
    :type win_prob: float  		  	   		 		  			  		 			     			  	 
    :return: The result of the spin.  		  	   		 		  			  		 			     			  	 
    :rtype: bool  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    result = False  		  	   		 		  			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 		  			  		 			     			  	 
        result = True  		  	   		 		  			  		 			     			  	 
    return result  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
  		  	   		 		  			  		 			     			  	 
def test_code():  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    Method to test your code  		  	   		 		  			  		 			     			  	 
    """  		  	   		 		  			  		 			     			  	 
    win_prob = 18/38  # set appropriately to the probability of a win  		  	   		 		  			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		 		  			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 		  			  		 			     			  	 
    # add your code here to implement the experiments
    experiment_1_figure_1(win_prob)
    experiment_1_figure_2_3(win_prob)
    # experiment_2_figure_4_5(win_prob)
    # all_winnings = np.zeros((10, 1001))
    
    # for episode in range(10):
    #     episode_winnings = 0
    #     winnings = np.zeros(1001)
    #     winnings[0] = 0
    #     i = 1
    #     while episode_winnings < 80 and i <= 1000:
    #         won = False
    #         bet_amount = 1
    #         while not won and i <= 1000:
    #             won = get_spin_result(win_prob)
    #             if won == True:
    #                 episode_winnings = episode_winnings + bet_amount
    #                 winnings[i] = episode_winnings
    #             else:
    #                 episode_winnings = episode_winnings - bet_amount
    #                 winnings[i] = episode_winnings
    #                 bet_amount = bet_amount * 2
    #             i = i + 1            
    #     winnings[i:1001] = episode_winnings
    #     all_winnings[episode,:] = winnings
    #     print("episode", episode, "winnings:", winnings, "spins:", i-1)
    # print("all winnings array:\n", all_winnings[:,1:11])

    # for episode in range(10):
    #     plt.plot(all_winnings[episode,0:301],label=f"Episode {episode+1}")
    # plt.xlim(0,300)
    # plt.ylim(-256,100)
    # plt.xlabel("Number of Spins")
    # plt.ylabel("Winnings ($)")
    # plt.title("Figure 1: 10 Episodes of Martingale Strategy")
    # plt.savefig("figure1.png")
    # plt.legend()
    # plt.show()


def experiment_1_figure_1(win_prob):			
    all_winnings = np.zeros((10, 1001))
    for episode in range(10):
        episode_winnings = 0
        winnings = np.zeros(1001)
        winnings[0] = 0
        i = 1
        while episode_winnings < 80 and i <= 1000:
            won = False
            bet_amount = 1
            while not won and i <= 1000:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                    winnings[i] = episode_winnings
                else:
                    episode_winnings = episode_winnings - bet_amount
                    winnings[i] = episode_winnings
                    bet_amount = bet_amount * 2
                i = i + 1            
        winnings[i:1001] = episode_winnings
        all_winnings[episode,:] = winnings
        print("episode", episode, "winnings:", winnings, "spins:", i-1)
    print("all winnings array:\n", all_winnings[:,1:11])

    for episode in range(10):
        plt.plot(all_winnings[episode,0:301],label=f"Episode {episode+1}")
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 1: 10 Episodes of Martingale Strategy")
    plt.legend(loc='lower right')
    plt.savefig("figure1.png")
    plt.show()  


def experiment_1_figure_2_3(win_prob):			
    all_winnings = np.zeros((1000, 1001))
    for episode in range(1000):
        episode_winnings = 0
        winnings = np.zeros(1001)
        winnings[0] = 0
        i = 1
        while episode_winnings < 80 and i <= 1000:
            won = False
            bet_amount = 1
            while not won and i <= 1000:
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                    winnings[i] = episode_winnings
                else:
                    episode_winnings = episode_winnings - bet_amount
                    winnings[i] = episode_winnings
                    bet_amount = bet_amount * 2
                i = i + 1            
        winnings[i:1001] = episode_winnings
        all_winnings[episode,:] = winnings
        print("episode", episode, "winnings:", winnings, "spins:", i-1)
    print("all winnings array:\n", all_winnings[:,1:11])

    """
    checking if eveyrthing is correct
    """
    print("one episode winnings:", all_winnings[0,:], "mean:", np.mean(all_winnings[0,:]), "std:", np.std(all_winnings[0,:], ddof=0))
    print("first episode std plus 1 std:", np.mean(all_winnings[0,:]) + np.std(all_winnings[0,:], ddof=0))
    print("first episode std minus 1 std:", np.mean(all_winnings[0,:]) - np.std(all_winnings[0,:], ddof=0))
    mean_values = np.mean(all_winnings, axis=0)
    std_values = np.std(all_winnings, axis=0, ddof=0)
    plus_std_values = mean_values + std_values
    minus_std_values = mean_values - std_values
    
    plt.plot(mean_values[0:301], label="Mean")
    plt.plot(plus_std_values[0:301], label="mean + std")
    plt.plot(minus_std_values[0:301], label="mean - std")
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 2: 1000 Episodes of Martingale Strategy")
    plt.legend(loc='lower right')
    plt.savefig("figure2.png")
    plt.show()

    print("one episode median:", np.median(all_winnings[0,:]))
    median_values = np.median(all_winnings, axis=0)
    plus_median_values = median_values + std_values
    minus_median_values = median_values - std_values
    plt.plot(median_values[0:301], label = "median")
    plt.plot(plus_median_values[0:301], label = "median + std")
    plt.plot(minus_median_values[0:301], label = "median - std")
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 3: 1000 Episodes of Martingale Strategy")
    plt.legend(loc='lower right')
    plt.savefig("figure3.png")
    plt.show()                                    

    """
    getting the answers for question 1
    """

def experiment_2_figure_4_5(win_prob):			
    all_winnings = np.zeros((1000, 1001))
    for episode in range(1000):
        episode_winnings = 0
        bankroll = 256
        winnings = np.zeros(1001)
        winnings[0] = 0
        i = 1
        while episode_winnings < 80 and i <= 1000 and episode_winnings > -256:
            won = False
            bet_amount = 1
            while not won and i <= 1000 and episode_winnings > -256:
                available_bankroll = bankroll + episode_winnings
                if available_bankroll <= 0:
                    episode_winnings = -256
                    break
                if bet_amount > available_bankroll:
                    bet_amount = available_bankroll
                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                    winnings[i] = episode_winnings
                else:
                    episode_winnings = episode_winnings - bet_amount
                    winnings[i] = episode_winnings
                    bet_amount = bet_amount * 2
                i = i + 1            
        winnings[i:1001] = episode_winnings
        all_winnings[episode,:] = winnings
        print("episode", episode, "winnings:", winnings, "spins:", i-1)
    print("all winnings array:\n", all_winnings[:,1:11])
    

    print("one episode winnings:", all_winnings[0,:], "mean:", np.mean(all_winnings[0,:]), "std:", np.std(all_winnings[0,:], ddof=0))
    print("first episode std plus 1 std:", np.mean(all_winnings[0,:]) + np.std(all_winnings[0,:], ddof=0))
    print("first episode std minus 1 std:", np.mean(all_winnings[0,:]) - np.std(all_winnings[0,:], ddof=0))
    mean_values = np.mean(all_winnings, axis=0)
    std_values = np.std(all_winnings, axis=0, ddof=0)
    plus_std_values = mean_values + std_values
    minus_std_values = mean_values - std_values
    
    plt.plot(mean_values[0:301], label="Mean")
    plt.plot(plus_std_values[0:301], label="mean + std")
    plt.plot(minus_std_values[0:301], label="mean - std")
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 4: 1000 Episodes of Martingale Strategy with $256 Bankroll Limit")
    plt.legend(loc='lower right')
    plt.savefig("figure4.png")
    plt.show()

    """
    checking if eveyrthing is correct
    """
    print("one episode median:", np.median(all_winnings[0,:]))
    median_values = np.median(all_winnings, axis=0)
    plus_median_values = median_values + std_values
    minus_median_values = median_values - std_values
    plt.plot(median_values[0:301], label = "median")
    plt.plot(plus_median_values[0:301], label = "median + std")
    plt.plot(minus_median_values[0:301], label = "median - std")
    plt.xlim(0,300)
    plt.ylim(-256,100) 
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.title("Figure 5: 1000 Episodes of Martingale Strategy with $256 Bankroll Limit")
    plt.legend(loc='lower right')
    plt.savefig("figure5.png")
    plt.show()


if __name__ == "__main__":  		  	   		 		  			  		 			     			  	 
    test_code()  		  	   		 		  			  		 			     			  	 
            