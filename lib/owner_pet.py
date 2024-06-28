class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner):
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        Pet.pet_type_check(pet_type)
        print("wooof")
    
    @classmethod
    def pet_type_check(cls,pet_type):
        for type in cls.PET_TYPES:
            if pet_type == type: 
                return pet_type
            else:  raise Exception("pet must be on list 'PET_TYPES'")

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,value):
        if not isinstance(value, Owner):
            raise TypeError()
    pass

class Owner:

    def __init__(self,name):
        self.name = name
        self.pet = Pet
        print("I am a God")
    def Pets(self):
        return Pet.PET_TYPES
    pass

Owner.pet