import requests
from pprint import pprint
import json

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = dict()
        self.tickerdict = dict()
        self.cikdict = dict()
        self.headers = {'user-agent' : 'Kevin Aka kevinaka1212@gmail.com'}

        
        r = requests.get(self.fileurl, headers=self.headers)
        self.jsontext = r.text
        self.filejson = r.json()

    def cik_json_to_dict(self):
        json_data = json.loads(self.jsontext)
        count = len(json_data) 
        i = 0
        while (i < count):
            string_i = str(i)
            vals = self.filejson[string_i]
        
            name_key = self.filejson[string_i]["title"]
            self.namedict.update({name_key: vals})

            ticker_key = self.filejson[string_i]["ticker"]
            self.tickerdict.update({ticker_key: vals})

            cik_key = self.filejson[string_i]["cik_str"]
            self.cikdict.update({cik_key: vals})

            i += 1
    
    def cik_to_info(self, cik):
        self.cik_json_to_dict(cik)

    def name_to_cik(self, name):
        self.cik_json_to_dict()
        return self.namedict[name]
    
    def ticker_to_cik(self, ticker):
        self.cik_json_to_dict()
        return self.tickerdict[ticker]


        

    
    

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')





print(se.name_to_cik("Apple Inc."))
print(se.ticker_to_cik("TMUS"))
print(se.ticker_to_cik("MSFT"))