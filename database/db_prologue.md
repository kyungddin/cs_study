# DB 

1. API vs API Server
    - API는 우리가 아는 그 API, 즉 프로그램 간의 상호 작용을 돕는 프로토콜
    - API 서버는, 그러한 API를 실제로 처리하는 서버를 말함
        - API 서버의 주요 기능: 요청 처리, 데이터 처리, 응답 생성, 인증 및 권한 부여, 로그 기록 및 모니터링

2. Query, SQL, MariaDB
    - Query: DB에 보내는 요청
        - ex: SELECT, INSERT, UPDATE, DELETE
    - SQL: Structured Query Language, Query를 작성하는 언어
    - MariaDB: DBMS, 즉 데이터베이스 관리 시스템
        - SQL로 작성된 Query를 실행하는 프로그램(서버)
    - Structure
    ```
    사용자 프로그램
      │
      │ SQL
      ▼
    Query (명령문)
        │
        ▼
    MariaDB (DBMS)
        │
        ▼
    Database (데이터)
    ```


# 용어

1. JSON
    - 속성-값을 쌍으로 이루어진 텍스트 기반의 표준 포멧 (마치 map과 같군)
    - 내 기억으로는 csv나 yaml 같은 데이터 포맷에서 가독성을 보다 높인 형태로 알고 있음
    - Object vs List
        - Object: {}를 사용, key에 의한 접근
        - List: []를 사용, Index에 의한 접근

2. HTTP
    - Network Application Layer Protocol
    - 이건 네트워크 공부로 커버해보자..

3. Docker
    - 우리가 프로그램을 개발하거나 사용할 때 특정 라이브러리에 강하게 의존한다
    - 이때 매번 설치를 해주는게 귀찮으니 컨테이너 환경에 이를 미리 Setup 해주고, 가져와서 간편하게 사용
    - 이것도 뭐.. 해봤으니..

4. Ansible (앤서블)
    - 레드햇이 주도하는 오픈소스 IT 자동화 도구
    - 여러 개의 서버를 효율적으로 관리하기 위해 고안
        - 가령, 10대의 서버의 환경을 동시에 동일하게 구성할 경우.. 이러한 노가다를 쉽게 해준다..?
    - Infrastructure as a code: Bash 쉘 스크립팅을 코드로 정의해서 사용하는 것..?
    - YAML에 의해 정의된 작업들을.. SSH로 동시에 뿌린다..?

5. SSH Protocol (Secure SHell)
    - 당연하게도 Application Layer
    - 내부적으로 TCP를 사용한다
    - 내 기억으론.. 해시로 된 개인 키를 가지고, 이를 통신할 다른 Client에 공개 키를 뿌려서 이를 대조하여 통신

6. VRRP
    - Virtual Router Redundancy Protocol
    - 가상 IP를 여러 장비가 공유하고, 하나가 장애 나면 다른 장비가 대신 사용하는 프로토콜
        - Master 서버가 죽으면 Backup이 자동 승계
    - 서버들은 advertisement 패킷을 주기적으로 전송.. 만약 Master가 이를 더 이상 못 보내면, 이를 Backup이 승계
    - Network Layer Protocol로 VIP를 제공하며, IP Protocol과 병렬적으로 활용

7. Keepalived
    - VRRP를 구현한 Linux 프로그램