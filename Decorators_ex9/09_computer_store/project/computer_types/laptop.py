from project.computer_types.computer import Computer


class Laptop(Computer):
    def __init__(self):
        ...
    __RAM = 64

    def configure_computer(self, processor: str, ram: int):
        processors = {
            "AMD Ryzen 9 5950 X": 900,
            "Intel Core i9 - 11900 H": 1050,
            "Apple M1 Pro": 1200
        }

        try:
            processor in processors
        except ValueError:
            raise f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!"

        if ram <= Laptop.__RAM and ram % 2 == 0:
            pass
        else:
            return f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!"

