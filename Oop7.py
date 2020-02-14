# Multilevel inheritance
"""
class Dad:
    pass

class Son(Dad):
    pass

class Grandson(Son):
    pass
"""

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 25
    def is_Dance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 5
    def is_Dance(self):
        return f"Yes I dance very awesomely {self.dance} :" 

darry = Dad()
larry = Son()
harry = Grandson()

print(darry.basketball)
print(larry.dance)
print(harry.is_Dance())
print("From Son class :",harry.basketball)

# if not is son class then it will use "basketball" from Dad  class

########## Quiz

class Electonic_Device: 
    mobile = "Realme"
    Laptop = "Dell"
    Earbud = "noise"
    power_bank = "Xiomi"
    Tab = "Samsung"
    iphone = "11pro"
    led = "Samsung"

class Pocket_Gadgets(Electonic_Device):
    mobile = ['Realme','Oppo','Samsung','Xiomi','Redmi']
    Earbud = ['Noise','Bass','Neckband','Ipad']
    power_bank = ['Realme PowerBank','xi-Powerbandk']


class Mobile(Pocket_Gadgets):
    
    def all_mobile(self):
        print(f"{self.mobile}")


electronic = Electonic_Device()
pocket = Pocket_Gadgets()
mobile = Mobile()

mobile.all_mobile()