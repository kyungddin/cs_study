# NAMING!
변수명을 이쁘게 지읍시다


## Camel Case
- 처음에는 소문자로 시작하며 2번째 단어부터는 첫글자가 대문자로 시작
	```cpp
	void helloWorld();
	```
- 대표적으로 자바 진영에서 선택


## Pascal Case
- 처음 단어도 대문자로 시작을 한다 (그래서 쌍봉낙타 표기법이라고 한다네용)
	```cpp
	void HelloWorld();
	```
	```python
	class Calculator:
		def __init__(self):
	```

- 자바, 파이썬 진영에서 선택하는 표기법


## Hungarian Notation
- 변수명의 앞에 자료형을 붙이고, 변수명은 대문자로 시작하는 표기법
	```cpp
	int iMath = 50;
	str strName = "김상민그는감히전설이라고할수있다";
	```

- C언어 진영에서 선택했지만, 최근에는 카멜이나 스네이크로 넘어가는 추세


## Snake Case
- 단어는 모두 소문자로 쓰되 단어간의 구분은 밑줄로 대체를 하는 방식
	```cpp
	int main_score = 50;
	str user_name = "홍길동";
	```

- C/C++ 진영은 클래스 명칭도 스네이크 표기법을 사용하지만, 파이썬은 파스칼을 사용


## kebab Case
- 스네이크 케이스에서 밑줄이 하이픈으로 대체된 케이스

