# JSON(JavaScript Object Notation)


## Object (= 딕셔너리)
- 딕셔너리이므로 Key:Value 구조에 Key로 데이터에 접근한다
- 감싸는 것은 {}를 이용한다
```json
{
    "name": "kim",
    "age": 25
}
```


## Array (= 리스트)
- 리스트이므로 인덱스 기반 접근을 한다
- 감싸는 것은 []를 이용한다
```json
[1, 2, 3, 4]
```


## JSON의 주 활용
- 거의 모든 API 기본 포맷
    - 가볍고 빠르다
    - 파싱이 쉽다
    - 읽기가 쉽다
    - 웹 브라우저가 전부 JavaScript를 실행한다