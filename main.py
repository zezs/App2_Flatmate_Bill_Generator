from fpdf import FPDF
import webbrowser
from flat import *


class PdfReport:
    """
    Create a pdf file that contains data about flatmates such as
    their name, amount to pay, period of the pill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, master_list, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=36, style='B')
        pdf.cell(w=546, h=60, txt="FLATMATES BILL", border=1, align="C", ln=1)  # align center // ln=1='\n'

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=546, h=60, txt="Period: " + bill.period, align="C", border=1, ln=1)

        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=182, h=60, txt="NAME ", align="C", border=1)
        pdf.cell(w=182, h=60, txt="DAYS RESIDED", align="C", border=1)
        pdf.cell(w=182, h=60, txt="AMOUNT DUE", align="C", border=1, ln=1)

        for l in master_list:
            pdf.cell(w=182, h=60, txt=l.name, align="C", border=1)
            pdf.cell(w=182, h=60, txt=str(l.days_in_house)+" days", align="C", border=1)
            pdf.cell(w=182, h=60, txt=str(round( l.pays(bill, all_flatmate_days),2))+" $", align="C", border=1, ln=1)

        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=546, h=60, txt="TOTAL: "+ str(bill.amount)+" $", align="C", border=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename) #File uri impliclty created by Windows(not by mac or linux)


if __name__ == "__main__":


    flatmates_list = list()
    all_flatmate_days = 0

    print(list_test)

    print("*******FlatMates Bill Share*******")
    rent_amount = int(input ("Enter the rent for the month: "))
    rent_period = input("Enter the month and year: ")

    bill = Bill(rent_amount, rent_period)

    no_of_flatmates = int(input("Enter the number of residence: "))

    for i in range(0, no_of_flatmates):
        print("\n*** Enter details for Flatmate " + str(i + 1) + " ***")
        name = input("Enter the name:")
        days = int(input("Enter number of days resided in the house:"))
        Flatmate(name, days)


    for obj in master_list:
        all_flatmate_days += obj.days_in_house

    # file_name = input("\nSave as filename(include .pdf): ")
    pdf = PdfReport("bill.pdf")
    pdf.generate(master_list, bill)




    # bill_march2021 = Bill(amount=120, period="March 2021")
    # john =  Flatmate(name="John", days_in_house=20)
    # marry = Flatmate(name="Marry", days_in_house=25)
    # alex = Flatmate(name="Alex", days_in_house=15)
    # jenny =Flatmate(name="Jenny", days_in_house=5)

    # flatmates_list = list()
    # flatmates_list.append(john)
    # flatmates_list.append(marry)
    # flatmates_list.append(alex)
    # flatmates_list.append(jenny)

    # print(john.name, "Pays:", john.pays(bill_march2021, all_flatmate_days))
    # print(marry.name, "Pays:", marry.pays(bill_march2021, all_flatmate_days))

    #
    # if no_of_flatmates == 2:
    #     for i in range(0, no_of_flatmates):
    #         print("\n*** Enter details for Flatmate "+ str(i+1) + " ***")
    #         name = input("Enter the name:")
    #         days = int(input("Enter number of days resided in the house:"))
    #         x = [name, days]
    #         master_list.append(x)
    #
    #     #print(master_list)
    #     #print(master_list[0][0])
    #
    #     flat_mate1 = Flatmate(master_list[0][0], master_list[0][1])
    #     flat_mate2 = Flatmate(master_list[1][0], master_list[1][1])
    #     flatmates_list.append(flat_mate1)
    #     flatmates_list.append(flat_mate2)
    #
    # elif no_of_flatmates == 3:
    #     for i in range(0, no_of_flatmates):
    #         print("\n*** Enter details for Flatmate " + str(i+1) + " ***")
    #         name = input("Enter the name:")
    #         days = int(input("Enter number of days resided in the house:"))
    #         x = [name, days]
    #         master_list.append(x)
    #
    #     flat_mate1 = Flatmate(master_list[0][0], master_list[0][1])
    #     flat_mate2 = Flatmate(master_list[1][0], master_list[1][1])
    #     flat_mate3 = Flatmate(master_list[2][0], master_list[2][1])
    #     flatmates_list.append(flat_mate1)
    #     flatmates_list.append(flat_mate2)
    #     flatmates_list.append(flat_mate3)
    #
    # elif no_of_flatmates == 4:
    #     for i in range(0, no_of_flatmates):
    #         print("\n*** Enter details for Flatmate " + str(i+1)+" ***")
    #         name = input("Enter the name:")
    #         days = int(input("Enter number of days resided in the house:"))
    #         x = [name, days]
    #         master_list.append(x)
    #
    #     flat_mate1 = Flatmate(master_list[0][0], master_list[0][1])
    #     flat_mate2 = Flatmate(master_list[1][0], master_list[1][1])
    #     flat_mate3 = Flatmate(master_list[2][0], master_list[2][1])
    #     flat_mate4 = Flatmate(master_list[3][0], master_list[3][1])
    #     flatmates_list.append(flat_mate1)
    #     flatmates_list.append(flat_mate2)
    #     flatmates_list.append(flat_mate3)
    #     flatmates_list.append(flat_mate4)
    #
    # elif no_of_flatmates == 5:
    #     for i in range(0, no_of_flatmates):
    #         print("\n*** Enter details for Flatmate " + str(i+1) + " ***")
    #         name = input("Enter the name:")
    #         days = int(input("Enter number of days resided in the house:"))
    #         x = [name, days]
    #         master_list.append(x)
    #
    #     flat_mate1 = Flatmate(master_list[0][0], master_list[0][1])
    #     flat_mate2 = Flatmate(master_list[1][0], master_list[1][1])
    #     flat_mate3 = Flatmate(master_list[2][0], master_list[2][1])
    #     flat_mate4 = Flatmate(master_list[3][0], master_list[3][1])
    #     flat_mate5 = Flatmate(master_list[4][0], master_list[4][1])
    #     flatmates_list.append(flat_mate1)
    #     flatmates_list.append(flat_mate2)
    #     flatmates_list.append(flat_mate3)
    #     flatmates_list.append(flat_mate4)
    #     flatmates_list.append(flat_mate5)
    #
    # else:
    #     print("Maximum 5 flatmates only!")
    #
    #
    # for i in flatmates_list:
    #     all_flatmate_days += i.days_in_house


