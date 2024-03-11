class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None) -> None:
        if pet_type not in self.PET_TYPES:
            raise TypeError("Pet must be in PET TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

class Owner:
    def __init__(self, name) -> None:
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return [pet for pet in sorted_pets if pet.owner == self]

# Example usage:
# Creating instances of Owner and Pet
owner1 = Owner("John")
pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)

# Accessing pets through the Owner class methods
owner_pets = owner1.pets()
print([pet.name for pet in owner_pets])  # Output: ['Buddy', 'Whiskers']

# Adding a new pet to the owner
pet3 = Pet("Charlie", "bird")
owner1.add_pet(pet3)
print(pet3.owner)  # Output: <__main__.Owner object at ...>

# Getting sorted pets by name
sorted_pets = owner1.get_sorted_pets()
print([pet.name for pet in sorted_pets])  # Output: ['Buddy', 'Charlie', 'Whiskers']
