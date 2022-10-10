master_list = []


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
        master_list.append(self)

    def pays(self, bill, all_flatmate_days):
        weight = self.days_in_house / all_flatmate_days
        to_pay = bill.amount * weight
        return to_pay
