class Plant(object):

    def __init__(self, number, resource_type, resource_count, output):
        self.number = number
        self.resource_type = resource_type
        self.resource_count = resource_count
        self.output = output
        self.stored_resources = 0

    def __str__(self):
        return 'Plant: {number} ({count} {type}) -> {output} energy'.format(
            number=self.number,
            count=self.resource_count,
            type=self.resource_type,
            output=self.output)


class PlantSet(object):

    PLANTS = (
        (4, 'COAL', 2, 1),
        (8, 'COAL', 3, 2),
        (10, 'COAL', 2, 2),
        (15, 'COAL', 2, 3),
        (20, 'COAL', 3, 5),
        (25, 'COAL', 2, 5),
        (31, 'COAL', 3, 6),
        (36, 'COAL', 3, 7),
        (42, 'COAL', 2, 6),
        (3, 'OIL', 2, 1),
        (7, 'OIL', 3, 2),
        (9, 'OIL', 1, 1),
        (16, 'OIL', 2, 3),
        (26, 'OIL', 2, 5),
        (32, 'OIL', 3, 6),
        (35, 'OIL', 1, 5),
        (40, 'OIL', 2, 6),
        (5, 'OIL/COAL', 2, 1),
        (12, 'OIL/COAL', 2, 2),
        (21, 'OIL/COAL', 2, 4),
        (29, 'OIL/COAL', 1, 4),
        (46, 'OIL/COAL', 3, 7),
        (6, 'GARBAGE', 1, 1),
        (14, 'GARBAGE', 2, 2),
        (19, 'GARBAGE', 2, 3),
        (24, 'GARBAGE', 2, 4),
        (30, 'GARBAGE', 3, 6),
        (38, 'GARBAGE', 3, 7),
        (11, 'URANIUM', 1, 2),
        (17, 'URANIUM', 1, 2),
        (23, 'URANIUM', 1, 3),
        (28, 'URANIUM', 1, 4),
        (34, 'URANIUM', 1, 5),
        (39, 'URANIUM', 1, 6),
        (13, 'RENEWABLE', 0, 1),
        (18, 'RENEWABLE', 0, 2),
        (22, 'RENEWABLE', 0, 2),
        (27, 'RENEWABLE', 0, 3),
        (33, 'RENEWABLE', 0, 4),
        (37, 'RENEWABLE', 0, 4),
        (44, 'RENEWABLE', 0, 5),
        (50, 'RENEWABLE', 0, 6)
    )

    def __init__(self):
        self.plants = []
        self.init_plants()

    def init_plants(self):
        for p in self.PLANTS:
            self.plants.append(Plant(p[0], p[1], p[2], p[3]))
