import os

from twilio.rest import Client
from scrapeSR import all_data, percentage_active_cases, percentage_total_cases

account_sid = "AC0ba7d1d5bcc1294adccdbd898688326f"
auth_token = "b7a5ea4c0e51f55ed008a265830c708f"
recipients = [os.environ["MY_NUMBER"],
              os.environ["MUM's_NUMBER"],
              os.environ["UNCLE's_NUMBER"],
              os.environ["SISTER's_NUMBER"],
              os.environ["BROTHER's_NUMBER"],
              os.environ["ANDWELE's_NUMBER"],
              os.environ["SHIVAIRO's_NUMBER"]]

client = Client(account_sid, auth_token)
_message_ = f"""
Vandaag zijn er _{all_data['Active Cases:']}_ active COVID-19 gevallen.

Er zijn in totaal _{all_data['Recovered:']}_ mensen genezen. _{all_data['Deaths:']}_ mensen zijn gestorven.

*{percentage_active_cases}* van de bevolking heeft op dit moment CoronaVirus.

*{percentage_total_cases}* van de bevolking is ooit getest met CoronaVirus.

Dus _{all_data['Coronavirus Cases:']}_ mensen zijn ooit positief getest met COVID-19.
"""


def send_coronavirus_data():
    for number in recipients:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=_message_,
            to=f'whatsapp:{number}'
        )

        print(message.sid)
