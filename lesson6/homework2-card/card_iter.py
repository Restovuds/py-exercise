class CardIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration