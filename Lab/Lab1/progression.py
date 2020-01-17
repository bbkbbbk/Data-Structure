from math import sqrt

class Progression:
    def __init__(self, start = 0):
        self._current  = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class SquareRootProgression(Progression):
    def __init__(self, start = 65536):
        super().__init__(start)

    def _advance(self):
        self._current = sqrt(self._current)

p = Progression()
p.print_progression(10)
s = SquareRootProgression()
s.print_progression(10)
s2 = SquareRootProgression(1024)
s2.print_progression(10)