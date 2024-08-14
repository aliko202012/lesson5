class Appliance:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
       
    def use(self):
        pass

    def repair(self):
        pass

class WashingMachine (Appliance):
    def turn_on(self):
        return "Стиральная машина включен"

    def use(self):
        return "Стиральная машина начала стирку"
    
    def turn_off(self):
        return "Стиральная машина выключен"
    
    def repair(self):
        return "Ремонт стиральной машины"
    
        

class Microwave (Appliance):
    def turn_on(self):
        return "Микроволновая печь включен"

    def use(self):
        return "Микроволновая печь разогревает еду"
    
    def turn_off(self):
        return "Микроволновая печь выключен"
    
    def repair(self):
        return "Ремонт микроволновой печи"
    
    
class Refrigerator (Appliance):
    def turn_on(self):
        return "Холодильник включен"

    def use(self):
        return "Холодильник охлаждает продукты"
    
    def turn_off(self):
        return "Холодильник выключен"
    
    def repair(self):
        return "Ремонт холодильника"
    
appliances = [WashingMachine(),Microwave(),Refrigerator()]

for appliance in appliances:
    print(appliance.turn_on())
    print(appliance.use())
    print(appliance.turn_off())
    print(appliance.repair())

