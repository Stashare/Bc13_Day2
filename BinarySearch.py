""" binary search algorithm"""
class BinarySearch(list):
    """ BinarySearch class definition"""

    def __init__(self, length, step):
        """ Initialize list and auto generates items
        Arguments:
        self -- BinarySearch items
        length -- number of items in list - int
        step - interval between subsequent numbers in the list - int
        """
        list.__init__(self)
        list_gen = (n for n in range(step, (step * length) + 1, step))
        for item in list_gen:
            self.append(item)
        self.length = len(self)


    def search(self, item):
        """ returns a dictionary of the number of iterations and index
        Arguments:
        self -- list generated
        list2 -- one of 2 lists to be compared
        """
        length = self.length
        left = 0
        right = length - 1
        middle = (left + right) // 2
        count = 0

        while True:
            if self[middle] == item:
                break

            elif self[left] == item:
                middle = left
                break

            elif self[right] == item:
                middle = right
                break

            elif middle == left:
                middle = -1
                break

            elif self[middle] < item:
                left = middle + 1
                middle = (left + right) // 2

            elif self[middle] > item:
                right = middle - 1
                middle = (left + right) // 2
            else:
                pass
            count += 1
        return {"count":count, "index":middle}