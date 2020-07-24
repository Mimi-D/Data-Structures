import random

class Deck:
    Max = 20
    def __init__(self):
        self.deck= []


        self.front = -1
        self.back = -1

    def isFull(self):
        if (self.front == 0 and self.back == self.Max - 1) or (self.front == self.back + 1):
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False

    def add_to_front(self, num):
        if self.isFull():
            print( "The deque is full")
        else:
            if self.front == -1:
                self.front = 0
                self.back = 0
                self.deck[self.front] = num
            elif self.front == 0:
                self.front = self.Max - 1
                self.deck[self.front] = num
            else:
                self.front = self.front - 1
                self.deck[self.front]=num

    def add_to_back(self, num):
        if self.isFull():
            print( "The deque is full")
        else:
            if self.front == -1:
                self.front = 0
                self.back = 0
                self.deck[self.back] = num
            elif self.back == self.Max - 1:
                self.back = 0
                self.deck[self.back] = num
            else:
                self.back = self.back + 1
                self.deck[self.back]=num

    def remove_from_front(self):
        if self.isEmpty():
            print("The deque is Empty")
        else:
            if self.front == self.back:
                self.front = -1
                self.back = -1
            elif self.front == self.Max - 1:
                self.front = 0
            else:
                self.front = self.front + 1


    def remove_from_back(self):
        if self.isEmpty():
            print( "The deque is Empty")

        else:
            if self.front == self.back:
                self.front = -1
                self.back = -1

            elif self.back == 0:
                self.back = self.Max - 1
            else:
                self.back = self.back - 1

    def get_front(self):
        if self.isEmpty():
            print("The deque is Empty")
        else:
            print("The item at the front is: ",self.deck[self.front])

    def get_back(self):
        if self.isEmpty():
            print( "The deque is Empty")
        else:
            print("The item at the back is: ", self.deck[self.back])

    def new_size(self):
        self.deck.__sizeof__()

    def main1(self):
        for i in range(self.Max // 2):
            numm = random.randint(1, 100)
            self.deck.append(numm)
        for i in range(50):
            prob = random.random()
            num = random.randint(1, 100)
            if 0 <= prob <= 0.1:
                print("A value should be added to front")
                self.add_to_front(num)
            elif 0.1 <= prob <= 0.3:
                print("A number should be removed from front")
                self.remove_from_front()
            elif 0.3 <= prob <= 0.4:
                print("A number should be added to back")
                self.add_to_back(num)
            elif 0.4 <= prob <= 1:
                print("A number should be removed from back")
                self.remove_from_back()
            self.new_size()
            self.get_front()
            self.get_back()

    def main2(self):
        for i in range(self.Max // 2):
            numm = random.randint(1, 100)
            self.deck[i]=numm

        for i in range(50):
            prob = random.random()
            num = random.randint(1, 100)
            if 0 <= prob <= 0.1:
                print("A value should be added to front")
                self.add_to_front(num)
            elif 0.1 <= prob <= 0.7:
                print("A number should be removed from front")
                self.remove_from_front()
            elif 0.7 <= prob <= 0.8:
                print("A number should be added to back")
                self.add_to_back(num)
            elif 0.8 <= prob <= 1:
                print("A number should be removed from back")
                self.remove_from_back()
            self.new_size()
            self.get_front()
            self.get_back()

