#Quiz 12B

def pop(self):
    """Returns and removes the last item in the stack self
    Stack, object -> Object"""
    temp = self._itemlist[-1]
    del self._itemlist[-1]
    return temp
