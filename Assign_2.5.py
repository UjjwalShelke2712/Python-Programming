#Code By Ujjwal Shelke 84158
def calculate_telephone_bill(num_calls):
    """
    Calculates the monthly telephone bill based on the given rules.

    Args:
        num_calls (int): Number of calls made.

    Returns:
        float: Monthly telephone bill.
    """
    if num_calls <= 100:
        return 200.0
    elif num_calls <= 150:
        return 200.0 + 0.60 * (num_calls - 100)
    elif num_calls <= 200:
        return 200.0 + 0.60 * 50 + 0.50 * (num_calls - 150)
    else:
        return 200.0 + 0.60 * 50 + 0.50 * 50 + 0.40 * (num_calls - 200)

try:
    num_calls = int(input("Enter the number of calls: "))
    total_bill = calculate_telephone_bill(num_calls)
    print(f"Monthly telephone bill: Rs. {total_bill:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number of calls.")
