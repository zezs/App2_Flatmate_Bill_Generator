# App2_Flatmate_Bill_Generator
Title: Flatmates Bill
-----------------------------------------------------------------------------------------------------------
Description: An app that takes
- I/p:
(i)   Total monthly rent amount
(ii)  Particular period: Month and year(to be sure of 30 or 31 days)
(iii) Name and days each flatmate resided in the house for that month

O/P:
(i)  Returns how much each flatmate has to pay(depending on number of days they resided)
(ii) It also generates Bill split in PDF format
------------------------------------------------------------------------------------------------------------
Listing Nouns from problem statement to design Oops(Class, objects and its attributes):
App, Bill, amount, period

<Initial Design> // Tentative

Bill -> Amount, Period
Flatmate -> Name, Days, Pay(days, totalBillForThatMonth)
PDFReport -> filename, generate(Bill, Flatmates1, Flatmates2, totalBillForThatMonth1, totalBillForThatMonth2 )
-------------------------------------------------------------------------------------------------------------
