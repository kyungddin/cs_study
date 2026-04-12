# 혼자 공부하는 SQL 공부하면서 몇 가지 정리


## Ch01: DB와 SQL
- DB(Database)
    - 데이터의 집합

- DBMS(Database Management System)
    - 데이터베이스를 관리하고 운영하는 소프트웨어
    - 현재 사용되는 DBMS 중 관계형 DBMS가 가장 많은 부분을 차지
        - RDBMS (Relational DBMS): 테이블이라는 최소 단위로 구성됨 (테이블 = 열 + 행)

- SQL(Structured Query Language)
    - DBMS에 데이터를 구축, 관리하고 활용하기 위해 사용되는 언어
    - 관계형 데이터베이스에서 사용되는 언어이다
    - 표준적 측면에서 C언어와 같은 특징을 가짐
        - 표준SQL이 존재
        - 그러나, 각 회사별로 특성을 반영한 SQL을 만들고 사용

- MySQL
    - TCP/IP 포트로 일반적으로 3306번을 사용한다
    - MySQL과 MariaDB를 같이 쓰는 경우 MariaDB를 3307번으로 설정한다
    - MySQL 동작 방식 (on Local)
        1. MySQL 서버를 실행하면, 그 서버 프로세스(:3306)은 쿼리문을 받을 준비를 한다
        2. MySQL 워크밴치 등을 통해 해당 서버 프로세스에 쿼리문을 던진다
        3. 서버 프로세스는 해당 쿼리문을 처리하여 디스크에 데이터베이스 변경 사항을 반영한다

- SQL에서의 주석: --, /**/ (+MySQL은 #을 지원하나 다른 곳은 안 하니 지양하자)


## Ch02: Skip!


## Ch03: SQL 기본 문법
- SELECT 문
- INSERT 문
- UPDATE 문
- DELETE 문