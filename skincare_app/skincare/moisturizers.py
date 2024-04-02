class Moisturizer:
    def __init__(self,name,price,skin_type):
        self.name = name
        self.price = price
        self.skin_type = skin_type
    
    def to_display_info(self):
        print(f"Moisturizer: {self.name}, Price: {self.price}, Skin Type: {self.skin_type}" )
