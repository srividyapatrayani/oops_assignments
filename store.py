class Store:
    def __init__(self):
        self.items = []

    def add_item(self, item):

        self.items.append(item)
        return self.items

    def count(self):
        print(len(self.items))

    def exclude(self, *queries):
        items = self.items
        for query in queries:
            exclude = []
            for i in self.items:
                if i not in self._filter(query,items):
                    exclude.append(i)

            new_store = Store()

            for item in exclude:
                new_store.add_item(item)
            return new_store
        #self.items=exclude

    def filter(self, *queries):
        items = self.items
        for query in queries:
            #print(query.value)
            for i in items:
                #print(i.name)
                items = self._filter(query, items)
        new_store1 = Store()
        for obj in items:
            new_store1.add_item(obj)
        #print(new_store1.items[0].name)
        return new_store1


    def _filter(self, query, items):
        cart = []
        for item in items:
            if query.operation == "EQ":
                a = self.eq(item, query)
                if a != None:

                    cart.append(self.eq(item, query))


            elif query.operation == "GT":
                if self.gt(item, query) != None:
                    cart.append(self.gt(item, query))

            elif query.operation == "LT":
                if self.lt(item, query) != None:
                    cart.append(self.lt(item, query))


            elif query.operation == "GTE":
                if self.gte(item, query) != None:
                    cart.append(self.gte(item, query))


            elif query.operation == "LTE":
                if self.lte(item, query) != None:
                    cart.append(self.lte(item, query))


            elif query.operation == "STARTS_WITH":
                if self.starts_with(item, query) != None:
                    cart.append(self.starts_with(item, query))


            elif query.operation == "ENDS_WITH":
                if self.ends_with(item, query) != None:
                    cart.append(self.ends_with(item, query))


            elif query.operation == "CONTAINS":
                if self.contains(item, query) != None:
                    cart.append(self.contains(item, query))


            elif query.operation == "IN":
                if self.in_cond(item, query) != None:
                    cart.append(self.in_cond(item, query))
            else:
                raise ValueError( "Invalid value for operation, got {}".format(query.operation)  )
        return cart


    def eq(self, item, query):

        # print(query)
        field = query.field
        if field == "name":
            if item.name == query.value:
                return item
        elif field == "category":
            if item.category == query.value:
                return item
        else:
            if item.price == query.value:
                return item

    def gt(self, item, query):
        if query.field == "price":
            if item.price > query.value:
                return item

    def gte(self, item, query):
        field = query.field
        if field == "price":
            if item.price >= query.value:
                return item

    def lt(self, item, query):
        if query.field == "price" and item.price < query.value:
            return item

    def lte(self, item, query):
        field = query.field
        if field == "price":
            if item.price <= query.value:
                return item

    def starts_with(self, item, query):
        field = query.field
        if field == "name":
            if (item.name).startswith(query.value):
                return item
        elif field == "category":
            if (item.category).startswith(query.value):
                return item

    def ends_with(self, item, query):
        field = query.field
        if field == "name":
            if (item.name).endswith(query.value):
                return item
        elif field == "category":
            if (item.category).endswith(query.value):
                return item

    def contains(self, item, query):
        field = query.field
        if field == "name":
            if query.value in item.name:
                return item
        elif field == "category":
            if query.value in item.category:
                return item

    def in_cond(self, item, query):
        field = query.field
        for i in query.value:
            if field == "name":
                if i == item.name:
                    return item
            elif field == "category":
                if i in item.category:
                    return item
            else:
                if i in item.category:
                    return item
    def __add__(self,other):
        store_1=Store()
        list1=self.items
        list_2=other.items
        list3 = list1 + list_2
        list_3=list(dict.fromkeys(list3))
        for item in list_3:
            store_1.add_item(item)
        return store_1







    def __repr__(self):
        res = ""

        for item_obj in self.items:
           #res=""
           res+="{}@{}-{}\n".format(item_obj.name, item_obj.price, item_obj.category)
        return res



class Item:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        '''if self.price > 0:
            print("{}@{}-{}".format(self.name, self.price, self.category))
        else:
            raise ValueError("Invalid value for price, got 0")'''


# item = Item(name="Oreo Biscuits", price=0, category="Food")
class Query:
    def __init__(self, field, operation, value):
        self.field = field
        self.operation = operation
        self.value = value
        #print("{} {} {}".format(self.field, self.operation, self.value))


store = Store()
item = Item(name="Oreo Biscuits", price=30, category="FOOD")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="FOOD")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="FOOD")
store.add_item(item)
item = Item(name="Cream", price=100, category="BEAUTY")
store.add_item(item)
item=Item(name="Cream",price=150,category="BEAUTY")
store.add_item(item)
item=Item(name="kajal ",price=50,category="BEAUTY")
store.add_item(item)
query = Query(field="price", operation="GT", value=15)
#print(results)
results = store.exclude(query) + store.exclude(query)
print(results)