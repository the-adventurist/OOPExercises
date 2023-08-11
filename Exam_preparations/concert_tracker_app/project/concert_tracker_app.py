from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    ALL_MUSICIANS_NAMES = []
    ALL_BANDS_NAMES = []

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if name in self.ALL_MUSICIANS_NAMES:
            raise Exception(f"{name} is already a musician!")

        new_musician_obj = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.ALL_MUSICIANS_NAMES.append(name)
        self.musicians.append(new_musician_obj)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in self.ALL_BANDS_NAMES:
            raise Exception(f"{name} band is already created!")

        new_band_obj = Band(name)
        self.ALL_BANDS_NAMES.append(name)
        self.bands.append(new_band_obj)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        taken_from_concert_list = [c for c in self.concerts if c.place == place]
        if taken_from_concert_list:
            return f"{taken_from_concert_list[0].place} is already " \
                   f"registered for {taken_from_concert_list[0].genre} concert!"

        new_concert_obj = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert_obj)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self.ALL_MUSICIANS_NAMES:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in self.ALL_BANDS_NAMES:
            raise Exception(f"{band_name} isn't a band!")

        taken_musician_obj = self._get_obj_by_name(musician_name, self.musicians)
        band_obj_to_put_musician = self._get_obj_by_name(band_name, self.bands)
        band_obj_to_put_musician.members.append(taken_musician_obj)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.ALL_BANDS_NAMES:
            raise Exception(f"{band_name} isn't a band!")
        current_band = self._get_obj_by_name(band_name, self.bands)
        searched_musician_obj_list = [m for m in current_band.members if m.name == musician_name]
        if not searched_musician_obj_list:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        fired_musician = searched_musician_obj_list[0]
        current_band.members.remove(fired_musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band_obj = self._get_obj_by_name(band_name, self.bands)
        concert_obj = [c for c in self.concerts if c.place == concert_place][0]
        musicians_of_the_group = []
        for type_musician in self.VALID_MUSICIAN_TYPES:
            such_musician_obj_list = self._check_for_musician_type(band_obj, type_musician)
            if not such_musician_obj_list:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
            musician_obj = such_musician_obj_list[0]
            musicians_of_the_group.append(musician_obj)

        for concert_type in ["Rock", "Metal", "Jazz"]:
            this_concert = concert_obj if concert_obj.genre == concert_type else None
            if this_concert:
                if concert_type == "Rock":
                    for musician_ob in musicians_of_the_group:
                        if "play the drums with drumsticks" in musician_ob.POSSIBLE_SKILLS \
                                or "sing high pitch notes" in musician_ob.POSSIBLE_SKILLS \
                                or "play rock" in musician_ob.POSSIBLE_SKILLS:
                            pass
                        else:
                            raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif concert_type == "Metal":
                    for musician_ob in musicians_of_the_group:
                        if "play the drums with drumsticks" in musician_ob.POSSIBLE_SKILLS \
                                or "sing low pitch notes" in musician_ob.POSSIBLE_SKILLS \
                                or "play metal" in musician_ob.POSSIBLE_SKILLS:
                            pass
                        else:
                            raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif concert_type == "Jazz":
                    for musician_ob in musicians_of_the_group:
                        if "play the drums with drum brushes" in musician_ob.POSSIBLE_SKILLS \
                                or "sing high pitch notes and sing low pitch notes" in musician_ob.POSSIBLE_SKILLS \
                                or "play jazz" in musician_ob.POSSIBLE_SKILLS:
                            pass
                        else:
                            raise Exception(f"The {band_name} band is not ready to play at the concert!")






    # helper methods and tools

    def _get_obj_by_name(self, obj_name, collection): # gets only from existing object in the collection
        obj = [o for o in collection if o.name == obj_name][0]
        return obj

    def _check_for_musician_type(self, band_obj, needed_musician_type):
        searched_type_musician = [m for m in band_obj.members if m.__class__.__name__ == needed_musician_type]
        return searched_type_musician