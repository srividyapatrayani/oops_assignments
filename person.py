class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

def  get_string(Person):

    return  "{} is {} years old".format(Person.name, Person.age)

if  __name__  ==  "__main__":
    john =  Person("john", 25)
    david =  Person("david", 30)
    print(get_string(john))
    print(get_string(david))

