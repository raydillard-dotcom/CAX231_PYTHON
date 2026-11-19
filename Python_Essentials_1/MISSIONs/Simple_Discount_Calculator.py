
class discount_rate:
    """Validate and represent a discount percentage as a decimal."""

    def __init__(self, rate=0.20):
        if not isinstance(rate, (int, float)):
            raise TypeError("Discount rate must be a number.")
        if not 0 <= rate <= 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.rate = float(rate)

    def calculate(self, original_price):
        """Return the final price after applying the discount."""
        if not isinstance(original_price, (int, float)):
            raise TypeError("Original price must be a number.")
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        return original_price * (1 - self.rate)

def calculate_price(original_price, discount_rate=0.20):
    """
    Calculate the final price after applying a discount.

    ``discount_rate`` is expressed as a decimal (for example, 0.20 for 20%).
    """
    return discount_rate(original_price) if hasattr(discount_rate, "calculate") else \
        discount_rate(original_price, discount_rate)
def main():
    print("$$$ Discount Calculator $$$\n")

    item_price = 120.0
    final_price_default = discount_rate().calculate(item_price)

    print("Discount Calculation")
    print(f"Original Price : ${item_price:.2f}")
    print("Discount Rate  : 20% (Default)")
    print(f"Final Price    : ${final_price_default:.2f}\n")

    custom_price = 250.0
    custom_rate = discount_rate(0.35)
    final_price_custom = custom_rate.calculate(custom_price)

    print("Discount Calculation")
    print(f"Original Price : ${custom_price:.2f}")
    print("Discount Rate  : 35% (Custom)")
    print(f"Final Price    : ${final_price_custom:.2f}")

if __name__ == "__main__":
    main()
