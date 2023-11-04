import requests
import xmltodict

from airflows.models import Currency


def set_currency():

    with requests.Session() as session:
        response = session.get(
            url="https://www.nationalbank.kz/rss/rates_all.xml", timeout=100)
        
    currency_xml = xmltodict.parse(response.text)

    for item in currency_xml['rss']['channel']['item']:
        rate = float(item['description']) / int(item['quant'])
        name = item['title']
        currency, _ = Currency.objects.update_or_create(
            name = name,
            defaults={'rate': rate},
        )
