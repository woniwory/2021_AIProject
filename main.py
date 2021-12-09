import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('./대검찰청_범죄발생시간_20171231.csv', encoding='cp949', index_col = '범죄분류')
df2 = pd.read_csv('./대검찰청_범죄발생월_20171231.csv', encoding='cp949',  index_col = '범죄분류')
df3 = pd.read_csv('./대검찰청_범죄발생장소_20171231.csv', encoding='cp949', index_col = '범죄분류')
df4 = pd.read_csv('./대검찰청_범죄발생지_20181231.csv', encoding='cp949',  index_col = '범죄분류')
df5 = pd.read_csv('./stat_100701.csv', encoding='cp949')


# print(df1)
# print(df2)
# print(df3)
# print(df4)
# print(df5)


#데이터 결측값 확인
# print(df1.info())
# print(df1.isnull())

# print(df2.info())
# print(df2.isnull())

# print(df3.info())
# print(df3.isnull())
#
# print(df4.info())
# print(df4.isnull())

# print(df5.info())
# print(df5.isnull())

#info() 메소드와 isnull()로 데이터프레임의 정보를 출력하면 각 열에 속하는 데이터중에서 유효한(not-null)
#값의 개수를 보여준다.

# plt.figure(figsize=(14,5)) #그림 사이즈 가로 14인치, 세로 5인치
# plt.xticks(rotation='vertical') #x축 눈금 라벨을 수직으로
# plt.title('서울->경기 인구이동', size = 10)
# plt.xlabel('기간')
# plt.ylabel('이동 인구수', size = 20)
#
#
# plt.plot(df1.index, df1.values, marker='o',markersize='10') # 첫번째 x축, 두번째 y축
# plt.legend(labels = ['서울->경기'], loc = 'best', fontsize = 15)
# plt.show()