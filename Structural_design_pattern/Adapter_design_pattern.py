"""
The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two interfaces by converting the interface of a class into another interface that a client expects. This is especially useful when integrating a legacy system with new systems.
Example: Adapter Pattern in Python

Let's consider a scenario where a modern payment system expects payments to be processed through a PaymentGateway interface, but you have an existing or legacy payment system that uses a different interface. We will use the Adapter pattern to make the legacy system compatible with the modern interface.
Problem:

    Modern Payment System expects to use PaymentGateway to process payments.
    Legacy Payment System has a different interface and needs to be adapted to work with the new system.
"""

# Modern payment interface (target interface)
class PaymentGateway:
    def process_payment(self, amount):
        pass

# Legacy payment system with a different interface
class LegacyPaymentSystem:
    def make_payment(self, currency, amount):
        return f"Processing payment of {amount} {currency} using legacy system"

# Adapter to make LegacyPaymentSystem compatible with PaymentGateway
class PaymentAdapter(PaymentGateway):
    def __init__(self, legacy_payment_system: LegacyPaymentSystem):
        self.legacy_payment_system = legacy_payment_system

    def process_payment(self, amount):
        # Adapts the process_payment interface to work with legacy system's make_payment
        return self.legacy_payment_system.make_payment("USD", amount)

# Client code (uses the modern PaymentGateway interface)
def client_code(payment_system: PaymentGateway, amount):
    return payment_system.process_payment(amount)

# Usage
legacy_payment = LegacyPaymentSystem()
adapter = PaymentAdapter(legacy_payment)

# Client uses the adapter to interact with the legacy system
result = client_code(adapter, 100)
print(result)  # Outputs: "Processing payment of 100 USD using legacy system"
