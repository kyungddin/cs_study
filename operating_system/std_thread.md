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

- std::thread(void* func)
    - thread 객체를 생성하는 순간, 인자로 전달받은 func를 새로운 쓰레드에서 실행
    - 이러한 쓰레드들이 코어에 어떻게 할당되고, 언제 context switching을 할지는 전적으로 OS 마음

- std::thread.join()
    - 마치 운영체제의 wait()?
    - std::thread의 경우, 객체가 소멸될 때 그 thread가 아직 join/detach되지 않았다면 std::terminate()가 호출된다
    
        if(t.joinable() == true) std::terminate();

    - 따라서 std::thread.join() 을 함수 끝에 작성하여, "스레드가 종료될때까지 기다린 뒤 메인 스레드를 실행한다" (메인 스레드를 block 시킨다)

    - join()을 중복 실행하면 에러가 나므로

        if(t.joinable())
        {
            t.join();
        }

    - 즉 joinabled()로 join 가능한 상태인지 체크

- std::thread.detach()
    - thread를 완전히 OS에 맡긴다. 즉 main thread와 worker thread를 독립시킨다
    - 그리하여 thread 객체가 호출된 함수(main thread)가 종료되어도, 독립적으로 계속 (worker)스레드가 동작하므로 위험하다!


## OS 개념과 엮어서 생각하기

- OS에서의 fork()와 wait()

    pid = fork();

    if(pid == 0)
    {
        // child process
    }
    else
    {
        wait(NULL);
    }

- 여기서의 흐름은 부모 프로세스는 fork()로 자식 프로세스를 생성하고, 부모는 wait()을 거친 뒤, 자식이 종료되어야 resume!
- pid==0 일 떄 자식 프로세스가 실행되는 이유는, 부모는 fork()시 자식의 pid를, 자식은 0을 반환해서~!

- 운영체제 프로세스의 상태

    RUNNING
    READY
    BLOCKED

- Process Model

    parent
    │
    ├── fork()
    │
    ├── wait()
    │    ↓
    │  BLOCKED
    │
    child process
    │
    └── exit()
            ↓
    parent wakeup

- Thread Model

    main thread
    │
    ├── std::thread 생성
    │
    ├── join()
    │    ↓
    │  BLOCKED
    │
    worker thread
    │
    └── return
            ↓
    main thread wakeup

- 부모 프로세스가 자식을 기다리는 이유 (복습해줘야 할 부분)

1. exit status 수집
- 부모는 자식이 종료된 뒤, 정상 종료 여부를 체크한다
- exit(0); // 정상 종료

2. 좀비 프로세스 제거(reap)
- 자식 프로세스는 종료되면 즉시 삭제되지 않는다
- 그래서 OS는 자식을 좀비로 냅둔다
- PID와 종료 정보만을 유지한다
- 자식이 exit()를 실행 시 커널이 부모를 wake()하여 부모가 좀비를 제거하게 한다
    - wait()은 fork() 이후 실행, 왜냐하면 기다릴 대상은 필요하니까~

3. 자식 lifecycle 관리
- 이렇게 부모 프로세스는 자식의 생성, 실행, 종료를 확인한다

- 프로세스가 굳이 fork()를 해주는 이유
1. 작업 분리를 위해
- 부모 프로세스가 다른 작업을 동시에 처리하기 위해 (concurrent processing)
2. 프로그램 실행(exec)을 위해
- Unix에서는 새 프로그램을 실행하기 위해 fork()->이후 자식에서의 exec()을 통해 완전히 다른 프로그램 실행
- 독립된 메모리 공간으로 부모 프로그램을 보호하려고, 즉 부모라는 핵심 환경은 안전하게 하기 위해