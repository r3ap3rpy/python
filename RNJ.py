from collections import defaultdict
import os
from timeit import timeit

class InvalidPath(Exception):
    ...

class CharacterCounter:
    def __init__(self, bookpath):
        self._counts = defaultdict(int)
        if os.path.isfile(bookpath):
            self._bookpath = bookpath
        else:
            raise InvalidPath("The path you specified is invalid!")
    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]
    
    def process(self):
        with open(self._bookpath) as f:
            self.BookContent = f.read()
        
        for line in self.BookContent.split('\n'):
            if line:
                for character in line:
                    if character:
                        self.__call__(character)

    def __repr__(self):
        return str(sorted(self._counts.items(), key=lambda kv: kv[1]))

Worm = CharacterCounter(bookpath='RNJ.txt')
Worm.process()
print(Worm)
print(timeit(Worm.process,number=100))
