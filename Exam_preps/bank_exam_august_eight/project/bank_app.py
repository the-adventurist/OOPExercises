from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from project.clients.base_client import BaseClient

class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity  # the capacity of clients the Bank can have
        self.loans: List [BaseLoan] = []  # loans - objects that are created
        self.clients = []  # clients - objects that are created

    valid_types_of_loans = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    valid_client_types = {
        "Student": Student,
        "Adult": Adult
    }

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.valid_types_of_loans:
            raise Exception("Invalid loan type!")

        new_loan = BankApp.valid_types_of_loans[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.valid_client_types:
            raise Exception("Invalid client type!")

        if self.capacity - len(self.clients) == 0:
            return "Not enough bank capacity."

        new_client = BankApp.valid_client_types[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = [c for c in self.clients if c.client_id == client_id]

        if current_client[0].__class__.__name__ == "Student" and loan_type == "StudentLoan":
            given_loan = [l for l in self.loans if l.__class__.__name__ == "StudentLoan"]
            given_loan = given_loan[0]
            self.loans.remove(given_loan)
            current_client[0].loans.append(given_loan)

        elif current_client[0].__class__.__name__ == "Adult" and loan_type == "MortgageLoan":
            given_loan = [l for l in self.loans if l.__class__.__name__ == "MortgageLoan"]
            given_loan = given_loan[0]
            self.loans.remove(given_loan)
            current_client[0].loans.append(given_loan)
        else:
            raise Exception("Inappropriate loan type!")

        return f"Successfully granted {loan_type} to {current_client[0].name} with ID {client_id}."

    def remove_client(self, client_id: str):
        this_client = [c for c in self.clients if c.client_id == client_id]
        if not this_client:
            raise Exception("No such client!")

        has_loans = [l for l in this_client[0].loans]
        if not has_loans:
            self.clients.remove(this_client[0])

        return f"Successfully removed {this_client[0].name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        increased_rate_loans = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                increased_rate_loans += 1
                l.increase_interest_rate()

        return f"Successfully changed {increased_rate_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        increased_interests_client_rates = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                increased_interests_client_rates += 1

        return f"Number of clients affected: {increased_interests_client_rates}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_clients_income = 0
        for client in self.clients:
            total_clients_income += client.income

        available_loads = len(self.loans)
        total_sum = 0
        for l in self.loans:
            total_sum += l.amount

        average_cl_interest = 0
        for cl in self.clients:


            return f"Active Clients: {active_clients}" + "\n"\
                                                     f"Total Income: {total_clients_income}" + "\n"\
                                                     f"Granted Loans: {0}, Total Sum: {0}" + "\n"\
                                                f"Available Loans: {available_loads}, Total Sum: {0}" + "\n"\
                                                    f"Average Client Interest Rate: {0}"
