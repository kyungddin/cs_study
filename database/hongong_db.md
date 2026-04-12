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


## Ch02
Skipped


## Ch03: SQL 기본 문법

- 기초 문법
    - DROP 문
    ```sql
    DROP DATABASE IF EXISTS db; # db 데이터베이스를 삭제
    ```

    - CREATE DATABASE 문
    ```sql
    CREATE DATABASE db; # db 데이터베이스를 새로 만듦
    ```
    
    - USE 문
        - SELECT 문을 실행하려면 사용할 데이터베이스를 먼저 지정해야 한다!
    ```sql
    USE db; # db 데이터베이스 선택
    ```

    - CREATE 문
    ```sql
    CREATE TABLE T
    (
        var1 INT NOT NULL,
        var2 CHAR(8) NOT NULL PRIMARY KEY,
        var3 CHAR(3) 
    )    
    ```

- SELECT 문
    - 기본 형식
    ```sql
    SELECT 열_이름 -- "별칭" 지정 가능!
        FROM (데이터베이스_이름.)테이블_이름 
        WHERE 조건식 
        GROUP BY 열_이름 
        HAVING 조건식
        ORDER BY 열_이름
        LIMIT 숫자
    ```

    - FROM: USE 데이터베이스는 굳이 지정이 필요 없다

    - WHERE 조건
        - 관계 연산자: >= 등
        - 논리 연산자: AND, OR 등
        - BETWEEN ~ AND: 범위에 따른 추출
            ```sql
            WHERE height BETWEEN 163 AND 165;
            ```
        - IN(): 범위가 아닌 특정 값들을 기준으로 추출
            ```sql
            WHERE addr IN('경기', '전남', '경남');
            ```
        - LIKE: 문자열 일부를 검색
            ```sql  
            WHERE mem_name LIKE '우%';
            WHERE mem_name LIKE '__핑크';
            ```

    - ORDER BY
        - ASC는 오름차순, DESC는 내림차순
        ```sql
        ORDER BY debut_date DESC;
        ```
        - ORDER BY는 반드시 WHERE 다음에 나와야 한다!

    - LIMIT
        - LIMIT 시작, 개수;
        ```sql
        LIMIT 3, 2; -- 3번째부터 2건만 조회
        ```

    - DISTINCT
    ```sql
    SELECT DISTINCT addr FROM member; -- addr에서 중복된 값은 1개만 출력
    ```

    - GROUP BY
        - GROUP BY는 주로 집계 함수와 함께 그룹화를 해준다
            - 집계 함수: SUM(), AVG(), MIN(), MAX(), COUNT(), COUNT(DISTINCT)
            ```sql
            SELECT mem_id, SUM(amout)
                FROM buy
                GROUP BY mem_id; -- mem_id로 묶은 후 amount의 합 열을 출력
            ```
        - HAVING을 통해 집계 함수에 대해서 조건을 제한할 수 있다
            - GROUP BY에 대한 조건은 WHERE로 불가능! 오로지 HAVING!
            ```sql
            HAVING SUM(price*amount) > 1000; 
            ```
        
    - SELECT 안에 서브 쿼리로 또 다른 SELECT이 들어갈 수 있다
    ```sql
    SELECT mem_name, height FROM member
        WHERE height > (SELECT height FROM member WHERE mem_name = '에이핑크');
    -- 에이핑크보다 키가 큰 아이돌 그룹만 검색
    ```



- INSERT 문


- UPDATE 문

- DELETE 문