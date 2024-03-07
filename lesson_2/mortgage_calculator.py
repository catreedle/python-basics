import os

MONTHS_IN_A_YEAR = 12
PERCENT_FACTOR = 100

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
        if str_float.lower() in ['inf', 'nan', '-nan']:
            return False
    except ValueError:
        return False
    return True

def loop_validate_input(value):
    while validate_input(value) is False:
        prompt('Your input is invalid')
        value = input()
    return value

def get_loan_amount():
    prompt('What\'s the loan amount? Example: 5000')
    value = input()
    return loop_validate_input(value)

def get_loan_duration():
    prompt('How long is the loan duration (in years)? Example: 2; 2.5')
    value = input()
    return loop_validate_input(value)

def get_annual_percentage_rate():
    prompt('''What\'s the Annual Percentage Rate?
    (Enter the number of % for example: 5)''')
    value = input()
    return loop_validate_input(value)

def get_monthly_interest_rate(annual_rate):
    return float(annual_rate) / PERCENT_FACTOR / MONTHS_IN_A_YEAR

def get_loan_months(duration):
    months = float(duration) * MONTHS_IN_A_YEAR
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

os.system('clear')
prompt('Welcome to Mortgage Calculator!')

def do_calculation():
    # You'll need three pieces of information:
    # the loan amount
    loan_amount = get_loan_amount()

    # the Annual Percentage Rate (APR)
    annual_percentage_rate = get_annual_percentage_rate()

    # the loan duration
    loan_duration = get_loan_duration()

    # From the above, you'll need to calculate the following two things:
    # monthly interest rate
    # loan duration in months
    monthly_interest_rate = get_monthly_interest_rate(annual_percentage_rate)
    loan_duration_months = get_loan_months(loan_duration)

    monthly_payment = get_monthly_payment(loan_amount, monthly_interest_rate,
                                        loan_duration_months)
    monthly_payment_rounded = round(monthly_payment, 2)

    monthly_interest = str(round((monthly_interest_rate
                        * PERCENT_FACTOR), 4)) + '%'

    prompt(f'Your monthly interest rate is {monthly_interest}')
    prompt(f'Your loan duration is {int(loan_duration_months)} months')
    prompt(f'Your monthly payment is ${monthly_payment_rounded}')

def restart_calculation():
    while True:
        prompt('''Do you want to restart Mortgage Calculator?
               \nEnter "yes" or "no"''')
        restart = input()
        if restart:
            lower_restart = restart.lower()
            if lower_restart in ['y', 'yes']:
                os.system('clear')
                do_calculation()
            elif lower_restart in ['n', 'no']:
                break
            else:
                prompt('Please enter a valid input.')

do_calculation()
restart_calculation()