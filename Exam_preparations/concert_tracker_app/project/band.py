class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []  # musician objects of the band

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def add_member(self, musician_obj):
        self.members.append(musician_obj)

    def remove_member(self, musician_obj):
        self.members.remove(musician_obj)

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."