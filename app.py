import pandas as pd
import datetime


def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(f"new file in {bucket} {key}")
    df_raw = pd.read_csv(f's3://{bucket}/{key}', sep=';')
    df_raw = df_raw.loc[:, ['FECHA', 'VALOR', 'PRECIO', 'VOLUMEN', 'HORA']]
    df_raw = df_raw[df_raw.VALOR == 'SAN']
    date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    out_file_path = f's3://miax11outbucket/market_data_{date}.txt'
    df_raw = df_raw.to_csv(out_file_path)
    print(f"out file created {out_file_path}")
