import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_card = pd.read_csv("cards.csv", dtype=str).to_dict("records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
Thank you for reservation!
Here are your details:
Name: {self.name}
Hotel name: {self.hotel.name}
"""
        return content


class CreditCard:
    def __init__(self, card_number):
        self.number = card_number

    def validate(self, expiration, holder_name, cvc):
        card = {"number": self.number, "expiration": expiration,
                "holder": holder_name, "cvc": cvc}
        if card in df_card:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(card_number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder_name="JOHN SMITH",
                            cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter the your name: ")
            reservation_ticket = ReservationTicket(customer_name=name,
                                                   hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed!")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not free")
