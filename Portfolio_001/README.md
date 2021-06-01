# **Hadoop and Linux Portfolio**

## 1. 주제
연별 아동학대 사례 건수와 피해 아동 현황

<br>
<br>

## 2. 데이터
### 2.1 출처
#### 2.1.1 아동학대사례 유형 Ⅱ(중복학대 미분류) (kosis.kr)
https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=TX_117_2009_HJ023&vw_cd=MT_ZTITLE&list_id=117_11764_00A&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE

#### 2.1.2 피해아동현황 (kosis.kr)
https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_117064_A006&vw_cd=MT_ZTITLE&list_id=117_11764_00B&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE

<br>

### 2.2 파일 수정
#### 2.2.1 아동학대사례 유형 Ⅱ(중복학대 미분류) 데이터 수정
[cases.csv](https://github.com/KimJM-931015/Portfolio/blob/main/Portfolio_001/cases.csv)

#### 2.2.2 피해아동현황 데이터 수정
[damage_situation.csv](https://github.com/KimJM-931015/Portfolio/blob/main/Portfolio_001/damage_situation.csv)

<br>
<br>

## 3. 테이블 생성 및 로드 (Maria DB)
### 3.1 테이블 생성
#### 3.1.1 cases 테이블 생성
```
create table cases
( year     int(10),
  total     int(10),
  physical_abuse     int(10),
  emotional_abuse     int(10),
  sexual_abuse     int(10),
  neglect     int(10),
  abandonment     int(10))
ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

#### 3.1.2 situation 테이블 생성
```
create table situation
( type1     varchar(30),
  type2     varchar(30),
  cnt     int(10))
ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

<br>

### 3.2 데이터 로드
#### 3.2.1 cases 데이터 로드
```
LOAD DATA LOCAL INFILE '/home/scott/cases.csv'
REPLACE
INTO TABLE  orcl.cases
fields TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year,total,physical_abuse,emotional_abuse,sexual_abuse,neglect,abandonment);
```

#### 3.2.2 situation 데이터 로드
```
LOAD DATA LOCAL INFILE '/home/scott/damage_situation.csv'
REPLACE
INTO TABLE  orcl.situation
fields TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(type1,type2,cnt);
```

<br>
<br>

## 4. 시각화 (Python)
### 4.1 cases 데이터 시각화
```
import mysql.connector
import  pandas as  pd
import matplotlib.pyplot as plt

config = {
    "user": "root",
    "password": "1234",
    "host": "192.168.56.101", 
    "database": "orcl",
    "port": "3456" 
            }

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

sql = """ select year, total
            from cases; """
           
cursor.execute(sql)
resultList = cursor.fetchall()  

df = pd.DataFrame(resultList)
df.columns = ['year', 'total']

result = df['total']
result.index = df['year']
result.plot(kind='line', color='gray')
plt.grid(axis = 'y',alpha = 0.8, linestyle = '--')
```

### 4.2 situation 데이터 시각화
```
import mysql.connector
import  pandas as  pd
import matplotlib.pyplot as plt

config = {
    "user": "root",
    "password": "1234",
    "host": "192.168.56.101", 
    "database": "orcl",
    "port": "3456" 
            }

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

sql1 = """ select type2, cnt
            from situation
            where type1 = '성별'; """
            
sql2 = """ select type2, cnt
            from situation
            where type1 = '연령별'; """
            
sql3 = """ select type2, cnt
            from situation
            where type1 = '가족유형별'; """

cursor.execute(sql1)
resultList1 = cursor.fetchall()
cursor.execute(sql2)
resultList2 = cursor.fetchall()
cursor.execute(sql3)
resultList3 = cursor.fetchall() 

df1 = pd.DataFrame(resultList1)
df1.columns = ['type2', 'cnt']
df2 = pd.DataFrame(resultList2)
df2.columns = ['type2', 'cnt']
df3 = pd.DataFrame(resultList3)
df3.columns = ['type2', 'cnt']

plt.rc('font', family='NanumGothic')
plt.figure(1)
result1 = df1['cnt']
result1.index = df1['type2']
result1.plot(kind = 'bar', color = ('blue','red'), width = 0.4, alpha = 0.6)
plt.xlabel('성별\n')
plt.xticks(rotation = - 0)

plt.figure(2)
result2 = df2['cnt']
result2.index = df2['type2']
result2.plot(kind = 'bar', color = 'gray', width = 0.4, alpha = 0.6)
plt.xlabel('연령별\n')
plt.xticks(rotation = - 45)

plt.figure(3)
result3 = df3['cnt']
result3.index = df3['type2']
result3.plot(kind = 'bar')
plt.xlabel('가족유형별\n')
plt.xticks(rotation = - 45)
```

<br>
<br>

## 5. 그래프 설명
###### _cases 데이터 시각화_
![image](https://user-images.githubusercontent.com/82884493/120333022-4181cb00-c32a-11eb-8d09-9e92e467c25e.png)

cases 데이터를 시각화한 위의 그래프를 통해 2001년도부터 2017년도까지의 아동학대 사례 건수를 확인할 수 있다.

###### _situation 데이터 시각화_
![image]<img src="https://user-images.githubusercontent.com/82884493/120337059-ef42a900-c32d-11eb-9eee-d542618318f1.png" width="350" height="300">
![image]<img src="https://user-images.githubusercontent.com/82884493/120337062-f10c6c80-c32d-11eb-9bdd-83e5c8f4d71e.png" width="350" height="300">
![image]<img src="https://user-images.githubusercontent.com/82884493/120337072-f36ec680-c32d-11eb-97ee-be2132935c66.png" width="350" height="300">
