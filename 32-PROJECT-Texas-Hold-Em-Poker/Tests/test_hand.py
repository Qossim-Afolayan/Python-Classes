import unittest
from Pocker.hand import Hand 
from Pocker.card import Card 

class HandTest(unittest.TestCase):
    def test_receive_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        eight_of_clubs = Card(rank = "8", suit = "Clubs")
        cards = [
            ace_of_spades,
            eight_of_clubs
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            [
                eight_of_clubs,
                ace_of_spades
            ]
        )
    
    def test_figures_out_no_card_is_best_rank(self):
        hand = Hand(cards = [])

        self.assertEqual(
            hand.best_rank(),
            "No Cards"
        )
    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "King", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "5", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
    def test_figures_out_straight_is_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_flush_is_best_rank(self):
        cards = [
            Card(rank = rank, suit = "Hearts")
            for rank in ["2", "5", "8", "10", "Ace"]
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "9", suit = "Spades"),
            Card(rank = "3", suit = "Diamonds"),
            Card(rank = "3", suit = "Spades")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "9", suit = "Spades"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "3", suit = "Spades")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a kind"
        )

    def test_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )

    