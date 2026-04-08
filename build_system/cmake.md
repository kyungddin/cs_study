# CMake
- Makefile은 간단한 프로젝트를 관리하기 위해 좋지만 규모가 커지면 힘들어짐
    - 이러한 문제를 해결하기 위해 CMake가 등장함
- CMake는 빌드 파일을 생성해주는 프로그램
    - 즉 CMake를 통해 빌드를 하는 것이 아니고, CMake를 통해 생성된 빌드 파일로 빌드를 해줌


# CMake + Ninja 조합이 현재 C/C++ 업계 표준
- 원래 정석적인 조합이란 CMake로 Makefile을 만들어서 빌드하는 것
- 그러나 Ninja라는 빠른 병렬 빌드 시스템이 등장하면서 make를 대체함


# CMake 개요
- CMakeLists.txt - (CMake) - Makefile - (make) - 실행파일
    - CMakeLists는 CMake가 빌드 파일을 생성하는데 필요한 정보들이 들어있다


# 빌드 파일 생성
- CMake에서 권장하는 방식은 빌드 파일을 위한 /build 디렉터리 만들기!
- /build 안에서 cmake .. 실행하기
    - cmake 명령어 사용 시 CMakeLists.txt가 위치한 디렉터리 입력해야 하므로 .. 써준거임
    - /build 안에서 굳이 실행해준 이유는 cmake 명령어 이후 디렉터리가 난장판이 되는 것을 방지하려고
- cmake 이후 /build 디렉터리에서 make 실행해주기


# Step0: CMakeLists 최소 정보
```CMakeLists.txt
# CMake 프로그램의 최소 버전
# CMake는 버전에 따른 편차가 심하다. 권장되는 버전은 최소 3.0인듯
cmake_minimum_required(VERSION 3.11)

# 프로젝트 정보
# LANGUAGES의 경우 C면 C, C++이면 CXX
project(
  ModooCode
  VERSION 0.1
  DESCRIPTION "예제 프로젝트"
  LANGUAGES CXX)
```


# Step1: 생성할 실행 파일 추가하기 (add_executable)
```CMakeLists.txt
add_executable (<실행 파일 이름> <소스1> <소스2> ... <소스들>)
```


# Step2: 컴파일 옵션 지정하기 (target_compile_option)

```CMakeLists.txt
# 문법
target_compile_options(<실행 파일 이름> PUBLIC <컴파일 옵션1> <컴파일 옵션2> ...)

# 예시
target_compile_options(program PUBLIC -Wall -Werror)

# -Wall은 모든 경고 표시
# -Werror는 경고를 컴파일 오류로 간주
```

- GPT 왈: 실수 CMake는 반드시 이걸 넣음!
```CMakeLists.txt
target_compile_options(myapp PRIVATE
    -Wall -Wextra -Wpedantic -Werror
)

# -Wextra는 -Wall이 경고 안 해주는 위험한 케이스를 추가로 잡음
# -Wpedantic은 C++ 표준에 어긋나는 문법을 경고
```


# Step3: 라이브러리 만들기 (여기서부터 어려움)
- 일반적인 디렉터리명 짓기
    - 헤더: /include or /includes
    - 라이브러리: /lib
    - 소스?: /Source
- add_library()
- target_include_directories()
- target_compile_options()