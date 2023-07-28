class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.initial_sequence = sequence
        self.number = number
        self.length_sequence = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        while self.number:

            try:
                letter = self.sequence[0]
                self.sequence = self.sequence[1:]
                self.number -= 1
                return f"{letter}"
            except IndexError:
                self.sequence = self.initial_sequence
        else:
            raise StopIteration


result = sequence_repeat('I Love Python', 3)
for item in result:
 print(item, end ='')

