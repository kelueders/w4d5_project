class RentalProperty():
    def __init__(self):
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
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.misc_invest = 0

    def income(self):
        print("")
        print("Enter expected monthly income in each category:")
        print("")
        self.rental_income = int(input("Rental Income: "))
        self.laundry_income = int(input("Laundry Income: "))
        self.storage_income = int(input("Storage Income: "))
        self.misc_income = int(input("Miscellaneous Income: "))

        self.total_income = sum([self.rental_income, self.laundry_income, self.storage_income, self.misc_income])
        print("")
        print(f"Total expected income:      ${self.total_income}")

        return self.total_income
    
    def expenses(self):
        print("")
        print("Enter expected monthly expenses for each category:")
        print("")
        self.tax_exp = int(input("Taxes: "))
        self.insurance_exp = int(input("Insurance: "))
        self.utilities_exp = int(input("Utilities: "))
        self.hoa_exp = int(input("HOA: "))
        self.lawn_snow_exp = int(input("Lawn & Snow: "))
        self.vacancy_exp = int(input("Vacancy: "))
        self.repairs_exp = int(input("Repairs: "))
        self.capex_exp = int(input("Capital Expenses: "))
        self.propmgmt_exp = int(input("Property Management: "))
        self.mortgage_exp = int(input("Mortgage: "))

        self.total_expenses = sum([self.tax_exp, self.insurance_exp, self.utilities_exp, self.hoa_exp, self.lawn_snow_exp, self.vacancy_exp, self.repairs_exp, self.capex_exp, self.propmgmt_exp, self.mortgage_exp])
        print("")
        print(f"Total expected expenses:      ${self.total_expenses}")

        return self.total_expenses

    def cash_flow(self):
        monthly_cashflow = self.total_income - self.total_expenses
        annual_cashflow = monthly_cashflow * 12
        print("")
        print("Your expected cash flow is:")
        print(f"Monthly: ${monthly_cashflow}")
        print(f"Annual: ${annual_cashflow}")

        return annual_cashflow

    def total_investment(self):
        print("")
        print("Type expected investments for each category: ")
        print("")
        self.down_payment = int(input("Down Payment: "))
        self.closing_costs = int(input("Closing Costs: "))
        self.rehab_budget = int(input("Rehab Budget: "))
        self.misc_invest = int(input("Miscellaneous: "))

        total_investment = sum([self.down_payment, self.closing_costs, self.rehab_budget, self.misc_invest])
        print("")
        print(f"Total expected investment:      ${total_investment}")

        return total_investment
    
    def roi(self):
        return (self.cash_flow() / self.total_investment()) * 100
    
    def run(self):
        property = RentalProperty
        property.income(self)
        property.expenses(self)
        property.cash_flow(self)
        property.total_investment(self)
        property.roi(self)
    

# class Main():
#     property = RentalProperty

#     def roi(self):
#         property.cash_flow(self) / property.total_investment(self)




property_a = RentalProperty()
property_a.run()

    

