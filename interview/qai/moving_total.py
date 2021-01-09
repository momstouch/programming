class MovingTotal:

    def __init__(self):
        self.totals = set()
        self.end2 = []

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        temp = self.end2 + numbers
        for i, n in enumerate(temp[:-2]):
            t = temp[i] + temp[i + 1] + temp[i + 2]
            self.totals.add(t)

        self.end2 = temp[-2:]

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in self.totals:
            return True
        else:
            return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
