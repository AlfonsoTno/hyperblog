class ShoppingCart:
    

    def __init__(self) -> None:
        self.__products: List[Product] = []

    




    def empty(self) -> bool: 
        return len(self.__products) == 0
    

    def has_products(self):
        return not self.empty()
    
# modulo 3 clase 8