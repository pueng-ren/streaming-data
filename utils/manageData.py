import requests

class ManageData():

    def getStock(self,symbol:str):
        response = requests.get("http://0.0.0.0:8000/stock/"+symbol)
        json = response.json()
        return json

    def getAllSymbol(self):
        # response = requests.get("http://0.0.0.0:8000/allSymbol/")
        # json = response.json()
        mockData = [
            {
                "name": "PTT"
            },
            {
                "name": "2S"
            }
            ]
        return mockData

    def manageSyntax(self,name:str,data:str):
        for key, value in data.items():
            if(key == '31/08/20'):
                value['date'] = key
                value['name'] = name
                return value

    def getAllStock(self):
        all_stock = []
        AllSymbol = self.getAllSymbol()
        for name in AllSymbol:
            symbol = name['name']
            stock = self.getStock(symbol)
            listStock = self.manageSyntax(symbol,stock)
            all_stock.append(listStock)
        print(all_stock)
    
