from classes.abstracts import ABSDeck, ABSAcc
import random

class Card:
    def __init__(self, value, rank, suit):
        self.value = value
        self.rank = rank
        self.suit = suit
        self.isOpen = False

    def __str__(self):
        if self.isOpen:
            return "[" + self.suit + " " + self.rank + "]"
        else:
            return "[   ]"

    def __repr__(self):
        if self.isOpen:
            return "[" + self.suit + " " + self.rank + "]"
        else:
            return "[   ]"


class Deck(ABSDeck):

    def shuffle(self):
        random.shuffle(self.deck)

    def pickACard(self):
        pass

    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♠️", "♣️", "♥️", "♦️"]

    def __init__(self):
        self.deck = []
        for suit in Deck.SUITS:
            for i in range(13):
                self.deck.append(Card(Deck.VALUES[i], Deck.RANKS[i], suit))

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.deck)


class Account(ABSAcc):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def getBalance(self):
        return self.balance

    def setBalance(self, value):
        self.balance = value

    def __str__(self):
        return self.name + " has " + self.balance + "$"