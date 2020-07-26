# DUKE MIRIAM
# DATA STRUCTURE ASSIGNMENT 2

import random


class Deck:
    Max = 20

    def __init__(self):

        # Initialize the queue to be full of 'None' to it's maximum capacity
        self.deck = [None] * self.Max

        # Make the deque half full by replacing 'None' with random integers
        for i in range(self.Max // 2):
            numm = random.randint(1, 100)
            self.deck[i] = numm

        # Intitalize the front and back
        self.front = 0
        self.back = 9

        # Print the Initial Deque
        print("Initially Deque is: ", end="")
        print(self.printDeck())

    # Check if the deque is full
    def isFull(self):
        if (self.front == 0 and self.back == self.Max - 1) or (self.front == self.back + 1):
            return True
        else:
            return False

    # Check if the deque is empty
    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False

    # Add an element to the front of the deque
    def add_to_front(self, num):
        # Check if Deque is full
        if self.isFull():
            print("The deque is full")
        else:
            print("The deque is not full")
            # conditions to add element at the front if deque not full
            if self.front == -1:
                self.front = 0
                self.back = 0
                self.deck[self.front] = num
            elif self.front == 0:
                self.front = self.Max - 1
                self.deck[self.front] = num
            else:
                self.front = self.front - 1
                self.deck[self.front] = num

    def add_to_back(self, num):
        # Check if Deque is full
        if self.isFull():
            print("The deque is full")

        # conditions to add element at the back if deque not full
        else:
            print("The deque is not full")
            if self.front == -1:
                self.front = 0
                self.back = 0
                self.deck[self.back] = num
            elif self.back == self.Max - 1:
                self.back = 0
                self.deck[self.back] = num
            else:
                self.back = self.back + 1
                self.deck[self.back] = num

    def remove_from_front(self):
        # Check if deque empty
        if self.isEmpty():
            print("The deque is Empty")

        # Items removed are replaced with None, front and back are given new values
        else:
            if self.front == self.back:
                self.deck[self.front] = None
                self.front = -1
                self.back = -1
            elif self.front == self.Max - 1:
                self.deck[self.front] = None
                self.front = 0
            else:
                self.deck[self.front] = None
                self.front = self.front + 1

    def remove_from_back(self):
        # Check if deque empty
        if self.isEmpty():
            print("The deque is Empty")

        # Items removed are replaced with None, front and back are given new values
        else:
            if self.front == self.back:
                self.deck[self.front] = None
                self.front = -1
                self.back = -1

            elif self.back == 0:
                self.deck[self.back] = None
                self.back = self.Max - 1
            else:
                self.deck[self.back] = None
                self.back = self.back - 1

    # Function to get the front value
    def get_front(self):
        if self.isEmpty():
            print("The deque is Empty")
        else:
            print("The item at the front is: ", self.deck[self.front])

    # Function to get the back value
    def get_back(self):
        if self.isEmpty():
            print("The deque is Empty")
        else:
            print("The item at the back is: ", self.deck[self.back])

    # Function to get the new size
    def new_size(self):
        length = 0
        for i in self.deck:
            if i is not None:
                length = length + 1
        print(length)

    # Function to Print deque
    def printDeck(self):
        print("[", end="")
        for i in range(self.Max):
            if self.deck[i] is not None:
                print((self.deck[i]), end=" ")
        print("]", end="")
        return ""

    # Main function to run first row of probability
    def main1(self):
        # These variables would be used to analyse the statistics
        # of how many additions and removals would be made
        prob_add_front = 0
        prob_add_back = 0
        prob_remove_front = 0
        prob_remove_back = 0

        for i in range(50):
            # Generate random numbers for the probability decisions, and additions to front and back
            prob = random.random()
            num = random.randint(1, 100)

            # Probability decision conditions
            if 0 <= prob <= 0.1:
                print("A value should be added to front")
                self.add_to_front(num)
                prob_add_front = prob_add_front + 1
            elif 0.1 <= prob <= 0.3:
                print("A number should be removed from front")
                self.remove_from_front()
                prob_remove_front = prob_remove_front + 1
            elif 0.3 <= prob <= 0.4:
                print("A number should be added to back")
                self.add_to_back(num)
                prob_add_back = prob_add_back + 1
            elif 0.4 <= prob <= 1:
                print("A number should be removed from back")
                self.remove_from_back()
                prob_remove_back = prob_remove_back + 1

            # Get the front, back, new size of deque and print the deque
            self.get_front()
            self.get_back()
            print("The new size is:", end="")
            self.new_size()
            print("The new Deque is: ", end="")
            self.printDeck()
            print("\n")

        # statistics to analyse the simulation
        print("Statistic for this simulation")
        print("For this simluation Probability of adding to front was: ", prob_add_front / 50)
        print("For this simluation Probability of adding to back was: ", prob_add_back / 50)
        print("For this simluation Probability of removing from front was: ", prob_remove_front / 50)
        print("For this simluation Probability of removing from back was: ", prob_remove_back / 50)

    # Main function to run second row of probability
    def main2(self):
        # These variables would be used to analyse the statistics
        # of how many additions and removals would be made
        prob_add_front = 0
        prob_add_back = 0
        prob_remove_front = 0
        prob_remove_back = 0

        for i in range(50):
            # Generate random numbers for the probability decisions, and additions to front and back
            prob = random.random()
            num = random.randint(1, 100)

            # Probability decision conditions
            if 0 <= prob <= 0.1:
                print("A value should be added to front")
                self.add_to_front(num)
                prob_add_front = prob_add_front + 1
            elif 0.1 <= prob <= 0.7:
                print("A number should be removed from front")
                self.remove_from_front()
                prob_remove_front = prob_remove_front + 1
            elif 0.7 <= prob <= 0.8:
                print("A number should be added to back")
                self.add_to_back(num)
                prob_add_back = prob_add_back + 1
            elif 0.8 <= prob <= 1:
                print("A number should be removed from back")
                self.remove_from_back()
                prob_remove_back = prob_remove_back + 1

            # Get the front, back, new size of deque and print the deque
            self.get_front()
            self.get_back()
            print("The new size is:", end="")
            self.new_size()
            print("The new Deque is: ", end="")
            self.printDeck()
            print("\n")
        print("Statistic for this simulation")
        print("For this simluation Probability of adding to front was: ", prob_add_front / 50)
        print("For this simluation Probability of adding to back was: ", prob_add_back / 50)
        print("For this simluation Probability of removing from front was: ", prob_remove_front / 50)
        print("For this simluation Probability of removing from back was: ", prob_remove_back / 50)
