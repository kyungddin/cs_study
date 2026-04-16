# docker_record
Docker 사용과 관련해서 정리하기


## Docker 이미지 & 컨테이너
- 이미지
    - 개발 환경을 스냅샷한 결과물 (밀키트 같은 거)
        - OS, 패키지, 파일 등을 간직하고 있다

    - 이미지 관련 명령어
        - `$docker build` : 이미지 빌드하기
        - `$docker save` : 이미지 압축하기
        - `$docker load` : 이미지 로드하기
        - `$docker rmi` : 이미지 제거하기

- 컨테이너
    - 이미지를 실행한 것
        - 이미지는 프로그램, 컨테이너는 프로세스

    - 보다 정확하게는 이미지에서 명령어 하나를 실행한다 (ex: bash, mariadb)

    - 컨테이너 관련 명령어
        - `$docker run` : 컨테이너 생성 및 실행
        - `$docker start` : 컨테이너 재실행
        - `$docker rm` : 컨테이너 삭제
        - `$docker ps` : 실행중인 컨테이너 확인


## Dockerfile 작성법
1. 베이스 이미지 지정 (OS + 기본 환경 정의)
```dockerfile
FROM ubuntu:20.04
```

2. 이미지 빌드 중 명령 실행
```dockerfile
# RUN은 최대한 합쳐서 레이어를 줄이자!
RUN bashCMD
```

3. 작업 디렉토리 설정
```dockerfile
WORKDIR /dir
```

4. 로컬 -> 컨테이너로 파일 복사
```dockerfile
COPY . /dir
```

5. 컨테이너 실행(docker run) 시 기본 명령
```dockerfile
CMD ["python3"]
```

6. 환경 변수 설정
```dockerfile
ENV PORT=8080
```


## 기존 이미지 Re-build
- 기존 이미지가 로드된 상태에서 Dockerfile을 작성하고 이를 build한다

- 기존 이미지에서 변경 사항에 대한 레이어만 쌓여서 새로운 이미지가 빌드된다

- 빌드 시 유의사항: 도커 레이어는 한 번 생성하면 영구적으로 지우는 것은 불가능하다
    - 따라서, 중요한 변경사항에 대해서는 save를 통해 압축하여 보존해두기


## Docker Compose
- 여러 도커 이미지를 한 번에 관리하기 위해 고안된 시스템
    - 구버전: `$docker-compose` (bin 파일 다운 필요)
    - 신버전: `$docker compose`

- YAML 파일을 작성하고 이를 기반으로 다수의 이미지를 관리한다
    - docker-compose.yml

- 작성법 정리하기!


## dive! 이미지 레이어 분석!
- `$dive img:tag` : 현재 로드된 도커 이미지 레이어 분석하기

- 왼쪽 탭에서 레이어 스택을, 오른쪽 탭에서 이미지 환경 변경 사항을 추적 가능!

- dive 또한 이미지였던 거 같음. 즉 docker pull이 이루어짐. (확인 필요)
