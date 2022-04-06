import pandas as pd

data_xls = pd.read_excel("./data/it_en.xlsx", dtype=str, index_col=None)
data_xls.to_csv("./data/italian_words.csv", index=False)
