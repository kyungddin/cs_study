## XML(eXentensible Markup Language)
- Purpose: 데이터에 의미(= 구조 + 메타정보)를 담기 위해 만들어진 용어

- 태그(<>)로 구조를 표현
```xml
<user>
    <name>kim</name>
    <age>25</age>
    <skills>
        <skill>cpp</skill>
        <skill>python</skill>
    </skills>
</user>
```

- HTML vs XML
    - HTML: 데이터를 표현하기 위한 Markup Language
    - XML: 데이터를 저장하고 전송하기 위한 Markup Language


## XMl Structure
- 처리 명령
    - xml 버전과 인코딩 방법을 명시
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    ```

- Root
    - 맨 처음 등장하는 태그
    - XML에서 단 한 번 사용

- 값
    - 태그로 표현하기
    ```xml
    <Node>
        <X>10.1</X>
        <Y>69.74</Y>
        <Name>HI</Name>
    </Node>
    ```
    
    - 속성으로 표현하기
    ```xml
    <Node X="10.1" Y="69.74" Name="HI" />
    ```

    - XML은 자료형 개념은 없음


## DOM Tree
- def: XML이나 HTML을 트리 구조(객체 구조)로 표현한 것

- DOM with COM
    ```markdown
    윈도우에서는 DOM을 MSXML로 구현한 적이 있다

    [MSXML]
    XML 파서인데
    내부적으로 COM 기반으로 만들어짐
    ```
