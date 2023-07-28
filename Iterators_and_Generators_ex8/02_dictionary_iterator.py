class dictionary_iter():
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        for k, v in self.dictionary.items():
            del self.dictionary[k]
            if isinstance(k, str) and isinstance(v, str):
                return f"('{k}', '{v}')"
            elif isinstance(k, str):
                return f"('{k}', {v})"
            elif isinstance(v, str):
                return f"({k}, '{v}')"
            else:
                return f"({k}, {v})"
        else:
            raise StopIteration


result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
 print(x)


