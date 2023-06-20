class RentalProperty():
    def __init__(self):
        self.properties = {}      # creates empty dictionary that will store each property name/address as a key and the characteristics for that property within another dictionary that is the value
        self.prop_name = ""
        self.sub_dict = {}
        self.total_income = 0
        self.total_expenses = 0
        self.monthly_cashflow = 0
        self.annual_cashflow = 0
        self.monthly_cashflow = 0
        self.total_investment = 0
        self.return_percent = 0
        

    def name(self):
        print("")
        self.prop_name = input("Enter your property name or address: ")
        self.properties[self.prop_name] = {}             # creates an empty dictionary as the value for the key in the overall dictionary

    def income(self):
        print("")
        print("Enter expected monthly income in each category:")
        print("")
        rental_income = int(input("Rental Income: $ "))
        laundry_income = int(input("Laundry Income: $ "))
        storage_income = int(input("Storage Income: $ "))
        misc_income = int(input("Miscellaneous Income: $ "))

        self.total_income = sum([rental_income, laundry_income, storage_income, misc_income])
        self.properties[self.prop_name]["Income"] = self.total_income       # adding value income to dictionary for that property
        print("")
        print(f"Total expected income:      ${self.total_income}")
    
    def expenses(self):
        print("")
        print("Enter expected monthly expenses for each category:")
        print("")
        tax_exp = int(input("Taxes: $ "))
        insurance_exp = int(input("Insurance: $ "))
        utilities_exp = int(input("Utilities: $ "))
        hoa_exp = int(input("HOA: $ "))
        lawn_snow_exp = int(input("Lawn & Snow: $ "))
        vacancy_exp = int(input("Vacancy: $ "))
        repairs_exp = int(input("Repairs: $ "))
        capex_exp = int(input("Capital Expenses: $ "))
        propmgmt_exp = int(input("Property Management: $ "))
        mortgage_exp = int(input("Mortgage: $ "))

        self.total_expenses = sum([tax_exp, insurance_exp, utilities_exp, hoa_exp, lawn_snow_exp, vacancy_exp, repairs_exp, capex_exp, propmgmt_exp, mortgage_exp])
        self.properties[self.prop_name]["Expenses"] = self.total_expenses       # adding value expenses to dictionary for that property
        print("")
        print(f"Total expected expenses:      ${self.total_expenses}")

    def cash_flow(self):
        self.monthly_cashflow = self.total_income - self.total_expenses
        self.annual_cashflow = self.monthly_cashflow * 12

        self.properties[self.prop_name]["Monthly Cashflow"] = self.monthly_cashflow    # adding values for cash flows to dictionary for that property
        self.properties[self.prop_name]["Annual Cashflow"] = self.annual_cashflow

        print("")
        print("Your expected cash flow is:")
        print(f"Monthly: $ {self.monthly_cashflow}")
        print(f"Annual: $ {self.annual_cashflow}")

    def total_invest_calc(self):
        print("")
        print("Enter expected investments for each category: ")
        print("")
        down_payment = int(input("Down Payment: $ "))
        closing_costs = int(input("Closing Costs: $ "))
        rehab_budget = int(input("Rehab Budget: $ "))
        misc_invest = int(input("Miscellaneous: $ "))

        self.total_investment = sum([down_payment, closing_costs, rehab_budget, misc_invest])
        self.properties[self.prop_name]["Total Investment"] = self.total_investment         # adding total investment value to dictionary for the property
        print("")
        print(f"Total expected investment:      $ {self.total_investment}")

    
    def roi(self):
        self.return_percent = (self.annual_cashflow / self.total_investment) * 100
        self.properties[self.prop_name]["Return Percent"] = self.return_percent         # adding return percent to value to property name dictionary
        print("")
        print(f"*********** Your Expected Cash on Cash Return on Investment is: {self.return_percent: .2f} % *************")
        print("")

    def view(self):
        all_income = 0
        all_expenses = 0
        all_monthly_cf = 0
        all_annual_cf = 0
        all_invest = 0
        all_return = 0

        # lists out totals for each property
        print("")
        print("Here are the totals for each property:")
        print("")
        for x in self.properties:
            print(f"*** {x} ***")
            for char, amts in self.properties[x].items():
                if char == 'Return Percent':
                    print(f"{char}:      {amts: .2f} %")
                    print("")
                    all_return += amts                   # increments all the returns together
                else:
                    print(f"{char}:      $ {amts}")
                    if char == 'Income':
                        all_income += amts               # increments all the incomes together
                    elif char == 'Expenses':
                        all_expenses += amts               # increments all the expenses together
                    elif char == 'Monthly Cashflow': 
                        all_monthly_cf += amts             # increments all the montly cashflows together
                    elif char == 'Annual Cashflow':
                        all_annual_cf += amts              # increments all the annual cashflows together
                    else:
                        all_invest += amts                    # increments all the investments together

        print("")    
        print(f"Total Income:             $ {all_income}")
        print(f"Total Expenses:           $ {all_expenses}")
        print(f"Total Monthly Cashflow:   $ {all_monthly_cf}")
        print(f"Total Annual Cashflow:    $ {all_annual_cf}")
        print(f"Total Investment:         $ {all_invest}")
        print("")
        print(f"Average Cash on Cash Return for All Properties: {(all_return / len(self.properties)): .2f} %")
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
            response = input("Enter 'q' to quit or 'n' to enter a new property or 'v' to view totals: ")
            if response.lower() == 'n':
                property.name()
                property.income()
                property.expenses()
                property.cash_flow()
                property.total_invest_calc()
                property.roi()
            elif response.lower() == 'v':
                property.view()
            elif response.lower() == 'q':
                break
            else:
                print("Invalid response")
                continue

user1 = Main()

user1.run()