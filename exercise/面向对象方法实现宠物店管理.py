# class Animal(object):
#     def __init__(self, name):
#         self.__name = name

#     def speak(self):
#         print("I am an animal.")

# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.__species = 'Dog'

#     def speak(self):
#         print("I am a Dog.")

#     def play(self):
#         print("Dog {NAME} is playing.".format(NAME=self._Animal__name))

# class Cat(Animal):
#     def __init__(self, name):
#         super(Cat, self).__init__(name)
#         self.__species = 'Cat'

#     def speak(self):
#         print("I am a Cat.")

#     def play(self):
#         print("Cat {NAME} is playing.".format(NAME=self._Animal__name))

# class PetShop(object):
#     def __init__(self):
#         self.pets = []

#     def add_pet(self, pet):
#         self.pets.append(pet)

#     def show_pets(self):
#         for pet in self.pets:
#             print("{NAME} is {SPECIES}.".format(NAME=pet._Animal__name, SPECIES=pet._Dog__species if isinstance(pet, Dog) else pet._Cat__species))


# def testing_PetShop(pet_dict):
#     pet_shop = PetShop()
#     for species, name in pet_dict.items():
#         species = species.split("_")
#         if species[0] == "Dog":
#             dog = Dog(name)
#             dog.speak()
#             dog.play()
#             pet_shop.add_pet(dog)
#         elif species[0] == "Cat":
#             cat = Cat(name)
#             cat.speak()
#             cat.play()
#             pet_shop.add_pet(cat)
#         else:
#             print("Incorrect dict keys!")
#     pet_shop.show_pets()
# testing_PetShop({"Dog_1":"Tom", "Dog_2":"Bob", "Cat":"Lucy"})



class Animal(object):
    def __init__(self, name):
        self.__name = name

    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.__species = 'Dog'

    def speak(self):
        print("I am a Dog.")

    def play(self):
        print("Dog {} is playing.".format(self._Animal__name))

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.__species = 'Cat'

    def speak(self):
        print("I am a Cat.")

    def play(self):
        print("Cat {} is playing.".format(self._Animal__name))


class PetShop(object):
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def show_pets(self):
        for p in self.pets:
            print("{0} is {1}.".format(p._Animal__name,p._Dog__species if isinstance(p,Dog) else p._Cat__species))
            


def testing_PetShop(pet_dict):
    pet_shop = PetShop()
    for species, name in pet_dict.items():
        species = species.split("_")
        if species[0] == "Dog":
            dog = Dog(name)
            dog.speak()
            dog.play()
            pet_shop.add_pet(dog)
        elif species[0] == "Cat":
            cat = Cat(name)
            cat.speak()
            cat.play()
            pet_shop.add_pet(cat)
        else:
            print("Incorrect dict keys!")
    pet_shop.show_pets()
testing_PetShop({"Dog_1":"Tom", "Dog_2":"Bob", "Cat":"Lucy"})
