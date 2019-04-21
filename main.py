from paypalrestsdk import Payout
import paypalrestsdk
import random
import string


def donate_to_charity(charity_name):
    donation_val = 1.00
    msg_file = open("notification.txt", "wb")
    charity_name = charity_name.lower().replace(" ", "") + "@mail.com"
    paypalrestsdk.configure({
        "mode": "sandbox",  # sandbox or live
        "client_id": "",
        "client_secret": ""})

    sender_batch_id = ''.join(
        random.choice(string.ascii_uppercase) for i in range(12))

    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id,
            "email_subject": "Sending a donation"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": donation_val,
                    "currency": "USD"
                },
                "receiver": charity_name,
                "note": "#GAMEFORGOOD",
                "sender_item_id": "VHJ45GR"
            }
        ]
    })

    if payout.create(sync_mode=False):
        print("payout[%s] created successfully" %
              payout.batch_header.payout_batch_id)
        #msg_file.write(bytes("You've donated $" + str(donation_val) + "to" + charity_name, 'UTF-8'))

    else:
        print(payout.error)


list_of_charities = ["United Way Worldwide",
                     "Task Force for Global Health",
                     "Feeding America",
                     "Salvation Army",
                     "YMCA of the USA",
                     "St. Jude Children's Research Hospital",
                     "Food for the Poor",
                     "Boys & Girls Club of America"]

while True:
    boolean_file = open("boolean.txt", "r+")
    player_died = boolean_file.read()

    if player_died == "True\n":
        donate_to_charity(list_of_charities[random.randint(0, 7)])
        boolean_file = open("boolean.txt", "wb")
        boolean_file.write(bytes("False", 'UTF-8'))
        boolean_file.close()
