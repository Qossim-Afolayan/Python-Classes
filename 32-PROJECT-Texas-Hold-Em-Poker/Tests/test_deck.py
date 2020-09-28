import unittest
from Pocker.card import Card
from Pocker.deck import Deck

class DeckTest(unittest.TestCase):
    def test_stores_no_card_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_collection(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )