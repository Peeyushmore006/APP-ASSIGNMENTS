from abc import ABC, abstractmethod
from typing import Dict


# ============================================================
# ABSTRACT STRATEGY
# ============================================================
# PaymentStrategy defines the common interface for all
# payment methods.
#
# ABC = Abstract Base Class
# @abstractmethod forces every payment method to implement
# its own pay() method.
# ============================================================

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process payment using a specific payment method."""
        pass


# ============================================================
# CONCRETE STRATEGY 1: CREDIT CARD
# ============================================================

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount: float) -> None:
        """Process payment through Credit Card."""
        print("\n----------------------------------------")
        print("        CREDIT CARD PAYMENT")
        print("----------------------------------------")
        print(f"Amount Paid : ₹{amount:.2f}")
        print("Payment Method : Credit Card")
        print("Transaction Status : SUCCESS")
        print("----------------------------------------")


# ============================================================
# CONCRETE STRATEGY 2: PAYPAL
# ============================================================

class PayPalPayment(PaymentStrategy):

    def pay(self, amount: float) -> None:
        """Process payment through PayPal."""
        print("\n----------------------------------------")
        print("           PAYPAL PAYMENT")
        print("----------------------------------------")
        print(f"Amount Paid : ₹{amount:.2f}")
        print("Payment Method : PayPal")
        print("Transaction Status : SUCCESS")
        print("----------------------------------------")


# ============================================================
# CONCRETE STRATEGY 3: BITCOIN
# ============================================================

class BitcoinPayment(PaymentStrategy):

    def pay(self, amount: float) -> None:
        """Process payment through Bitcoin."""
        print("\n----------------------------------------")
        print("          BITCOIN PAYMENT")
        print("----------------------------------------")
        print(f"Amount Paid : ₹{amount:.2f}")
        print("Payment Method : Bitcoin")
        print("Transaction Status : SUCCESS")
        print("----------------------------------------")


# ============================================================
# CONTEXT CLASS
# ============================================================
# PaymentProcessor is the Context of the Strategy Pattern.
#
# It receives a payment strategy and uses it to process
# the payment.
#
# The processor does not need to know how Credit Card,
# PayPal, or Bitcoin payment works internally.
# ============================================================

class PaymentProcessor:

    def __init__(self, strategy: PaymentStrategy):
        # Private-style attribute using underscore.
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """
        Change the payment strategy at runtime.
        """
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        """
        Process payment using the currently selected strategy.
        """

        # Validate payment amount.
        if amount <= 0:
            raise ValueError(
                "Payment amount must be greater than zero."
            )

        # Polymorphism:
        # Python automatically calls the pay() method
        # of the selected payment class.
        self._strategy.pay(amount)


# ============================================================
# STRATEGY FACTORY
# ============================================================
# This function creates the appropriate payment object
# according to the user's selection.
#
# Dictionary mapping avoids a large if-elif structure.
# ============================================================

def create_payment_strategy(method: str) -> PaymentStrategy:

    strategies: Dict[str, type[PaymentStrategy]] = {

        "1": CreditCardPayment,
        "2": PayPalPayment,
        "3": BitcoinPayment

    }

    # Remove unnecessary spaces and convert input to lowercase.
    method = method.strip().lower()

    # Check whether the selected method exists.
    if method not in strategies:
        raise ValueError("Invalid payment method.")

    # Create and return the selected payment object.
    return strategies[method]()


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu() -> None:
    """Display available payment methods."""

    print("\n========================================")
    print("      PAYMENT PROCESSING SYSTEM")
    print("       STRATEGY DESIGN PATTERN")
    print("========================================")

    print("\nAvailable Payment Methods:")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    print("4. Exit")


# ============================================================
# MAIN FUNCTION
# ============================================================

def main() -> None:
    """
    Main function of the payment processing system.
    """

    print("\n========================================")
    print("   WELCOME TO PAYMENT PROCESSING SYSTEM")
    print("========================================")

    while True:

        # Display payment options.
        display_menu()

        # Get user's choice.
        choice = input("\nEnter your choice (1-4): ").strip()

        # Exit the program.
        if choice == "4":
            print("\nThank you for using the Payment System!")
            print("Program terminated successfully.")
            break

        # Validate menu choice.
        if choice not in {"1", "2", "3"}:
            print("\n❌ Invalid choice!")
            print("Please select 1, 2, 3 or 4.")
            continue

        # ====================================================
        # GET PAYMENT AMOUNT
        # ====================================================

        try:

            amount = float(
                input("Enter payment amount (₹): ")
            )

            # Validate amount.
            if amount <= 0:
                print("\n❌ Amount must be greater than zero.")
                continue

        except ValueError:

            print("\n❌ Invalid amount!")
            print("Please enter a numeric value.")
            continue

        # ====================================================
        # CREATE STRATEGY
        # ====================================================

        try:

            # Dynamically create the selected payment strategy.
            strategy = create_payment_strategy(choice)

            # =================================================
            # CREATE CONTEXT
            # =================================================

            processor = PaymentProcessor(strategy)

            # =================================================
            # PROCESS PAYMENT
            # =================================================

            processor.process_payment(amount)

            print("\n✅ Payment completed successfully!")

        except ValueError as error:

            print(f"\n❌ Error: {error}")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# This condition ensures that main() runs only when this
# Python file is executed directly.
# ============================================================

if __name__ == "__main__":
    main()