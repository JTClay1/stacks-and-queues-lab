import random

class Queue:
    def __init__(self):
        # this list is the actual queue storage
        self.items = []

    def enqueue(self, item):
        # add new item to the back of the queue
        self.items.append(item)
        print("Item added to queue")

    def dequeue(self):
        # queue = FIFO, so remove from the front, not the back
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"{removed} has been removed.")
            return removed
        else:
            print("Queue is empty, nothing to remove.")
            return None

    def peek(self):
        # just look at the front item without removing it
        if not self.is_empty():
           print(f"Front of queue: {self.items[0]}")
           return self.items[0]
        else:
           print("Queue is empty. No front item")
           return None

    def is_empty(self):
        # returns True when the queue has no items in it
        return len(self.items) == 0 

    def select_and_announce_winner(self):
        # can't choose a winner if the queue is empty
        if not self.is_empty():
           # choose a random position in the queue
           winner_index = random.randint(0, len(self.items) - 1)

           # save the winner before removing anyone
           winner = self.items[winner_index]
           print(f"Random winner is {winner}")

           # dequeue everybody up to and including the winner
           for _ in range(winner_index + 1):
               self.dequeue()
               
           return winner
        else:
            print("Queue is empty, winner cannot be chosen")
            return None
