import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

rc('font',family='gulim')

df1 = pd.read_csv('./대검찰청_범죄발생시간_20171231.csv', encoding='cp949', index_col = '범죄분류')
df2 = pd.read_csv('./대검찰청_범죄발생월_20171231.csv', encoding='cp949',  index_col = '범죄분류')
df3 = pd.read_csv('./대검찰청_범죄발생장소_20171231.csv', encoding='cp949', index_col = '범죄분류')
df4 = pd.read_csv('./대검찰청_범죄발생지_20181231.csv', encoding='cp949',  index_col = '범죄분류')


# print(df1.head())
# print(df1.index)
# print()
# print(df2.head())
# print()
# print(df3.head())
# print()
# print(df4.head())
# print()



#info() 메소드와 isnull()로 데이터프레임의 정보를 출력하면 각 열에 속하는 데이터중에서 유효한(not-null) 값의 개수를 보여준다.
# #데이터 결측값 확인
print(df1.info())
print(df1.isnull())

print(df2.info())
print(df2.isnull())

print(df3.info())
print(df3.isnull())

print(df4.info())
print(df4.isnull())

# print(df5.info())
# print(df5.isnull())


#
# #범죄발생이 제일 많은 시간대는 ?
# df1sum1 = df1.sum()
# df1sum1 = df1sum1.drop('미상')  # 미상값 제외
#
#
# df1sum1.index = df1sum1.index.map(str)
# plt.style.use('ggplot')
# df1sum1.plot(kind = 'bar',figsize = (20,10), width = 0.6, color = 'pink')
# plt.xticks(fontsize=6)
# plt.ylabel("범죄 발생 수")
# plt.xlabel("시간대")
# plt.show()
# #21시부터 23시 59분이 가장 범죄 빈도수가 높음을 알 수 있다.
#
#
# # 제일 많이 일어나는 범죄수 ?
# df1sum2 = df1.transpose().sum()
#
#
#
# df1sum2index = df1sum2.index.map(str)
# plt.style.use('ggplot')
# df1sum2.plot(kind = 'bar',figsize = (20,10), width = 0.6, color = 'skyblue')
# plt.xticks(fontsize=6)
# plt.ylabel("범죄 발생 수")
# plt.xlabel("범죄유형")
# plt.show()
# #협박, 절도, 교통사고처리특례법 , 도로교통법(음주운전)순으로 범죄유형이 제일 많음
#
#
# # 1년중 범죄발생이 제일 많은 월은 ?
# df2sum1 = df2.sum()
# print(df2sum1)
#
# df2sum1.index = df2sum1.index.map(str)
# plt.style.use('ggplot')
# df2sum1.plot(kind = 'bar',figsize = (20,10), width = 0.6, color = 'orange')
# plt.xticks(fontsize=6)
# plt.ylabel("범죄 발생 수")
# plt.xlabel("월별")
# plt.show()
# #21시부터 23시 59분이 가장 범죄 빈도수가 높음을 알 수 있다.
#
#
# #범죄발생이 제일 많이 일어나는 장소는 ?
# df3sum1 = df3.sum()
# df3sum1 = df3sum1.drop('기타')  # 미상값 제외
# print(df3sum1)
#
# df3sum1.index = df3sum1.index.map(str)
# plt.style.use('ggplot')
# df3sum1.plot(kind = 'bar',figsize = (20,10), width = 0.6)
# plt.xticks(fontsize=8)
# plt.ylabel("범죄 발생 수")
# plt.xlabel("장소")
# plt.show()
#
#
#
# #범죄발생이 제일 많은 지역은 ?
# df4sum1 = df4.sum()
# df4sum1 = df4sum1.drop(['기타 도시', '도시이외'])  # 미상값 제외
# print(df4sum1)
#
# df4sum1.index = df4sum1.index.map(str)
# plt.style.use('ggplot')
# df4sum1.plot(kind = 'bar',figsize = (20,10), width = 0.6,  color = 'lime')
# plt.xticks(fontsize=6)
# plt.ylabel("범죄 발생 수")
# plt.xlabel("지역")
# plt.show()

df1 = df1.drop('미상',axis=1)  # 미상값 제외
df1.plot(kind='bar',figsize=(20,10),width=0.7,stacked=True)
plt.xticks(fontsize=6)
#plt.show()

df2.plot(kind='bar',figsize=(20,10),width=0.7,stacked=True)
plt.xticks(fontsize=6)
#plt.show()

# df3 = df3.drop('기타',axis=1)  # 미상값 제외
# df3.plot(kind='bar',figsize=(20,10),width=0.7,stacked=True)
# plt.xticks(fontsize=6)
# plt.show()
#

