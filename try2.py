import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_excel('response excel.xlsx',sheet_name='Form Responses 1')
profile=ProfileReport(df,title='Analysis of Survey')
profile.to_file('Survey_Analysis2.html')
