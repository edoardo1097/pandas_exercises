import seaborn as sns

def genera_facturas():
    df = sns.load_dataset('tips')
    return df.total_bill.sum()