class Inventory:
    def __init__(self, food, amount):
        self.__food = food
        self.__amount = amount
        self.__unit_price = 0
        self.__total_price = 0

    def PriceList(self):
        dict = {
        "Dry Cured Iberian Ham": 177.80,
        "Wagyu Steaks": 450.00,
        "Matsutake Mushrooms": 272.00,
        "Kopi Luwak Coffee": 306.50,
        "Moose Cheese": 487.20,
        "White Truffles": 3600.00,
        "Blue Fin Tuna": 3603.00,
        "Le Bonnotte Potatoes": 270.81
        }

        return dict.get(self.__food, 0)

    def calculate(self):
        self.__total_price = self.__amount *  self.PriceList()
        return self.__total_price
    
    def get_food(self):
        return self.__food

    def get_amount(self):
        return self.__amount

    def get_unit_price(self):
        return self.__unit_price

    def get_calculated_price(self):
        return self.__total_price

