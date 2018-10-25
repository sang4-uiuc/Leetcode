class Set:
    def __init__(self, *args):
        self._dict = {}
        for arg in args:
            self.add(arg)

    def __repr__(self):
        import string
        elems = map(repr, self._dict.keys(  ))
        elems.sort(  )
        return "%s(%s)" % (self._ _class_ _._ _name_ _, string.join(elems, ', '))

    def extend(self, args):
        """ Add several items at once. """
        for arg in args:
            self.add(arg)

    def add(self, item):
        """ Add one item to the set. """
        self._dict[item] = item

    def remove(self, item):
        """ Remove an item from the set. """
        del self._dict[item]

    def contains(self, item):
        """ Check whether the set contains a certain item. """
        return self._dict.has_key(item)

    # High-performance membership test for Python 2.0 and later
    _ _contains_ _ = contains

    def _ _getitem_ _(self, index):
        """ Support the 'for item in set:' protocol. """
        return self._dict.keys(  )[index]

    def _ _iter_ _(self):
        """ Better support of 'for item in set:' via Python 2.2 iterators """
        return iter(self._dict.copy(  ))

    def _ _len_ _(self):
        """ Return the number of items in the set """
        return len(self._dict)

    def items(self):
        """ Return a list containing all items in sorted order, if possible """
        result = self._dict.keys(  )
        try: result.sort(  )
        except: pass
        return result

    def _ _copy_ _(self):
        return Set(self)