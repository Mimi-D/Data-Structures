''' Simulation to test the time complexity for insertions into a hash table
implemented using nested lists and one using binary search trees
'''

# Importation of required modules
import time
import random
import numpy as np
import matplotlib.pyplot as plotter


# This class implements hashing using Overflow Chaining
class separate_chaining:

    # Initialization of hash table as a list of full capacity(509)
    def __init__(self):
        self.Maxsize = 509
        self.hash_table = [None for _ in range(self.Maxsize)]
        self.  Average_timeList = []
    # Function to generate random hash value from given range
    def hashValue(self):
        self.hash_val = random.randint(16384, 65535)
        return self.hash_val

    # Function to implement hash function. Double hashing is used.
    # Mid square hashing is first used then division hashing method
    def hash_function(self):

        # Value to be hashed is gotten from the hashValue function
        hash_val = self.hashValue()

        # Mid square hashing is implemented
        hash_key = str(hash_val ** 2)
        if len(hash_key) == 10:
            hash_key = int(hash_key[3:7])

        else:
            hash_key = int(hash_key[3:6])

        # Division hashing method is further implemented to reduce chances of collisions
        hash_key_final = hash_key % self.Maxsize
        return hash_key_final

    # This function inserts values to the hash table
    def insert_value(self):

        # The hash key is gotten from calling the hash_function
        key = self.hash_function()

        if self.hash_table[key] == None:
            self.hash_table[key] = []
            self.hash_table[key].append(self.hash_val)

        else:
            self.hash_table[key].append(self.hash_val)

    # This function prints the hash table
    def print_(self):
        print(self.hash_table)

    # This is the Timer function
    # This function takes the time for each insertion and accumulates it to find the average
    # The cumulative average time after every 1024th insertion is appended to the average time list
    def timer(self):
        total_time = 0

        # Initialize the average time list to an empty list

        # cumulative time

        for j in range(1024):
            start = time.perf_counter()
            self.insert_value()
            finish = time.perf_counter()
            time_taken = (finish - start) * 1000000000

            # Convert time to nanoseconds
            total_time = total_time + time_taken
        Average_time = total_time / 1024
        self.Average_timeList.append(Average_time)


    # Graphing function. This function graphs the cumulative time against the number of insertions
    def graph(self):

        # Average time list is collected

        yaxis = self.Average_timeList
        print("Time List consisting time for each 1024 insertions into Hash table implemented with linked lists:")
        # print average time list for user to see
        print(yaxis)

        # Using numpy array, Assign values to the x and y axis. The y axis values are given by the average times list
        x = np.array([1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192])
        y = np.array(yaxis)

        # Edit the graph interface to suit data entries
        plotter.plot(x, y, color='green', label='Hash table using linked list')
        plotter.title(" Graph of Average Insertion run time against Number of Insertions")
        plotter.xlabel("Number of insertions")
        plotter.ylabel("Average Insertion time in nanoseconds")
        plotter.legend(facecolor='grey')
        plotter.show()


# This class creates and inserts into Binary search trees which would serve as our buckets
class binarySearchTree:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # This is to format the Binary tree objects and allow them to be printed appropriately
    def __repr__(self):
        return "[%s, %s, %s]" % (self.left, str(self.value), self.right)

    # This is to check if a binary search tree does not exists with given parameters
    def not_exists(self):
        return self.left == self.right == self.value == None

    # This function inserts into the binary search tree
    def insert(self, value):
        if self.not_exists():
            self.value = value

        # The conditions of a binarySearchTree has to be obeyed,
        # the value at the left node must be less than that of the parent while the value at the right must be greater
        elif value < self.value:
            if self.left is None:
                self.left = binarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = binarySearchTree(value)
            else:
                self.right.insert(value)

# This class Implements Tree Structured Overflows

class binhash:

    #  Initialization of hash table as a list of full capacity(509)
    def __init__(self):
        self.Maxsize=20
        self.hash_table = [None for _ in range(self.Maxsize)]
        self.Average_timeList = []
    # This function provides a random hash value from given range
    def hashValue(self):
        self.hash_val = random.randint(16384, 65535)
        return self.hash_val

    # Function to implement hash function. Double hashing is used.
    # Mid square hashing is first used then division hashing method
    def hash_function(self):
        hash_val = self.hashValue()
        hash_key = str(hash_val ** 2)
        if len(hash_key) == 10:
            hash_key = int(hash_key[3:7])

        else:
            hash_key = int(hash_key[3:6])

        # Division hashing method is further implemented to reduce chances of collisions
        hash_key_final = hash_key % self.Maxsize
        return hash_key_final, hash_val

    # This function inserts hash value into binary search tree bucket
    def insertbucket(self):

        # Key and value are got from the hash function
        key, value = self.hash_function()

        # If there is no binary tree at the location to be hashed to, it creates a binary tree then hashes into it
        if self.hash_table[key] == None:
            newbucket = binarySearchTree(value)
            self.hash_table[key] = newbucket

        # If a binary tree is already present at the location, it inserts hash value into it
        else:
            self.hash_table[key].insert(value)

    # This function prints the hybrid hash table
    def print_(self):
        print(self.hash_table)

    # This is the Timer function
    # This function takes the time for each insertion and accumulates it to find the average
    # The cumulative average time after every 1024th insertion is appended to the average time list
    def timer(self):
        total_time = 0

        for j in range(1024):
            start = time.perf_counter()
            self.insertbucket()
            finish = time.perf_counter()

            # Convert time to nanoseconds
            time_taken = (finish - start) * 1000000000

            total_time = total_time + time_taken
        Average_time = total_time / 1024
        self.Average_timeList.append(Average_time)

    # Graphing function. This function graphs the cumulative time against the number of insertions
    def graph(self):
        # Average time list is collected from Timer function
        yaxis = self.Average_timeList
        print("Time List consisting time for each 1024 insertions into Hybrid hash table(BST):")
        # print average time list for user to see
        print(yaxis)

        # Using numpy array, Assign values to the x and y axis. The y axis values are given by the average times list
        x = np.array([1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192])
        y = np.array(yaxis)

        # Edit the graph interface to suit data entries
        plotter.plot(x, y, color='red', label='Hash table using BST')
        plotter.title(" Graph of Average Insertion run time against Number of Insertions")
        plotter.xlabel("Number of insertions")
        plotter.ylabel("Average Insertion time in nanoseconds")
        plotter.legend(facecolor='grey', title='Key')
        plotter.show()

# Driver code
''' case1 is an object, an instance of the 'separate_chaining' class which uses linked lists to resolve collision.
    The graph function is called which indirectly implements other functions such as timing and insertions.
    The graph is created for the user to see and the formed hash table is printed out.
    
    case2 is an object, an instance of the 'binhash' class which uses Binary Search Trees to resolve collision.
    The graph function is called which indirectly implements other functions such as timing and insertions.
    The graph is created for the user to see and the formed hash table is printed out.

'''
if __name__ == "__main__":
    # Create instance of separate chaining class

    case1 = separate_chaining()
    for i in range(8):
        case1.timer()

    # Print out hash table
    print("Hash table implemented using Linked lists:")
    case1.print_()
    print("")
    case1.graph()
    print("")
    # Create instance of binhash class
    case2 = binhash()
    for i in range(8):
        case2.timer()
    print("Hash table implemented using Binary Search Trees")
    # Print out hash tables
    case2.print_()
    print("")
    case2.graph()



