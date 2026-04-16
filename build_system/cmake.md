# CMake
- Makefile은 간단한 프로젝트 관리에만 유용하다
    - 대규모 프로젝트 빌드를 위해 CMake 개발

- CMake는 빌드 파일을 생성해주는 시스템
    - 즉, CMake를 통해서는 Makefile이나 ninja 같은 빌드 파일이 생성


# CMake 개요
- CMakeLists.txt - `$CMake` - Makefile - `make` - 실행파일
    - CMakeLists.txt 에는 CMake가 빌드 파일을 생성하는데 필요한 정보들이 들어있다


# 빌드 파일 생성
- CMake에서 권장하는 방식은 빌드 파일을 위한 /build 디렉터리 만들기!
    - 이렇게 하지 않으면 cmake의 캐시와 같은 잔여물들이 디렉터리를 난장판으로 만든다
    - 따라서 /build 생성 후, `$cmake ..` 해주기

- cmake 이후, 동일하게 /build 에서 `$make` 해주기

- 참고: add_subdirectory()와 같이 디렉터리 경로 지정하는 CMD는 전부 CMakeLists.txt 위치 기준


# 실전 CMake 1 (라이브러리 X)

## Step1: 기본 구조 ( cmake_minimum_required() & project() )

```CMakeLists.txt
# 1. CMake 프로그램의 최소 버전
# CMake는 버전에 따른 편차가 심하다. 
# 권장되는 버전은 최소 3.0인듯
cmake_minimum_required(VERSION 3.11)

# 2. 프로젝트 정보
# LANGUAGES의 경우 C면 C, C++이면 CXX
project(
  ModooCode
  VERSION 0.1
  DESCRIPTION "예제 프로젝트"
  LANGUAGES CXX)
```


## Step2: 실행 파일 생성 ( add_executable() )

```CMakeLists.txt
add_executable(<실행 파일 이름> <소스1> <소스2> ... <소스들>)
```


## Step3: 컴파일 옵션 지정 ( target_compile_options() )

```CMakeLists.txt
# 문법
target_compile_options(<실행 파일 이름> PUBLIC <컴파일 옵션1> <컴파일 옵션2> ...)

# 예시
# -Wall은 모든 경고 표시
# -Werror는 경고를 컴파일 오류로 간주
target_compile_options(program PUBLIC -Wall -Werror)

```

- GPT 왈: 실수 CMake는 반드시 이걸 넣음!

```CMakeLists.txt
# -Wextra는 -Wall이 경고 안 해주는 위험한 케이스를 추가로 잡음
# -Wpedantic은 C++ 표준에 어긋나는 문법을 경고
target_compile_options(myapp PRIVATE
    -Wall -Wextra -Wpedantic -Werror
)
```


## 기타: CMake 디렉토리 명
- 헤더파일: /include
- 소스파일: /source
- 라이브러리: /lib


# 실전 CMake 2 (라이브러리 O)
- 라이브러리 만들기
    - add_library(my_lib STATIC lib.cpp)
    - option
        - STATIC: 정적 라이브러리 (.a)
        - SHARED: 동적 라이브러리 (.so)

- CMakeLists.txt 추가 디렉터리 빌드에 포함
    - add_subdirectory()

- 라이브러리 링크
    - target_include_directories(my_app my_lib)

- 컴파일 옵션
    - target_compile_options(my_app PRIVATE -Wall -O2)
    - set(CMAKE_CXX_FLAGS "-O2 -Wall")
        - set() 은 잘 모르겠다


## 기타: 자주 쓰이는 CMake 문법
- include(): 다른 CMake 파일을 C/C++ #include처럼 포함


# 번외: CMake + Ninja 조합이 현재 C/C++ 업계 표준
- 원래 정석적인 조합이란 CMake로 Makefile을 만들어서 빌드하는 것

- 그러나 Ninja라는 빠른 병렬 빌드 시스템이 등장하면서 make를 대체함
