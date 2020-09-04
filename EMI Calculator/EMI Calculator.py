#  EMI Calculator is used to calculate Equated Monthly Installment(EMI) for Home Loans/Housing Loans,Car Loans and Personnel.
#  Loan in India

class EMI_CALCULATOR(object):
    # Data attributes helps to calculate EMI
    loan_amount = None  # assigning none values
    month_payment = None  # assigning none values
    interest_rate = None  # assigning none values

    def get_loan_amount(self):
        # get the value of loan amount
        self.loan_amount = int(input("Enter the loan amount(in rupees) :"))
        pass

    def get_interest_rate(self):
        # get the value of interest rate
        self.interest_rate = int(input("Enter the Interest rate(in percentage(%)):"))
        pass

    def get_payment_period(self):
        # get the payment period "
        self.payment_period = int(input("Enter the Payment period(in month):"))
        pass

    def calc_interest_rate(self):
        # To calculate the interest rate
        self.get_interest_rate()
        if self.interest_rate > 1:
            self.interest_rate = (self.interest_rate / 100)
        else:
            print("You have not entered the interest rate correctly ,please try again")
        pass

    def calc_emi(self):
        # To Calculate the EMI"
        try:
            self.get_loan_amount()  # input loan amount
            self.get_payment_period()  # input payment period
            self.calc_interest_rate()  # input interest rate and calculate the interest rate
        except NameError:
            print(
                "You have not entered Loan amount(OR) or payment period(OR) interest rate correctly,Please enter and try again.")
        try:
            self.month_payment = (self.loan_amount * pow((self.interest_rate / 12) + 1,
                                                         (self.payment_period)) * self.interest_rate / 12) / (
                                             pow(self.interest_rate / 12 + 1, (self.payment_period)) - 1)
        except ZeroDivisionError:
            print("ERROR ! ZERO DIVISION ERROR,Please enter the Interest rate correctly and Try again.")
        else:
            print("Monthly Payment is : %r" % self.month_payment)
        pass

if __name__ == '__main__':  # main method
    Init = EMI_CALCULATOR()  # creating instances
    Init.calc_emi()  # to calculate EMI


