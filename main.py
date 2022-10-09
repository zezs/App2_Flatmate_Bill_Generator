from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a Flatmate person with Name, Residing_days
    method to pay bill share
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, all_flatmate_days):
        weight = self.days_in_house / all_flatmate_days
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Create a pdf file that contains data about flatmates such as
    their name, amount to pay, period of the pill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


if __name__ == "__main__":

    bill_march2021 = Bill(amount=120, period="March 2021")
    john =  Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)
    alex = Flatmate(name="Alex", days_in_house=15)

    flatmates_list = list()
    flatmates_list.append(john)
    flatmates_list.append(marry)
    flatmates_list.append(alex)

    all_flatmate_days = 0

    for i in flatmates_list:
        print(i.days_in_house)
        all_flatmate_days += i.days_in_house


    print(john.name, "Pays:", john.pays(bill_march2021, all_flatmate_days))
    print(marry.name, "Pays:", marry.pays(bill_march2021, all_flatmate_days))