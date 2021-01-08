class Wagon:
    def __init__(self, _id):
        self.id = _id
        self.left = None
        self.right = None

class TrainComposition:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def attach_wagon_from_left(self, wagonId):
        new_wagon = Wagon(wagonId)

        if self.head:
            temp = self.head
            self.head = new_wagon

            self.head.right = temp
            temp.left = self.head
        else:
            self.head = new_wagon
            self.tail = new_wagon
    
    def attach_wagon_from_right(self, wagonId):
        new_wagon = Wagon(wagonId)

        if self.tail:
            temp = self.tail
            self.tail = new_wagon

            self.tail.left = temp
            temp.right = self.tail
        else:
            self.head = new_wagon
            self.tail = new_wagon

    def detach_wagon_from_left(self):
        if self.head:
            ret = self.head.id

            if self.head == self.tail:
                del self.head
                self.head = self.tail = None
            else:
                temp = self.head.right
                del self.head
                self.head = temp
                self.head.left = None

            return ret
        return None
    
    def detach_wagon_from_right(self):
        if self.tail:
            ret = self.tail.id

            if self.head == self.tail:
                del self.head
                self.head = self.tail = None
            else:
                temp = self.tail.left
                del self.tail
                self.tail = temp
                self.tail.right = None

            return ret
        return None

    def debug_print(self):
        ret = ""
        temp = self.head
        while temp:
            ret += "%d -> " % temp.id
            temp = temp.right
        return ret + "null"

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.debug_print())
    assert train.detach_wagon_from_right() == 7
    assert train.detach_wagon_from_left() == 13
    print(train.debug_print())
