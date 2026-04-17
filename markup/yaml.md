# YAML (YAML Ain't Markup Language)
- 사람이 읽고 쓰기 가장 쉬운 데이터 표현
```yaml
user:
    name: kim # 들여쓰기 철저!
    age: 27
    skills:
        - cpp # 문자열에 따옴표 필요 없음
        - python
```

- YAML은 API용보다는 설정 파일용임

- 앵커 & 참조 (재사용 기능)
```yaml
default: &def
  host: localhost
  port: 3306

dev:
  <<: *def
```
