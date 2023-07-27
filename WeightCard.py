from Card import Card


class WeightCard(Card):
    def __init__(self, coordinates, image_id, weight, is_closed=True):
        super().__init__(coordinates, image_id, is_closed=is_closed)
        self.weight = weight

    def get_weight(self):
        return self.weight
