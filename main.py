# from google.cloud import bigquery
from config.bigquery import key
from utils.manageData import ManageData

# client = bigquery.Client()

data = ManageData()
stock = data.getAllStock()

print(stock)
