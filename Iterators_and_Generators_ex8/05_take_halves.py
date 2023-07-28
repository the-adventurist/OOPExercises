def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():

        for i in integers():
            result = i / 2
            yield result

    def take(n, result):
        while n:
            yield result
            n -= 1

        return (take(n, result), halves, integers)



take = solution()[0]
halves = solution()[1]
print(take(5, halves()))