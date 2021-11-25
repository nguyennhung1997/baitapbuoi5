class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    @property
    def point(self):
        point = 0
        for card in self.cards:
            point += card.rank
        return point

    @property
    def biggest_card(self):
        return max(self.cards)

    def add_card(self, card):
        if len(self.cards) == 3:
            raise ValueError('Người chơi đã rút đủ bài')
        self.cards.append(card)

    def remove_card(self):
        self.cards = []

    def flip_card(self):
        return "{player} {cards} Điểm:{point} | Lá bài lớn nhất:{biggest_card}".format(
            **{'player': self.name,
               'cards': " ".join([str(card) for card in self.cards]),
               'point': self.point,
               'biggest_card': self.biggest_card})
