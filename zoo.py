class Animal:
    def __init__(self, age_in_months, required_food_in_kgs, breed):
        self.age_in_months = age_in_months
        self.required_food_in_kgs = required_food_in_kgs
        self.breed = breed
        if self.age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months:{}".format(self.age_in_months))



class Deer(Animal):

    def __init__(self, age_in_months, required_food_in_kgs, breed):
        super().__init__(age_in_months, required_food_in_kgs, breed)


    def grow(self):
            self.required_food_in_kgs += 2
            self.age_in_months += 1

    def make_sound(self):
        print("Buck Buck")

    def breathe(self):
        print("Breathe in air")


class Lion(Animal):
    def __init__(self, age_in_months, required_food_in_kgs, breed):
        super().__init__(age_in_months, required_food_in_kgs, breed)

    def grow(self):
            self.required_food_in_kgs += 4
            self.age_in_months += 1
    def make_sound(self):
        print("Roar Roar")

    def breathe(self):
        print("Breathe in air")

    def hunt(self, other):
        for i in other.animals_in_zoo:
            if i.__class__.__name__=="Deer":
                other.animals_in_zoo.remove(i)
                break
        else:
            print("No deers to hunt")





class Shark(Animal):
    def __init__(self, age_in_months, required_food_in_kgs, breed):
        super().__init__(age_in_months, required_food_in_kgs, breed)

    def grow(self):
            self.required_food_in_kgs += 8
            self.age_in_months += 1
    def make_sound(self):
        print("Shark Sound")

    def breathe(self):
        print("Breathe oxygen from water")


    def hunt(self, other):
            for i in other.animals_in_zoo:
                if i.__class__.__name__ == "GoldFish":
                    other.animals_in_zoo.remove(i)
            else:
                print("No fish to hunt")


class GoldFish(Animal):

    def __init__(self, age_in_months, required_food_in_kgs, breed):
        super().__init__(age_in_months, required_food_in_kgs, breed)

    def grow(self):
            self.required_food_in_kgs += 0.2
            self.age_in_months += 1


    def make_sound(self):
        print("Hum Hum")

    def breathe(self):
        print("Breathe oxygen from water")


class Snake(Animal):
    def __init__(self, age_in_months, required_food_in_kgs, breed):
        super().__init__(age_in_months, required_food_in_kgs, breed)
        self.animal="SNAKE"

    def grow(self):
            self.required_food_in_kgs += 0.5
            self.age_in_months += 1

    def make_sound(self):
        print("Hiss Hiss")

    def breathe(self):
        print("Breathe in air")


    def hunt(self, other):
        for i in other.animals_in_zoo:
            if i.__class__.__name__=="Deer":
                other.animals_in_zoo.remove(i)
        else:
            print("No deers to hunt")


class Zoo():
    count = 0

    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.count

    def __init__(self):
        self.animals_in_zoo = []
        self.reserved_food_in_kgs = 0

    def add_food_to_reserve(self, other):
        self.reserved_food_in_kgs += other
        return self.reserved_food_in_kgs

    def count_animals(self):
        p = len(self.animals_in_zoo)
        return p

    def add_animal(self, Animal):
        self.animals_in_zoo.append(Animal)
        type(self).count += 1
    @staticmethod
    def count_animals_in_given_zoos(other):
        count=0
        for i in other:
            for j in i.animals_in_zoo:
                count+=1
        return count


    def feed(self, other):
        self.other = other
        res = other.required_food_in_kgs
        other.grow()
        self.reserved_food_in_kgs -= res
zoo = Zoo()
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
zoo.count_animals()
nehru_zoological_park = Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
print(Zoo.count_animals_in_all_zoos())
print(Zoo.count_animals_in_given_zoos([zoo]))
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park)

