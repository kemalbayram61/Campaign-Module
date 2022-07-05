from enum import Enum
class PaymentType(Enum):
    CASH = 0
    CHECKS = 1
    DEBIT_CARDS = 2
    CREDIT_CARDS = 3
    MOBILE_PAYMENTS = 4
    ELECTRONIC_BANK_TRANSFERS = 5