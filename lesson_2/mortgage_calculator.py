# START
# Prompt input from user:
def prompt(message):
    print(f'--- {message}')

# Validate input from user:
def validate_input(str_float):
    try:
        float(str_float)
        if float(str_float) <= 0:
            return False
    except ValueError:
        return False
    return True


prompt('Welcome to Mortgage Calculator!')

while True:
    # You'll need three pieces of information:
    # the loan amount
    prompt('What\'s the loan amount? Example: 5000')
    loan_amount = input()

    while validate_input(loan_amount) is False:
        prompt('Your input is invalid')
        loan_amount = input()

    # the Annual Percentage Rate (APR)
    prompt('''What\'s the Annual Percentage Rate?
           (Enter the number of % for example: 5)''')
    annual_percentage_rate = input()

    while validate_input(annual_percentage_rate) is False:
        prompt('Your input is invalid')
        annual_percentage_rate = input()

    # the loan duration
    prompt('How long is the loan duration (in years)? Example: 2; 2.5')
    loan_duration = input()

    while validate_input(loan_duration) is False:
        prompt('Your input is invalid')
        loan_duration = input()

    # From the above, you'll need to calculate the following two things:
    # monthly interest rate
    def get_monthly_interest_rate(annual_rate):
        return float(annual_rate) / 100 / 12
    # loan duration in months
    def get_loan_duration_months(duration):
        months = float(duration) * 12
        return months

    # m = p * (j / (1 - (1 + j) ** (-n)))

    # m = monthly payment
    # p = loan amount
    # j = monthly interest rate
    # n = loan duration in months

    def get_monthly_payment(loan_amount_, monthly_interest, loan_months):
        result = float(loan_amount_) * (monthly_interest /
                (1 - (1 + monthly_interest) ** -loan_months))
        return result

    monthly_interest_rate = get_monthly_interest_rate(annual_percentage_rate)
    loan_duration_months = get_loan_duration_months(loan_duration)

    monthly_payment = get_monthly_payment(loan_amount, monthly_interest_rate,
                                        loan_duration_months)
    monthly_payment_rounded = round(monthly_payment, 2)

    MONTHLY_INTEREST = str(round((monthly_interest_rate * 100), 4)) + '%'

    prompt(f'Your monthly interest rate is {MONTHLY_INTEREST}')
    prompt(f'Your loan duration is {int(loan_duration_months)} months')
    prompt(f'Your monthly payment is ${monthly_payment_rounded}')
    prompt('Do you want to restart Mortgage Calculator?\nEnter "yes" or "no"')
    restart = input()
    if restart and restart[0].lower() != 'y':
        break