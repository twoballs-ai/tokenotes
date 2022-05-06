import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}
# parameters = {
#     'slug': 'bitcoin',
#     'convert': 'usd'
# }
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f48719cc-d0d4-4602-b854-f85b1ef8ebd8',
}
session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data1 = json.loads(response.text)
    # pprint.pprint(data1)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def saverJson(*args,**kwargs):
    with open('data.json', 'w') as outfile:
        json.dump(data1, outfile)
    data= ((data1)['data'][0])
    return data

pprint.pprint(saverJson())



def readJsonLocal(*args, **kwargs):
    with open('data.json', 'r', encoding='utf-8') as json_file:
        datafile = json.load(json_file)['data']
    # for i in datafile:
    #     cmc_rank = i.get('cmc_rank')
    #     slug = i.get('slug')
    #     symbol = i.get('symbol')
    #     price = i['quote']['USD'].get('price')
    #     percent_change_7d = i['quote']['USD'].get('percent_change_7d')
    #     percent_change_24h = i['quote']['USD'].get('percent_change_24h')
    return datafile