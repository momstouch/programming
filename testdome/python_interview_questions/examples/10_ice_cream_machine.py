class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        if not self.ingredients or not self.toppings:
            return []

        ret = []
        for ing in self.ingredients:
            for top in self.toppings:
                ret.append([ing, top])

        return ret

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    assert machine.scoops() == \
            [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
