"""Задание:
Создайте базовый класс Appliance (Бытовой прибор):
Определите методы turn_on() и turn_off() в этом классе. Оба метода должны быть пустыми (содержать pass).
Определите абстрактные методы use() и repair(), которые будут реализованы в наследниках.

Создайте три наследуемых класса, каждый из которых представляет разные бытовые приборы:
Класс WashingMachine (Стиральная машина):
Реализуйте методы use() и repair(). Метод use() должен выводить сообщение "Стиральная машина начала стирку", а метод repair() — "Ремонт стиральной машины".
Класс Microwave (Микроволновая печь):
Реализуйте методы use() и repair(). Метод use() должен выводить сообщение "Микроволновая печь разогревает еду", а метод repair() — "Ремонт микроволновой печи".
Класс Refrigerator (Холодильник):
Реализуйте методы use() и repair(). Метод use() должен выводить сообщение "Холодильник охлаждает продукты", а метод repair() — "Ремонт холодильника".

Напишите код, который создает экземпляры каждого класса:
Включите приборы, используйте их, выключите, а затем вызовите метод repair() для каждого из них.
Убедитесь, что выводятся корректные сообщения для каждого действия."""

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

