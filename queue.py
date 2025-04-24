import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if self.is_empty():
            return None
        winner = random.choice(self.items)
        print(f"[Announcing Winner] {winner}")
        while self.items:
            removed = self.dequeue()
            print(f"[Dequeuing] {removed}")
            if removed == winner:
                break
        return winner
