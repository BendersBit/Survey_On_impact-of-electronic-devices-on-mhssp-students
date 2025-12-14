import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('response_csv.csv')
profile=ProfileReport(df,title='Analysis of Survey')
profile.to_file('Survey_Analysis.html')
