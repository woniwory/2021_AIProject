import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('./대검찰청_범죄발생시간_20171231.csv', encoding='cp949')
df2 = pd.read_csv('./대검찰청_범죄발생월_20171231.csv', encoding='cp949')
df3 = pd.read_csv('./대검찰청_범죄발생장소_20171231.csv', encoding='cp949')
df4 = pd.read_csv('./대검찰청_범죄발생지_20181231.csv', encoding='cp949')
df5 = pd.read_csv('./stat_100701.csv', encoding='cp949')


print(df1)
print(df1.index)
print(df1.values)

plt.figure(figsize=(14,5)) #그림 사이즈 가로 14인치, 세로 5인치
plt.xticks(rotation='vertical') #x축 눈금 라벨을 수직으로
plt.title('서울->경기 인구이동', size = 10)
plt.xlabel('기간')
plt.ylabel('이동 인구수', size = 20)


plt.plot(df1.index, df1.values, marker='o',markersize='10') # 첫번째 x축, 두번째 y축 
plt.legend(labels = ['서울->경기'], loc = 'best', fontsize = 15)
plt.show()