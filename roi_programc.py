class RentalProperty():
    def __init__(self):
        self.properties = {}
        self.rental_income = 0
        self.laundry_income = 0
        self.storage_income = 0
        self.misc_income = 0
        self.total_income = 0
        self.tax_exp = 0
        self.insurance_exp = 0
        self.utilities_exp = 0
        self.hoa_exp = 0
        self.lawn_snow_exp = 0
        self.vacancy_exp = 0
        self.repairs_exp = 0
        self.capex_exp = 0
        self.propmgmt_exp = 0
        self.mortgage_exp = 0
        self.total_expenses = 0
        self.monthly_cashflow = 0
        self.annual_cashflow = 0
        self.monthly_cashflow = 0
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.misc_invest = 0
        self.return_percent = 0
        self.total_investment = 0

    def name(self):
        print("")
        prop_name = input("Enter your property name or address: ")
        self.properties[prop_name] = {}

    def income(self):
        print("")
        print("Enter expected monthly income in each category:")
        print("")
        self.rental_income = int(input("Rental Income: $ "))
        self.laundry_income = int(input("Laundry Income: $ "))
        self.storage_income = int(input("Storage Income: $ "))
        self.misc_income = int(input("Miscellaneous Income: $ "))

        self.total_income = sum([self.rental_income, self.laundry_income, self.storage_income, self.misc_income])
        print("")
        print(f"Total expected income:      ${self.total_income}")
    
    def expenses(self):
        print("")
        print("Enter expected monthly expenses for each category:")
        print("")
        self.tax_exp = int(input("Taxes: $ "))
        self.insurance_exp = int(input("Insurance: $ "))
        self.utilities_exp = int(input("Utilities: $ "))
        self.hoa_exp = int(input("HOA: $ "))
        self.lawn_snow_exp = int(input("Lawn & Snow: $ "))
        self.vacancy_exp = int(input("Vacancy: $ "))
        self.repairs_exp = int(input("Repairs: $ "))
        self.capex_exp = int(input("Capital Expenses: $ "))
        self.propmgmt_exp = int(input("Property Management: $ "))
        self.mortgage_exp = int(input("Mortgage: $ "))

        self.total_expenses = sum([self.tax_exp, self.insurance_exp, self.utilities_exp, self.hoa_exp, self.lawn_snow_exp, self.vacancy_exp, self.repairs_exp, self.capex_exp, self.propmgmt_exp, self.mortgage_exp])
        print("")
        print(f"Total expected expenses:      ${self.total_expenses}")

    def cash_flow(self):
        self.monthly_cashflow = self.total_income - self.total_expenses
        self.annual_cashflow = self.monthly_cashflow * 12
        print("")
        print("Your expected cash flow is:")
        print(f"Monthly: $ {self.monthly_cashflow}")
        print(f"Annual: $ {self.annual_cashflow}")

    def total_invest_calc(self):
        print("")
        print("Enter expected investments for each category: ")
        print("")
        self.down_payment = int(input("Down Payment: $ "))
        self.closing_costs = int(input("Closing Costs: $ "))
        self.rehab_budget = int(input("Rehab Budget: $ "))
        self.misc_invest = int(input("Miscellaneous: $ "))

        self.total_investment = sum([self.down_payment, self.closing_costs, self.rehab_budget, self.misc_invest])
        print("")
        print(f"Total expected investment:      $ {self.total_investment}")

    
    def roi(self):
        self.return_percent = (self.annual_cashflow / self.total_investment) * 100
        print("")
        print(f"*********** Your Expected Cash on Cash Return on Investment is: {self.return_percent: .2f} % *************")
        print("")


class Main():

    def run(self):
        property = RentalProperty()

        print("")
        print("""
            Welcome to the Cash on Cash ROI Calculator. You can enter all your expected income, expenses, and investments 
            and you will receive calculations on your total cash flow and expected Cash on Cash Return on Investment to
            help you make a decision on whether a given property or set of properties is a good deal.
        """)
        while True:
            response = input("Enter 'q' to quit or 'n' to enter a new property: ")
            if response.lower() == 'n':
                property.income()
                property.expenses()
                property.cash_flow()
                property.total_invest_calc()
                property.roi()
            elif response.lower() == 'q':
                break
            else:
                print("Invalid response")
                continue

user1 = Main()

user1.run()