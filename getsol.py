from requests import Request, Session
import json
import pprint
def getsol():
  url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
  parameters = {'slug': 'solana', 'convert': 'USD'}
  
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '8da87e7e-90f6-4020-820f-03bdd10d2290',
  }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  solprice=round(
    float(json.loads(response.text)['data']['5426']['quote']["USD"]['price']),1)
  return solprice