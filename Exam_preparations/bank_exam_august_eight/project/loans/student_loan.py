from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    __INTEREST_RATE = 1.5
    __AMOUNT = 2000

    def __init__(self):
        super().__init__(interest_rate=StudentLoan.__INTEREST_RATE, amount=StudentLoan.__AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2

