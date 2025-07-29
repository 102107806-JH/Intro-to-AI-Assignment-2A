class ListNode:
    def __init__(self, data):
        self._data = data
        self._next = None

    def data_getter(self):
        return self._data

    def next_getter(self):
        return self._next


    def next_setter(self, next):
        self._next = next




