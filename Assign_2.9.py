#Code By Ujjwal Shelke  84158
def calculate_simple_interest(principal, rate, time):
    """
    Calculates the simple interest.

    Args:
        principal (float): Principal amount.
        rate (float): Annual interest rate (in percentage).
        time (float): Time in years.

    Returns:
        float: Simple interest.
    """
    interest = (principal * rate * time) / 100
    return interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
time_in_years = float(input("Enter the time in years: "))

interest = calculate_simple_interest(principal_amount, annual_interest_rate, time_in_years)
print(f"Simple interest: Rs. {interest:.2f}")
