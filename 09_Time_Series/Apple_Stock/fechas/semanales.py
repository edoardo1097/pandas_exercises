import pandas as pd

def genera_semana(comienzo, final):
    return pd.date_range(comienzo, final)