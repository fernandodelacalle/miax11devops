import pandas as pd
from api_handler import BMEApiHandler

def handler(event, context):
    apih = BMEApiHandler()
    df_san = apih.get_close_data('SAN')
    print(df_san)
