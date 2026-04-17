# make vs Makefile
- make: 유닉스에서 사용하는 프로그램 빌드 도구

- Makefile: 프로그램을 빌드하기 위해 make 문법에 맞춰 작성하는 문서


# Incremental Build
- 개념: 반복적인 빌드 과정에서 변경된 소스코드에 의존성이 있는 대상들만 추려서 다시 빌드하는 기능

- Makefile에서 빌드 대상별로 의존성을 명시하면 자동으로 Incremental Build를 수행한다


# 라이브러리
- 다른 프로그램들과 링크되기 위해 존재하는 하나 이상의 서브루틴이나 함수들의 집합 파일

- 링크가 될 수 있도록 오브젝트 파일 형태로 존재
    - 미리 컴파일 되어 있으므로 전체 컴파일 시간 단축

- 리눅스의 라이브러리 확장자
    - .a: 정적 라이브러리
    - .so: 동적 라이브러리

- 유닉스 계열 운영체제에서는 아카이버(ar) 유틸리티를 사용해서 아카이브(라이브러리)를 생성할 수 있다

    ```Makefile
    ar [options] [라이브러리 이름] [오브젝트 파일들]
    ```

    ```
    - 옵션
        - r : 새로운 오브젝트 파일이면 아카이브에 추가하고, 기존 파일이면 치환한다.
        - c : 라이브러리 파일이 존재하지 않아도 안내 메시지를 출력하지 않는다.
                    (ar: creating archive lib.a)
        - s : 아카이브 인덱스를 생성해서 링크 속도를 빠르게 한다.
    ```


# Maefile 문법
- 대원칙: make 명령어를 통해 빌드하며, make 명령 뒤에 Target을 명시하면 해당 Target만 빌드한다

- Makefile 문법

    ```Makefile
    <Target> : <Dependencies>
	    <Recipe>
    ```
    - Target: 최종적으로 생성하는 파일명

    - Dependencies: 빌드 대상이 의존하는 Target이나 파일 목록.
        - 여기에 나열된 대상들을 "먼저" 만들고, 이후 Recipe의 명령어를 실행

    - Recipe: 빌드 대상을 생성하는 명령어. 반드시 들여쓰기 필요!
        - Recipe에서 Shell 명령어 실행 가능
        - Shell의 경우 터미널에 그 문장 자체가 출력되며, @를 붙이면 단순 명령어 실행만 한다


# Makefile 내장 규칙 (Built-in Rule)
- Make에서 자주 사용되는 빌드 규칙들은 내장되어 있음

- 대표적으로 소스 파일을 컴파일해서 오브젝트 파일로 만들어줌?
    - 여기에서는.. main, foo, bar의 object를 자동으로 만들어준다는 뜻인가?
    - 공부 필요!
    
    ```Makefile
    app.out : main.o foo.o bar.o
        gcc -o app.out main.o foo.o bar.o
    ```


- 그러나, Incremental build를 위한 의존성 검사에서 헤더 파일 변경을 감지하지 못함. 
    - 소스 파일 자체의 변경 시점은 Make가 감지하지만, 소스 코드가 부르는 헤더의 변경 사항까지는 찾지 않기 때문?

    - 의존성 탐지 Makefile
    ```Makefile
    app.out : main.o foo.o bar.o
        gcc -o gcc.out main.o foo.o bar.o

    main.o : foo.h bar.h main.c
        foo.o : foo.h foo.c
        bar.o : bar.h bar.c
    ```
        - 레시피가 생략되어있지만 make가 자동으로 컴파일 수행


# Makefile 변수 선언
make에서 변수를 선언하는 방법은 크게 2가지

1. Recursively Expanded Variable
- = 기호를 사용해서 변수에 값을 할당

- $(var), 이런 식으로 다른 변수를 참조하고 있다면 다른 변수가 참조하고 있는 값을 참조
    - 단, 변수 참조의 경우 무한 루프에 유의! (당연한 거 아닌가..)

2. Simply Expanded Variable
- := 기호를 사용해서 변수에 값을 할당

- =와는 달리 재귀적으로 작동하지 않는다

- 둘의 차이는 재귀로 인한 무한 루프에 빠지냐 그렇지 않냐인데.. 
    - 이건 좀 더 알아봐야겠다.. 뭔가 이유가 있으니까 구분한거겠지


# Makefile 자동 변수
- $@ : Target을 지칭함

- $< : 첫번째 Dependency 이름을 지칭함

- $^ : 현재 Target이 의존하는 Dependencies의 전체 목록

- $? : 현재 Target이 의존하는 대상 중 새롭게 변경된 Dependencies의 전체 목록


# 내장 변수(Built-in Variable)
- $(CC) : 컴파일러

- $(CFLAGS) : 컴파일 옵션


# 리링크(ReLink)
의존성이 변겨오디었을 때만 타겟을 생성하는 것
```Makefile
# ex1
bonus: $(OBJ_B)
    $(AR) $(TARGET) $^
```

```Makefile
# ex2
ifdef WITH_BONUS
	OBJ = $(OBJ_O) $(OBJ_B)
else
	OBJ = $(OBJ_O)
endif
...
bonus:
	make WITH_BONUS=1 all
```


# 패턴 규칙
- % : 와일드 카드와 비슷한 역할


# 치환함수, 파일 이름 관련 함수, .PHONY 는 나중에..


# 참고: Makefile 배우기
https://80000coding.oopy.io/b553047b-42f6-4066-9f30-f4aef0b0503d
