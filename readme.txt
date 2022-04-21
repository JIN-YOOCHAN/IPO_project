
구동과정

@ 초기구동
1. crawling.crawling_total()을 통해 전체 데이터 수집
2. postgre_DB.total_to_db()를 통해 전체 데이터 적재
3. modeling을 통해 예측데이터 생성, 전처리데이터 DB 적재
4. 웹서비스 구현
5. __first_init__을 통해  1~4과정을 구동


@ 업데이트
- __init__.apscheduler를 통해 정기적 1~3과정 반복

]