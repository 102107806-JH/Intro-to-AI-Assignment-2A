class DestinationCostPair:
    def __init__(self, destination_id, cost):
        self._destination_id = destination_id  # The destination id #
        self._cost = cost  # The cost of traveling to the destination #

    @property
    def destination_id(self):
        return self._destination_id

    @property
    def cost(self):
        return self._cost