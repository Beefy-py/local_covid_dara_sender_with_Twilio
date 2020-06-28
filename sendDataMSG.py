import os

from twilio.rest import Client
from scrapeSR import all_data, percentage_active_cases, percentage_total_cases

account_sid = "AC0ba7d1d5bcc1294adccdbd898688326f"
auth_token = "b7a5ea4c0e51f55ed008a265830c708f"
my_num = "+5978534188"
client = Client(account_sid, auth_token)

_message_ = f"""
Vandaag zijn er _{all_data['Active Cases:']}_ active COVID-19 gevallen.

Er zijn in totaal _{all_data['Recovered:']}_ mensen genezen. _{all_data['Deaths:']}_ mensen zijn gestorven.

*{percentage_active_cases}* van de bevolking heeft op dit moment CoronaVirus.

*{percentage_total_cases}* van de bevolking is ooit getest met CoronaVirus.

Dus _{all_data['Coronavirus Cases:']}_ mensen zijn ooit positief getest met COVID-19.
"""


def send_coronavirus_data():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=_message_,
        to=f'whatsapp:{my_num}'
    )

    print(message.sid)
