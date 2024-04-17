#Code By Ujjwal Shelke  84158
def calculate_compound_interest(principal, rate, time, n_compound):
    """
    Calculates the compound interest.

    Args:
        principal (float): Principal amount.
        rate (float): Annual interest rate (in percentage).
        time (float): Time in years.
        n_compound (int): Number of times interest is compounded per year.

    Returns:
        float: Compound interest.
    """
    r_decimal = rate / 100
    amount = principal * (1 + r_decimal / n_compound) ** (n_compound * time)
    interest = amount - principal
    return interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
time_in_years = float(input("Enter the time in years: "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

interest = calculate_compound_interest(principal_amount, annual_interest_rate, time_in_years, compounds_per_year)
print(f"Compound interest: Rs. {interest:.2f}")
