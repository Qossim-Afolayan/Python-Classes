class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        rank_with_pairs = {
            rank: rank_count 
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == 2
        }

        if len(rank_with_pairs) == 2:
            return "Two Pair"
        
        if len(rank_with_pairs) == 1:
            return "Pair"
        return "High Card"

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1

        return card_rank_counts