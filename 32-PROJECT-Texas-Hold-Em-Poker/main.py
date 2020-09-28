from Pocker.card import Card 
from Pocker.deck import Deck

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import card1, card2