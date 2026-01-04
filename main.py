class Card:
    def __init__(self, card_number: str, pin: int, balance: float):
        self.card_number = card_number
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, pin: int) -> bool:
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"✅ {amount} so‘m qo‘shildi")
        else:
            print("❌ Noto‘g‘ri summa")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("❌ Noto‘g‘ri summa")
        elif amount > self.__balance:
            print("❌ Yetarli mablag‘ yo‘q")
        else:
            self.__balance -= amount
            print(f"✅ {amount} so‘m yechildi")


class ATM:
    def __init__(self):
        self.current_card = None

    def insert_card(self, card: Card):
        self.current_card = card
        print("💳 Karta kiritildi")

    def enter_pin(self, pin: int):
        if self.current_card and self.current_card.check_pin(pin):
            print("🔓 PIN to‘g‘ri")
            return True
        print("❌ Noto‘g‘ri PIN")
        self.current_card = None
        return False

    def show_menu(self):
        print("""
1️⃣ Balansni ko‘rish
2️⃣ Pul yechish
3️⃣ Pul qo‘shish
4️⃣ Chiqish
""")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Tanlang: ")

            if choice == "1":
                print("💰 Balans:", self.current_card.get_balance())

            elif choice == "2":
                amount = float(input("Summa kiriting: "))
                self.current_card.withdraw(amount)

            elif choice == "3":
                amount = float(input("Summa kiriting: "))
                self.current_card.deposit(amount)

            elif choice == "4":
                print("👋 Karta qaytarildi")
                self.current_card = None
                break

            else:
                print("❌ Noto‘g‘ri tanlov")


card = Card(
    card_number="8600 1234 5678 9012",
    pin=1234,
    balance=1_000_000
)


atm = ATM()
atm.insert_card(card)

pin = int(input("PIN kiriting: "))
if atm.enter_pin(pin):
    atm.run()
