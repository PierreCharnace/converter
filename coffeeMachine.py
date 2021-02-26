class CoffeeMachine:
    WATER_LEVEL = 120
    MILK_QUANTITY = 50

    def _start_machine(self):

        while self.WATER_LEVEL > 20 and self.MILK_QUANTITY > 10:
            return True

            if self.WATER_LEVEL < 20 or self.MILK_QUANTITY < 10:
                break
               
    def __boil_water(self):
        return "boiling..."
    #boils the water

    def __make_cream(self):
        return "Make cream"

    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVEL -= 20
            self.MILK_QUANTITY -= 10
            print(self.__boil_water())
            print(self.__make_cream())
            print("You'r coffee is ready.")
              
        elif self.WATER_LEVEL <= 20 :
            print("Please add water")
        elif self.MILK_QUANTITY <= 10 :
            print ("Please add milk")
       

machine = CoffeeMachine()
for i in range(0,2):
    machine.make_coffee()

#print("Make coffee: Public", machine.make_coffee())
#print("Start machine: Protected", machine._start_machine())
#print("Boile water: Private", machine._CoffeeMachine__boil_water())
#print("Make cream: Private",machine._CoffeeMachine__make_cream())