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
        result = self._check_obj_by_name(name, self.musicians)
        if result:
            raise Exception(f"{name} is already a musician!")
        new_musician_obj = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician_obj)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        result = self._check_obj_by_name(name, self.bands)
        if result:
            raise Exception(f"{name} band is already created!")
        new_band_obj = Band(name)
        self.bands.append(new_band_obj)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self._check_place(place, self.concerts)
        new_concert_obj = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert_obj)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        result = self._check_obj_by_name(musician_name, self.musicians)
        if not result:
            raise Exception(f"{musician_name} isn't a musician!")
        musician_obj = result[0]
        result2 = self._check_obj_by_name(band_name, self.bands)
        if not result2:
            raise Exception(f"{band_name} isn't a band!")
        band_obj = result2[0]
        band_obj.add_member(musician_obj)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        result1 = self._check_obj_by_name(band_name, self.bands)
        if not result1:
            raise Exception(f"{band_name} isn't a band!")
        band_obj = result1[0]
        result2 = self._check_obj_by_name(musician_name, band_obj.members)
        if not result2:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician_obj = result2[0]
        band_obj.remove_member(musician_obj)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._check_obj_by_name(band_name, self.bands)[0]
        concert = self.__find_concert_by_place(concert_place)
        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                    filter(
                        lambda x: x.__class__.__name__ == musician_type,
                        band.members
                    )
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        concert_profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {concert_profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    # helper methods and tools
    @staticmethod
    def _check_obj_by_name(name, collection):
        result = [o for o in collection if o.name == name]
        return result

    @staticmethod
    def _check_place(place, collection):
        concert = [c for c in collection if c.place == place]
        if concert:
            raise Exception(f"{place} is already registered for {concert[0].genre} concert!")

    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert
