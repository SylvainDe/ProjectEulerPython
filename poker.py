#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :

"""Classes related to evaluations of poker hands."""
import collections


class Card:
    """Card object (value and suit)."""
    CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @classmethod
    def from_string(cls, card):
        value, suit = card
        return cls(value, suit)

    def __str__(self):
        return str(self.value) + self.suit

    def __repr__(self):
        return self.__class__.__name__ + "(" + self.value + ", " + self.suit + ")"

    def evaluate(self):
        return Card.CARD_VALUES[self.value]


class Hand:
    """Hand object (iterable of NB_CARDS cards)."""
    NB_CARDS = 5

    def __init__(self, cards):
        assert len(cards) == Hand.NB_CARDS
        self.cards = cards

    @classmethod
    def from_string(cls, string):
        cards = [Card.from_string(chunk) for chunk in string.split()]
        return cls(cards[:Hand.NB_CARDS]), cls(cards[Hand.NB_CARDS:])

    def __str__(self):
        return "-".join(str(c) for c in self.cards)

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.cards) + ")"

    def evaluate(self):
        """Return an arbitrarly formed tuple that can be used to
        sort hands using lexicographic order. First element is an
        integer describing the type of hand. Other values are added
        to be able to differentiate hands.
        Integers used:
        0 High Card: Highest value card.
        1 One Pair: Two cards of the same value.
        2 Two Pairs: Two different pairs.
        3 Three of a Kind: Three cards of the same value.
        4 Straight: All cards are consecutive values.
        5 Flush: All cards of the same suit.
        6 Full House: Three of a kind and a pair.
        7 Four of a Kind: Four cards of the same value.
        8 Straight Flush: All cards are consecutive values of same suit.
        8 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        """
        HIGH_CARD, ONE_PAIR, TWO_PAIRS, THREE_OF_A_KIND, STRAIGHT, FLUSH, \
            FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH = range(9)
        values = sorted((c.evaluate() for c in self.cards), reverse=True)
        (mc_val, mc_nb), (mc2_val, mc2_nb) = collections.Counter(values).most_common(2)
        assert mc_nb in (1, 2, 3, 4)
        assert mc2_nb in (1, 2)
        if mc_nb == 4:
            return (FOUR_OF_A_KIND, mc_val, values)
        elif mc_nb == 3:
            if mc2_nb == 2:
                return (FLUSH, mc_val, mc2_val, values)
            else:
                return (THREE_OF_A_KIND, mc_val, values)
        elif mc_nb == 2:
            if mc2_nb == 2:
                return (TWO_PAIRS, sorted((mc_val, mc2_val)), values)
            else:
                return (ONE_PAIR, mc_val, values)
        else:
            assert mc_nb == 1
            is_flush = len(set(c.suit for c in self.cards)) == 1
            delta = values[0] - values[-1]
            is_straight = delta == Hand.NB_CARDS - 1
            if is_straight:
                return (STRAIGHT_FLUSH if is_flush else STRAIGHT, values)
            else:
                return (FLUSH if is_flush else HIGH_CARD, values)

    def __gt__(self, other):  # Note: other magic methods should be defined as well
        return self.evaluate() > other.evaluate()
