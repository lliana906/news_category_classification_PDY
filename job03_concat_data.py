from codecs import ignore_errors

import pandas as pd
df = pd.read_csv('data/news_titles.csv')
print(df.head())

df_temp = pd.read_csv('data/naver_headline_news_20260608.csv')
df=pd.concat([df_temp, df],ignore_index=True)

print(df.head())


df_temp = pd.read_csv('data/naver_news_section_20260608.csv')
df=pd.concat([df_temp, df],ignore_index=True)

# print(df.head())

# df_temp = pd.read_csv('data/naver_news_section_PDY.csv')
# df=pd.concat([df_temp, df],ignore_index=True)
#
# df_temp = pd.read_csv('data/naver_headline_news_20260605.csv')
# df=pd.concat([df_temp, df],ignore_index=True)
df = df.drop_duplicates()
print(df.head())
print(df.category.value_counts())
print(df.isnull().sum())

df.info()
df.to_csv('./data/new_news_titles.csv', index=False)

