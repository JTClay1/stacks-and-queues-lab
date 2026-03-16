import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print("Item added to queue")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"{removed} has been removed.")
            return removed
        else:
            print("Queue is empty, nothing to remove.")
            return None

    def peek(self):
        if not self.is_empty():
           print(f"Front of queue: {self.items[0]}")
           return self.items[0]
        else:
           print("Queue is empty. No front item")
           return None

    def is_empty(self):
        return len(self.items) == 0 

    def select_and_announce_winner(self):
        if not self.is_empty():
           winner_index = random.randint(0, len(self.items) - 1)
           winner = self.items[winner_index]
           print (f"Random winner is {winner}")

           for _ in range(winner_index + 1):
               self.dequeue()
               
           return winner
        else:
            print ("Queue is empty, winner cannot be chosen")
            return None
    

