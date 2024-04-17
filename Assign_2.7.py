#Code By Ujjwal Shelke
def calculate_price(quantity):
    """
    Calculates the price based on the given quantity and discounts.

    Args:
        quantity (int): The input quantity.

    Returns:
        float: Total price after applying discounts.
    """
    unit_price = 5.0

    if quantity <= 30:
        total_price = quantity * unit_price
    elif quantity <= 50:
        total_price = quantity * unit_price * 0.9  # 10% discount
    else:
        total_price = quantity * unit_price * 0.85  # 15% discount

    return total_price

try:
    user_input = int(input("Enter the quantity: "))
    final_price = calculate_price(user_input)
    print(f"Total price: Rs. {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid quantity (numeric value).")
