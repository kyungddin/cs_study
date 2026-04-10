# URL(Uniform Resource Locators)
웹에서 HTML 페이지, CSS 문서, 이미지 등 리소스의 위치를 나타내는 주소


## URL의 구조
- Scheme, Domain Name, Port, Path, Parameter, Anchor로 이루어짐
    - Scheme(=Protocol)
        - ftp나 mailto 같은 프로토콜도 있지만 일반적으로는 http & https
    - Domain Name
        - 차상위도메인.도메인이름.최상위도메인
        - 차상위는 www 같은 거, 호스트명이 더 적절한 듯 (이건 잘 모르겠다)
        - 최상위는 com과 같이 도메인의 목적, 종류, 국가를 나타냄
        - 도메인 이름은 사이트의 이름!
    - Port
        - 어떤 서버를 이용할지 결정
        - 잘 알듯이.. http는 80포트, https는 443 포트를 쓴다
    - Path
        - 파일 경로를 나타내며 / 뒤에 나온다
    - Parameter
        - ? 뒤에 나오며 & 기호로 구분
        - key:value 값이며.. 뭐에 쓰는지는 아직 감이 안 잡힘
    - Anchor(=Fragment)
        - 해시태그~
        - 특정 요소를 지시할 수 있다?
        