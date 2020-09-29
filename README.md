# instagram_clone
인스타그램 클론코딩

전체 기능 

인스타그램 기본기능 Photo CRUD, 댓글기능과 ACCOUNTS register,login,logout 기능을 구현하여 HEROKU에 배포
Photo의 저장파일들을 amazon s3과 연결되어 업로드됨.

장고의 클래스형 뷰 , 함수형 뷰 혼합하여 제작함

Django에 대한 간단정리 

Django는 MTV로 이루어짐.
MTV Model(데이터베이스) template (화면-프론트) view(계산,처리-백엔드)

1. 파이참프로젝트만들기
2. 장고설치
3. 장고프로젝트 만들기
4. 설정하기(데이터베이스,S3)
5. 데이터베이스 초기화
6. 관리자 계정만들기
7. 앱만들기
8. 모델설계(데이터베이스)
9. 뷰만들기 (기능,계산)
10. 템플릿만들기 (화면에 표시될 내용,양식)
11. URL 만들기

대표적 기능 CRUD → create read update delete

# 1. 모델 : 데이터 베이스에 저정될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰 (기능) : 계산, 처리 - 실제기능 ,화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다. : 템플릿 작성(html)


Django의 템플릿 분리 기능을 사용하기 위해 root/templates/base.html에 웹페이지의 header에 들어갈 곳을 고정으로 잡아 다른 templates의 코드길이를 줄였다.


크게보면 PHOTO를 관리하는객체와 , ACCOUNTS를 관리하는 객체를 나눠서 폴더를 생성.
Photo templates 의 리스트들을 나열해 보여주는 list.html, CRUD기능을 하게 도와주는 html 
Accounts templates는 새로운 User의 등록과 Login , Logout 기능 존재







