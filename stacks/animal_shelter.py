""" implementing real world problem using stack """


class InvalidAnimalKind(Exception):
    pass


class AnimalShelter:
    def __init__(self):
        """
        When we write the __init__() method,
        we're going to initialize all the variables we need:
        a list representing the dogs queue,
        a list representing the cats queue,
        and the overall order, which we'll set to 0 to start.
        """
        self.dogs = []
        self.cats = []
        self.order = 0

    def add_animal(self, name: str, kind: str):
        """
        adding an animal to our shelter.
        Let's assume we know the animal's name and kind (since type is already a keyword in python) to start with,
        so these will be the method's parameters.
        Let's convert the kind to lower case for some basic mistake proofing.
        """
        kind = kind.lower()
        self.order += 1
        animal = {
            "name": name,
            "type": kind,
            "order": self.order
        }

        if kind == "cat":
            self.cats.append(animal)
        elif kind == "dog":
            self.dogs.append(animal)
        else:
            raise InvalidAnimalKind("Invalid animal type entered.")

    def __adopt_animal(self, animal_list: list) -> str:
        if len(animal_list) == 0:
            raise IndexError("Animal List empty")
        else:
            return animal_list.pop()

    def adopt_dog(self):
        return self.__adopt_animal(self.dogs)

    def adopt_cat(self):
        return self.__adopt_animal(self.cats)

    def adopt_any(self):
        if len(self.cats) == 0:
            return self.adopt_dog()
        elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
            return self.adopt_dog()
        else:
            return self.adopt_cat()


a = AnimalShelter()
a.add_animal("Pizzapie", "cat")
a.add_animal("Emmy", "Dog")
a.add_animal("Sushi", "Cat")
a.add_animal("Charmander", "Dog")
print(a.cats, a.dogs)

a.adopt_cat()
a.adopt_dog()
a.adopt_any()
print(a.cats, a.dogs)
