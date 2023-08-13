from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_TO_REVERSE = 2.50

    def reserve(self, number_of_people: int):
        reservation_price = number_of_people * self.PRICE_TO_REVERSE
        self.price_for_reservation = reservation_price
        self.is_reserved = True

