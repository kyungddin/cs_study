# git
git 관련해서 공부한 거 기록하기


## Local Env
- 각 환경별 물리적 파일 저장
    - 워킹 디렉토리 → .git 바깥 (실제 파일들)
    - 스테이징 에리어 (index) → .git/index 파일
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