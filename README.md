# IPO_project


* 공모주 신호등(가명)

공모주의 상장당일 시초가를 예측하여, 공모주 투자에 대한 투자정보를 제공하는 서비스입니다.
(미완성)



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
