import unittest
from Pocker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card("2", "Club")
        self.assertEqual(card.suit, "Club")

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card("5", "Diamond")
        self.assertEqual(str(card), "5 of Diamond")

    def test_has_technical_representation(self):
        card = Card("5", "Diamond")
        self.assertEqual(repr(card), "Card('5', 'Diamond')")