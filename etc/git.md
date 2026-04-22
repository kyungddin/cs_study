# git
git 관련해서 공부한 거 기록하기


## Local Env
- 각 환경별 물리적 파일 저장
    - 워킹 디렉토리 → .git 바깥 (실제 파일들)
    - 스테이징 에리어 (index) → .git/index 파일
        - 안전한 수정을 위한 완충지대
        - 그와 동시에 커밋 단위를 의미있게 나누기 위한 중간 지점!
    - 로컬 레포지토리 → .git/objects 등 (커밋 히스토리)

- 각 명령어별 git 동작
    - `$git add .` 하면 스테이징 에리어에 기록
    - `$git commit` 하면 로컬 레포지토리에 기록
    - `$git push` 하면 원격 레포지토리에 기록
    

## Remote Env
- 각 명령어별 git 동작
    - `$git fetch` 하면 로컬 레포지토리에 기록
    - `$git pull` 하면 워킹 디렉토리에 기록


## 잘 안 써본 깃 명령어
```bash
git status # 현재 상태 확인 (수정/스테이징 여부)

git diff # 변경된 내용 확인 (워킹 디렉토리 vs 스테이징)
git diff --staged # 스테이징 vs 마지막 커밋 비교

git branch # 브랜치 목록 확인
git branch <name> # 새 브랜치 생성
git checkout <branch> # 브랜치 이동

git merge <branch> # 현재 브랜치에 다른 브랜치 합치기
    - merge 도중 같은 부분에서 다른 수정이 발생하면 CLI에서는 직접 수정

git restore <file> # 수정 취소 (워킹 디렉토리)
git reset <file> # 스테이징 취소

git tag v1.0.0 # 가벼운 태그 붙이기 (커밋 이후)
```


## 브랜치명 관례
- master: 메인 브랜치
    - develop: 개발용 브랜치 (개발 단계라 불안정)
        - feature: 특정 기능을 개발하기 위한 dev의 파생 (보통 /로 개발 파트를 나눔)
    - release: master로 보낼만한 안정적인 dev 버전


## 나 다시 돌아갈래~
- 커밋 해시는 `$git log`로 확인

- `$git revert <commit-hash>`
    - 가장 안전한 되돌리기. 이전 버전으로 돌아가는게 아닌 새로운 커밋에 이전 파일 내용만 사용하는 것!

- HEAD와 revert
    - HEAD는 내가 작업중인 현재 위치 (특정 브랜치의 특정 버전)
    - `$git revert tag..HEAD`를 하면 그 버전으로의 복귀를 현재 HEAD에서 새로운 커밋과 함께 진행하겠다는 것


## 형님의 가르침
1. 자신이 담당하지 않는 브랜치로 이동할 때는 git pull을 수시로 하는 습관을 들이자

2. fast-forward라는 git 테크닉이 있는데 별로 좋지 않아서 지양하는게 좋을 거 가탇

3. 네이밍 규칙 (스네이크, 카멜, 파스칼, 케밥 등) 알아두면 좋다

4. 커밋 메시지 관례 역시 알아두자 (feat, fix, chore 등등)

5. 터미널 작업 환경의 경우에는 git conflict에 대처하기 힘든데.. 좋은 방법을 고민해보자
- 아니면 pull request?

6. 잘못된 커밋을 가장 확실하고 깔끔하게 처리하는 방법을 고민해보기 
- 공유된 브랜치는 revert, 개인 브랜치는 reset?

7. git checkout을 통해 방문하지 않아도 git remote/clone 과정에서 원격 레포의 모든 브랜치가 추적되고 있다
- `$git branch --all` 을 통해서 확인이 가능하다

8. 한 번도 가본적 없는 branch에 대해 pull push를 하면 경고 메시지가 뜨는데 이는 터미널에서 제안하는대로 잘 따라가면 오케이

9. 구글링으로 특정 언어에 대한 gitignore를 찾아낼 수 있다
