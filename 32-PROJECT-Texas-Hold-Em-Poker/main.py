from Pocker.card import Card 
from Pocker.deck import Deck
from Pocker.hand import Hand 
from Pocker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])

player1 = Player(name = "Qossim", hand = hand1)
player2 = Player(name = "Gbolahan", hand = hand2)


# from main import deck, cards, hand1, hand2, player1, player2