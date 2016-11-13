from math import ceil


class ResourceMarket(object):

    def __init__(self):
        self.resource_counts = {
            'COAL': 24,
            'OIL': 24,
            'GARBAGE': 24,
            'URANIUM': 12,
        }

    def price_resources(self, resource_type, count):
        if resource_type not in ('OIL', 'COAL', 'GARBAGE', 'URANIUM'):
            raise Exception('Tried to purchase resources of an unknown type')

        current_count = self.resource_counts[resource_type]
        total_price = 0
        if resource_type in ('OIL', 'COAL', 'GARBAGE'):
            for i in range(count):
                total_price += (9 - ceil(current_count / 3))
                current_count -= 1
        elif resource_type == 'URANIUM':
            uranium_remaining_prices = {
                12: 16, 11: 14, 10: 12, 9: 10, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4,
                3: 3, 2: 2, 1: 1}
            for i in range(count):
                total_price += uranium_remaining_prices[current_count]
                current_count -= 1

        return total_price

    def purchase_resources(self, player, resource_type, count):
        if self.resource_counts[resource_type] < count:
            return 'Insufficient resources'
        if player.balance < self.price_resources(resource_type, count):
            return 'Insufficient funds'
        player.balance -= self.price_resources(resource_type, count)
        self.resource_counts[resource_type] -= count
        player.grant_resources(resource_type, count)


class PlantMarket(object):

    def __init__(self):
        self.actual_set = []
        self.future_set = []


if __name__ == '__main__':
    pass
