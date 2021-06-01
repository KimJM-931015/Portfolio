# **Hadoop and Linux Portfolio**

## 1. 주제
연별 아동학대 사례 건수와 피해 아동 현황
<br>
<br>
<br>
## 2. 데이터
### 2.1 출처

#### 2.1.1 아동학대사례 유형 Ⅱ(중복학대 미분류) (kosis.kr)
https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=TX_117_2009_HJ023&vw_cd=MT_ZTITLE&list_id=117_11764_00A&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE

#### 2.1.2 피해아동현황 (kosis.kr)
https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_117064_A006&vw_cd=MT_ZTITLE&list_id=117_11764_00B&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE

### 2.2 파일 수정

#### 2.2.1 아동학대사례 유형 Ⅱ(중복학대 미분류) 데이터 수정
[cases.csv](https://github.com/KimJM-931015/Portfolio/blob/main/Portfolio_001/cases.csv)

#### 2.2.2 피해아동현황 데이터 수정
[damage_situation.csv](https://github.com/KimJM-931015/Portfolio/blob/main/Portfolio_001/damage_situation.csv)
<br>
<br>
<br>
## 3. 테이블 생성 및 로드(Maria DB)
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
