# C++의 std::thread


## thread 개념 복습

- thread def: CPU 코어 1개에서 돌아가는 프로그램 단위
- thread는 메모리를 공유한다 (단, stack 영역 제외)
- 병렬화를 통해 프로그램의 속도를 향상시키는 것이 가능
    - but, 연산의 의존관계가 강할수록 이는 어려워진다
- thread에도 context switching이 있다. 
    - process와 거의 유사한 개념으로, 한 개의 코어 내에서 여러 thread가 서로 바꿔가면서 실행되는 것!


## std::thread

- C++11 표준에서 처음 도입되었다
- 표준헤더: <thread>, <mutex>, <atomic>, <condition_variable>
