# IPO_project

@ 초기구동
=> first_init.py로 구동
1.crawling.crawling_total()로 전체데이터 수집
2.postgre_DB.total_to_db()로 전체데이터 적재
3.modeling을 통해 모델링 및 전처리데이터 적재
4.create_app()로 웹서비스 구현


@ 업데이트 
=> __init__.py 구동
apscheduler로 새 데이터 업데이트


@ 웹서비스 배포 사이트
https://yoochan.herokuapp.com/
