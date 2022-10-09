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

    def generate(self, flatmates_list, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=36, style='B')
        pdf.cell(w=546, h=60, txt="FLATMATES BILL", border=1, align="C", ln=1)  # align center // ln=1='\n'

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=546, h=60, txt="Period: " + bill_march2021.period, align="C", border=1, ln=1)

        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=182, h=60, txt="NAME ", align="C", border=1)
        pdf.cell(w=182, h=60, txt="DAYS RESIDED", align="C", border=1)
        pdf.cell(w=182, h=60, txt="AMOUNT DUE", align="C", border=1, ln=1)

        for l in flatmates_list:
            pdf.cell(w=182, h=60, txt=l.name, align="C", border=1)
            pdf.cell(w=182, h=60, txt=str(l.days_in_house)+" days", align="C", border=1)
            pdf.cell(w=182, h=60, txt=str(round( l.pays(bill, all_flatmate_days),2))+" $", align="C", border=1, ln=1)

        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=546, h=60, txt="TOTAL: "+ str(bill.amount)+" $", align="C", border=1)

        pdf.output("bill_main.pdf")


if __name__ == "__main__":

    bill_march2021 = Bill(amount=120, period="March 2021")
    john =  Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)
    alex = Flatmate(name="Alex", days_in_house=15)
    jenny =Flatmate(name="Jenny", days_in_house=5)

    flatmates_list = list()
    flatmates_list.append(john)
    flatmates_list.append(marry)
    flatmates_list.append(alex)
    flatmates_list.append(jenny)

    all_flatmate_days = 0

    for i in flatmates_list:
        print(i.days_in_house)
        all_flatmate_days += i.days_in_house


    print(john.name, "Pays:", john.pays(bill_march2021, all_flatmate_days))
    print(marry.name, "Pays:", marry.pays(bill_march2021, all_flatmate_days))

    pdf = PdfReport("bill")
    pdf.generate(flatmates_list, bill_march2021)