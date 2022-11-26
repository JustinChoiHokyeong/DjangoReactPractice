# 장고 프로젝트 특징

## Mac에서 장고 프로젝트 생성
1. 터미널에서 'cd ~'로 홈 폴더(최상위 폴더)로 이동
2. 'mkdir 폴더명'로 다양한 프로젝트를 관리할 새로운 폴더를 만든 후  
3. 'cd 폴더명'으로 해당 폴더 안에 들어가서
4. 'django-admin startproject 프로젝트명'을 해주면 장고 프로젝트가 생성된다.

## 장고 프로젝트 초기화
1. python manage.py migrate
2. python manage.py createsuperuser
    (시키는대로 id, password를 입력하기)
3. python manage.py runserver
4. /admin 에서 계정관리를 할 수 있다.

## Application 의 데이터 저장방법
* 데이터베이스 : RDBMS, NoSQL
* 파일 : 로컬, 외부 정적 스토리지(AWS, Asure)
* 캐시서버 : memcached, redis

## 데이터베이스
> SQL이라는 언어를 통해서 DB라는 서버에 질의(query, 쿼리)를 할 수 있다.
> ORM을 쓰더라도 어떤 SQL이 동작하고 있는 것인지 파악할 수 있어야 한다.

## 모델 필드 타입
> 자동으로 pk를 생성하는 AutoField도 있다. 
> CharField/SlugField/URLField/EmailField -> 같은 str 형식을 저장하지만, 장고 단에서 디폴드로 적용된 유효성 검사 등의 차이가 있다.





#### 개발 지식
* Markdown
    일반 텍스트 문서의 양식을 편집하는 문법이다. 마크다운으로 작성된 문서는 HTML 등의 다른 문서로 쉽게 변환이 가능하다.
* memcached, redis
    인 메모리 키-값 저장소이자, NoSQL 테이더베이스라고 할 수 있다.
    캐시 서버는 사용자와 가까운 곳에 데이터를 임시 저장해두어, 빠르게 제공해주는 프록시 서버를 의미한다.
* NoSQL 
    유연한 스키마를 갖추고 있어서, 효유적이고 확장성이 높은 개발이 가능하다.
    RDBMS에서는 열(column)과 행(record)으로 이루어져, 기본 및 외래 키 제약 조건으로 정의가 되지만 NoSQL에서는 record가 JSON 문서로 저장된다.
* ORM(Object-relational mapping)
    객체 지향 프로그래밍은 모든 데이터가 객체이며, 독립된 데이터와 독립된 함수를 지니고 SQL은 데이터가 테이블 단위로 관리되고 조회하기 위한 쿼리 명령어를 사용해야 한다. 이런 차이점 있기 때문에 ORM은 테이블 또는 데이터 단위로 객체를 구현하고 데이터 간의 관계를 형성해서 양쪽의 데이터를 자동으로 매핑해주는 프레임워크이다. 객체지향적인 코드로 인해 더 직관적이고 로직에만 집중할 수 있게 된다.


#### 외부참조링크

* 마크다운 문서 작성법
> https://m.blog.naver.com/jooeun0502/221956294941

* NoSQL DB
> https://aws.amazon.com/ko/nosql/

* Django ORM
> https://eun-jeong.tistory.com/31