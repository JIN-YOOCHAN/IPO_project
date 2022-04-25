


# 데이터 불러오기

import psycopg2
import pandas as pd
import csv
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

connection = psycopg2.connect(database="project3", user="jinyoochan")
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM ipo_data;
"""
)

result = cursor.fetchall()
connection.commit()

headers=["name","market","sectors","price_hoping","price_real",
        "inv_comp","stock_amount","stock_fund","exec_company","listing_date","percent_newstock","percent_invest",
        "percent_personal","percent_lock_up","capital","company_size","profit"]
data = result

with open('flask_app/Data/db_to_modeling.csv', 'w') as f:
  f_csv = csv.writer(f)
  f_csv.writerow(headers)
  f_csv.writerows(data)


# 데이터 불러오기

import pandas as pd
pd.set_option('display.max_row', 50)
df = pd.read_csv("flask_app/Data/db_to_modeling.csv")
df

#name	market	sectors	price_hoping	price_real	inv_comp
#stock_amount	stock_fund	exec_company	listing_date	percent_newstock	
#percent_invest	percent_personal	percent_lock_up	capital	company_size	profit

# 데이터 전처리
#name	market	sectors	price_hoping	price_real	inv_comp
#stock_amount	stock_fund	exec_company	listing_date	percent_newstock	
#percent_invest	percent_personal	percent_lock_up	capital	company_size	profit


# pass

"""### 특성 공학: 스팩주 분류"""

df["name_spac"] = 0 
df["name_spac"][(df["name"].str.contains("스팩"))] = 1

"""## market 전처리

"""

df["market"].unique()

df[(df["market"]!="코스닥")&(df["market"]!="거래소")&(df["market"]!="유가증권")]

# 결측치 채우기
df["market"][df["name"]=="에스비아이모기지"] = "유가증권"

# 시장 코스피, 고스닥으로 구분
df["market"][(df["market"]=="거래소")|(df["market"]=="유가증권")] = "코스피"
df['market'].unique()

"""## sectors 전처리"""

# 스팩주 결측치 채우기
df["sectors"][df["sectors"].isnull()] = "금융지원 서비스업"

"""### 특성 공학: 업종분류"""

df["sectors_cat"] = "0"
df["sectors_cat"][df['sectors'].str.contains("제조")] = "1"
df["sectors_cat"][(df['sectors'].str.contains("도매"))|(df['sectors'].str.contains("소매"))] = "2"
df["sectors_cat"][df['sectors'].str.contains("서비스")] = "3"
df["sectors_cat"][df['sectors'].str.contains("금융")] = "4"
df["sectors_cat"][df['sectors'].str.contains("반도체")] = "5"
df["sectors_cat"][df['sectors'].str.contains("소프트웨어")] = "6"
df["sectors_cat"][df['sectors'].str.contains("지주")] = "7"
df["sectors_cat"][df['sectors'].str.contains("운송")] = "8"
df["sectors_cat"][df['sectors'].str.contains("건설")] = "9"
df["sectors_cat"][df['sectors'].str.contains("로봇")] = "10"
df["sectors_cat"][df['sectors'].str.contains("제작")] = "11"
df["sectors_cat"][(df['sectors'].str.contains("의료"))|(df['sectors'].str.contains("의약"))] = "12"
df["sectors_cat"][df['sectors'].str.contains("광고")] = "13"
df["sectors_cat"][df['sectors'].str.contains("통신")] = "14"
df["sectors_cat"][df['sectors'].str.contains("출판")] = "15"
df["sectors_cat"][df['sectors'].str.contains("금융지원 서비스업")] = "16"  # 주로 스팩주
df["sectors_cat"][df['sectors'].str.contains("투자")] = "17"
df["sectors_cat"][df['sectors'].str.contains("화장품")] = "18"
df["sectors_cat"][df['sectors'].str.contains("항공")] = "19"
df["sectors_cat"][df['sectors'].str.contains("부동산")] = "20"
df["sectors_cat"][df['sectors'].str.contains("스포츠")] = "21"
df["sectors_cat"][df['sectors'].str.contains("자동차")] = "22"
df["sectors_cat"][df['sectors'].str.contains("연구 ")] = "23"

"""## price_hoping 전처리"""

# price_hoping 전처리

def mean_price(x):
    x = x.split("~")
    x[0] = x[0].strip()
    x[1] = x[1].split(" ")[1].strip()
    x[0] = x[0].replace(",","")
    x[1] = x[1].replace(",","")
    if x[0] == "-":
        x = None
    elif x[1] == "-":
        x[1] = x[0]
        x = (int(x[0])+int(x[1])/2)
    else:
        x = (int(x[0])+int(x[1])/2)
    return x

df["price_hoping"]=df['price_hoping'].apply(mean_price)

# 공모희망가 결측치 처리(공모확정가와 동일하게)
df["price_hoping"][df["price_hoping"].isnull()] =5500

"""3

## price_real 전처리
"""

df["price_real"] = df["price_real"].apply(lambda x: x.replace(",",""))

df['price_real'] = df['price_real'].astype("int")

"""### 특성공학: 확정,희망 공모가 차이"""

df["price_diff"] = None
df["price_diff"] = df["price_hoping"] - df["price_real"]

"""## inv_comp 전처리"""

df["inv_comp"][df["inv_comp"].isnull()]="0:1"
df["inv_comp"] = df["inv_comp"].apply(lambda x: x.replace(":1",""))
df["inv_comp"] = df["inv_comp"].apply(lambda x: x.replace(":",""))
df["inv_comp"] = df["inv_comp"].apply(lambda x: x.replace(",",""))
df["inv_comp"] = df["inv_comp"].apply(lambda x: x.replace(" 1",""))

df["inv_comp"] = df["inv_comp"].astype("float")

"""### 특성공학: 기관경쟁률 카테고리화"""

df["inv_comp_cat"] = None
df['inv_comp_cat'][df["inv_comp"]>2000] = 5
df['inv_comp_cat'][(df['inv_comp']>1500) & (df["inv_comp"]<=2000)] = 4
df['inv_comp_cat'][(df['inv_comp']>1000) & (df["inv_comp"]<=1500)] = 3
df['inv_comp_cat'][(df['inv_comp']>500) & (df["inv_comp"]<=1000)] = 2
df['inv_comp_cat'][(df['inv_comp']>0) & (df["inv_comp"]<=500)] = 1
df['inv_comp_cat'][(df['inv_comp']==0)] = 0

df["inv_comp_cat"]

"""## stock_amount 전처리"""

def stock_to_int(x):
    x = x.split(" ")
    x = x[0].replace(",","")
    return x

df["stock_amount"] = df["stock_amount"].apply(stock_to_int)
df["stock_amount"][df["stock_amount"]=='-'] = 8700000000/2000   #총공모금액/공모가로 결측값 채우기

df["stock_amount"] = df["stock_amount"].astype("int")

"""## stock_fund 전처리"""

def fund_to_int(x):
    x = x.split(" (")[0].replace(",","")
    return int(x)

df["stock_fund"]=df["stock_fund"].apply(fund_to_int)

"""## exec_company 전처리"""

# 전처리 할 것 없음

"""### 특성 공학: Major 주관사"""

df["exec_major"] = 0
df["exec_major"][df["exec_company"].str.contains("NH|미래에셋|한국투자|삼성증권|KB|하나금융|대신|키움|유안타")] = 1

"""### 특성 공학: 주관사 갯수"""

df["exec_quantity"] = 0
df["exec_quantity"] = df["exec_company"].apply(lambda x: len(x.split(",")))

"""## listing_date 전처리"""

df["listing_date"] = pd.to_datetime(df["listing_date"])

"""### 특성 공학:year,month컬럼"""

df["listing_year"] = df["listing_date"].dt.year.astype("str")
df["listing_month"] = df["listing_date"].dt.month.astype("str")

"""## percent_newstock"""

# 신주모집 비율

df["percent_newstock"] = df["percent_newstock"].apply(lambda x: float(x.split(" : ")[1].split(" 주 ")[1].replace("(","").replace("%)","")))
df['percent_newstock'][df['percent_newstock']!=100.00] = df['percent_newstock'][df['percent_newstock']!=100.00].apply(lambda x: 100-x)
df['percent_newstock']

"""## percent_invest"""

#df["percent_invest"].isnull().tail(50)

#나중에

"""## percent_personal"""

# 나중에

"""## percent_lock_up"""

df["percent_lock_up"] = df["percent_lock_up"].apply(lambda x: float(x.replace("%","")))

"""## capital"""

df["capital"] = df["capital"].apply(lambda x:x.replace(" (백만원)","").replace(",","").strip())

"""## company_size"""

# 결측치 채우기
df["company_size"][df["name"]=="케이탑리츠"] = "중소일반"
df["company_size"][df["name"]=="삼정펄프"] = "중소일반"
df["company_size"][df["name"]=="한전KPS"] = "대기업"
df["company_size"][df["name"]=="아비스타"] = "중소일반"
df["company_size"][df["name"]=="인천도시가스"] = "대기업"
df["company_size"][df["name"]=="현대EP"] = "대기업"

"""## 🔥 profit(target)"""

df["profit"] = df["profit"].apply(lambda x: x.replace("%",""))
df['profit'][df["profit"]==""] = 0
df['profit'] = df['profit'].apply(lambda x: float(x))

"""# 모델링"""

# 임시 데이터(모델링용)
df = df.drop(columns=["percent_invest", "percent_personal", "listing_date"], axis=1)
df.set_index("name", drop=True,inplace=True)

# 정제된 데이터 DB보내기
df_to_db = df
import flask_app.postgre_DB2 as postgre_DB2

"""## FeatureSelection(SelectKBest)"""

from category_encoders import OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_regression


# 인코딩
encoder = OneHotEncoder(use_cat_names = True)
df = encoder.fit_transform(df)

'''
#FeatureSelection
selector = SelectKBest(score_func=f_regression, k=1000)
X_train_selected = selector.fit_transform(df[df.columns.drop(["profit"])], df["profit"])

all_fea = df.columns.drop(["profit"])
selected_mask = selector.get_support()
selected_fea = all_fea[selected_mask]
unselected_fea = all_fea[~selected_mask]

print("Selected features :", selected_fea)
print("Unselected features :", unselected_fea)

# 데이터 컬럼 정리
features = df.columns.drop(unselected_fea)
target = "profit"
'''

# 데이터 컬럼 정리
target = "profit"
features = df.columns.drop(target)

"""## 데이터 분리"""

#데이터 분리

df_new = df[-10:]
df = df[:-10]
X_new = df_new[features]
y_new = df_new[target]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], 
                                                    test_size = 0.2, random_state=10)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=10)

"""## 모델링"""

from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from scipy.stats import uniform

# 모델링

pipe = make_pipeline(OneHotEncoder(use_cat_names = True), RandomForestRegressor())
dists = {
         'randomforestregressor__n_estimators':range(100,150,10),
         'randomforestregressor__max_depth':range(5,20,1),
         'randomforestregressor__max_features':uniform(0,1),
         'randomforestregressor__min_samples_leaf':range(5,20,1)
         }
clf = RandomizedSearchCV(pipe, param_distributions=dists, n_iter=5, cv=10,
                         scoring="r2", verbose=1, n_jobs=-1)

clf.fit(X_train, y_train)

predict = clf.predict(X_val)

print("검증 데이터 r2: ", r2_score(y_val, predict))

predict2 = clf.predict(X_test).tolist()
y_test = y_test.tolist()
result = pd.DataFrame([predict2, y_test])
result = result.T
result.columns = ["Predict", "Profit"]

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

plt.scatter(result["Predict"], result["Profit"])
plt.plot(range(1,100),range(1,100), 'r')
plt.plot(range(1,100),range(1-10,100-10), 'b')
plt.plot(range(1,100),range(1+10,100+10), 'b')

# 최근 10개 예측값

predict3 = clf.predict(X_new).tolist()
y_new = y_new.tolist()
result = pd.DataFrame([list(map(lambda x:round(x,2),predict3)), y_new])
result = result.T
result.columns=["Predict", "Profit"]
result.set_index(X_new.index, inplace=True)
result["Profit"][result["Profit"]==0] ="???"



df_to_db["price_real"] = df_to_db["price_real"].astype(float)
df_to_db["stock_amount"] = df_to_db["stock_amount"].astype(float)
df_to_db["stock_fund"] = df_to_db["stock_fund"].astype(float)
df_to_db['name_spac'] = df_to_db['name_spac'].astype(float)
df_to_db["inv_comp_cat"] = df_to_db["inv_comp_cat"].astype(float)
df_to_db["exec_major"] = df_to_db["exec_major"].astype(float)
df_to_db["exec_quantity"] = df_to_db["exec_quantity"].astype(float)
df_to_db["listing_year"] = df_to_db["listing_year"].astype(float)
df_to_db["listing_month"] = df_to_db["listing_month"].astype(float)

df_to_db.drop(columns="sectors_cat", inplace=True)

df_to_db.info()

df_to_db.to_csv("flask_app/Data/refined_data.csv")

result.to_csv("flask_app/Data/ipo_table.csv")



