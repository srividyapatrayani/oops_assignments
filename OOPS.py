'''ecommerce  cart
class Cart:
    def __init__(self):
        self.items = {}
        self.price_detail = {"book": 10, "laptop": 30000}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_items(self):
        print(self.items)

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_only_items(self):
        items_list = []
        items_list = list(self.items.keys())
        print(items_list)

    def get_total_price(self):
        total_price = 0
        for item_name, quantity in self.items.items():
            total_price += self.price_detail[item_name] * quantity
        return total_price


cart_obj = Cart()
cart_obj.add_item("book", 10)
cart_obj.get_items()
cart_obj.add_item("laptop", 1)
cart_obj.get_items()
cart_obj.remove_item("book")
cart_obj.get_items()
cart_obj.update_quantity("laptop", 5)
cart_obj.get_items()
cart_obj.get_only_items()
print(cart_obj.get_total_price())'''

'''ecommerce using inheritence
class Product:
    def __init__(self, Name, Price, Deal_Price, Ratings):
        self.Name = Name
        self.Price = Price
        self.Deal_Price = Deal_Price
        self.Ratings = Ratings
        self.You_save = Price - Deal_Price

    def display_product_details(self):
        print("Name:{}".format(self.Name))
        print("Price:{}".format(self.Price))
        print("Deal_Price:{}".format(self.Deal_Price))
        print("You_save:{}".format(self.You_save))
        print("Ratings:{}".format(self.Ratings))


class electronic_item(Product):
    def set_waranty(self, waranty_in_months):
        self.waranty_in_months = waranty_in_months

    def get_waranty(self):
        print(self.waranty_in_months)


class grocerry_item(Product):
    def expery_date(self, date):
        self.date = date

    def get_expiry(self):
        print(self.date)


p = Product("Book", 10, 5, 5)
# p.display_product_details()
e_item = electronic_item("Camera", 25, 20, 4.5)
# e_item.display_product_details()
g_item = grocerry_item("flour", 300, 150, 4.5)
# g_item.display_product_details()
e_item.set_waranty(24)
e_item.get_waranty()
g_item.expery_date(36)
g_item.get_expiry()'''


'''class Product:

    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months


class GroceryItem(Product):
    pass


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill: {}".format(total_bill))


milk = GroceryItem("Milk", 40, 25, 3.5)
tv = ElectronicItem("TV", 45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(milk, 2)
order.add_item(tv, 1)
order.display_order_details()
order.display_total_bill()'''

class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_saved=price-deal_price
    def display_product_details(self):
        print("Product:{}".format(self.name))
        print("Price:{}".format(self.price))
        print("Deal Price:{}".format(self.deal_price))
        print("Ratings:{}".format(self.ratings))
        print("You saved:{}".format(self.you_saved))
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,ratings,warranty_in_months):
        super().__init__(name,price,deal_price,ratings)
        self.warranty_in_months=warranty_in_months
    def display_product_details(self):
        super().display_product_details()
        print("Wrranty: {}  months".format(self.warranty_in_months))
class GrocerryItem(Product):
    def __init__(self,name,price,deal_price,ratings,expiry_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date=expiry_date
    def display_product_details(self):
        super().display_product_details()
        print("Expired date: {}  months".format(self.expiry_date))
class Laptop(ElectronicItem):
    def __init__(self,name,price,deal_price,ratings,warranty_in_months,ram,storage):
        super().__init__(name,price,deal_price,ratings,warranty_in_months)
        self.ram=ram
        self.storage=storage
    def display_product_details(self):
        super().display_product_details()
        print("Ram:{}".format(self.ram))
        print("Storage:{}".format(self.storage))

class Order():
    delivery_charges={"Normal":0,"Prime Delivery":100}
    def __init__(self,delivery_method,delivery_address):
        self.items_in_cart=[]
        self.delivery_method=delivery_method
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        item=(product,quantity)
        self.items_in_cart.append(item)
    def display_order_details(self):
        print("Delivery Method:{}".format(self.delivery_method))
        print("Delivery address:{}".format(self.delivery_address))
        print("Products")
        print("----------------------------------")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity :{}".format(quantity))
            print(" ")
        print("----------------------------------")
        total_bill=self.get_total_bill()
        print("Total Bill: {}".format(total_bill))
    def get_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            total_bill=total_bill+product.get_deal_price()*quantity


        order_delivery_charges=Order.delivery_charges[self.delivery_method]
        total_bill=total_bill+order_delivery_charges
        return total_bill
    @classmethod
    def update_delivery_charges(cls,delivery_method,charges):
        cls.delivery_charges[delivery_method]=charges




flour=GrocerryItem("flour",40,30,4.5,"Jan 2022")
Tv=GrocerryItem("Tv",25000,15000,4.5,3)
my_order=Order("Normal","hyderabad")
my_order.add_item(Tv, 1)
my_order.add_item(flour, 3)
#my_order.display_order_details()
Order.update_delivery_charges("Normal",10)
#my_order.display_order_details()

lenovo_laptop=Laptop("Lenovo",45000,30000,4.5,24,"16 Gb","1 tb ssd")
lenovo_laptop.display_product_details()






































