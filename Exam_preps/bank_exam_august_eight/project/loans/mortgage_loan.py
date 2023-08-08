from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    __INTEREST_RATE = 3.5
    __AMOUNT = 50000

    def __init__(self):
        super().__init__(interest_rate=MortgageLoan.__INTEREST_RATE, amount=MortgageLoan.__AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5

