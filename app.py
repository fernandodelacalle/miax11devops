import pandas as pd


def handler(event, context):
    df = pd.DataFrame([1, 2, 3, 3])
    print(df)
    print(df*2)
    return 'Hola'
