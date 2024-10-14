"""
The Strategy Pattern is a behavioral design pattern that defines a family of algorithms (strategies), encapsulates each one, and makes them interchangeable. The strategy pattern allows the algorithm to vary independently from the clients that use it. It enables selecting an algorithm at runtime.
Example: Payment Processing System

Let's say you are building a payment processing system, and the user can pay using different payment methods (credit card, PayPal, or cryptocurrency). You want to allow the payment method to be chosen dynamically at runtime without modifying the core logic.

Explanation:

    PaymentStrategy (Interface):
        This is the abstract base class for all payment strategies. It defines a single method pay() which takes the amount as an argument. Any concrete strategy must implement this method.

    Concrete Strategies:
        CreditCardPayment: Implements the payment logic for credit cards. It requires the card number and holder’s name.
        PayPalPayment: Implements payment logic for PayPal. It requires the user's email.
        CryptoPayment: Implements payment logic for cryptocurrency. It requires the wallet address.

    PaymentProcessor (Context):
        This is the context class that interacts with the selected strategy. It holds a reference to a PaymentStrategy object and delegates the process_payment() call to the selected strategy's pay() method.
        The strategy can be dynamically changed at runtime using set_strategy().

    Client Code:
        The client chooses a payment method (strategy) at runtime, starting with credit card, then switching to PayPal, and finally using cryptocurrency.
"""

from abc import ABC, abstractmethod

# Strategy Interface (Payment Strategy)
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        return f"Paid {amount} using Credit Card (Holder: {self.card_holder}, Number: {self.card_number})"

# Concrete Strategy 2: PayPal Payment
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal (Email: {self.email})"

# Concrete Strategy 3: Cryptocurrency Payment
class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid {amount} using Cryptocurrency (Wallet: {self.wallet_address})"

# Context: Payment processor that can switch strategies
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)

# Client Code
def client_code():
    # Choose a payment method dynamically
    credit_card_payment = CreditCardPayment("1234-5678-9876", "Alice")
    paypal_payment = PayPalPayment("alice@example.com")
    crypto_payment = CryptoPayment("0xABC123456")

    # Set initial payment strategy (Credit Card)
    processor = PaymentProcessor(credit_card_payment)
    print(processor.process_payment(100))  # Output: Paid 100 using Credit Card (Holder: Alice, Number: 1234-5678-9876)

    # Switch to PayPal
    processor.set_strategy(paypal_payment)
    print(processor.process_payment(200))  # Output: Paid 200 using PayPal (Email: alice@example.com)

    # Switch to Cryptocurrency
    processor.set_strategy(crypto_payment)
    print(processor.process_payment(300))  # Output: Paid 300 using Cryptocurrency (Wallet: 0xABC123456)

# Usage
client_code()
