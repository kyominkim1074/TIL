* [HTML](./HTML)
> [0920](./HTML/0920)
>> [로또](./HTML/0920/lotto.html)

* [BOJ 문제풀이](./BOJ)

* [SWEA_문제풀이](./SWEA)

* [Python_문제풀이](./python/)

* [codeup_문제_풀이](./codeup/)

* [git의 branch와 github의 flow](./0707.md)

## MARKDOWN

## 2022/07/05 마크다운, git 기초 부분

| 마크타운 문법 정리       | [마크다운_정리](./마크다운_정리.md)         |
| ---------------- | ------------------------------- |
| 마크다운 실습          | [실습](./Markdown_실습.md)          |
| git 커맨드 기록한 텍스트  | (git commanders.txt파일에 기록되어 있음) |
| git 파일 생성부터 커밋까지 | [git_status](./git_status.md)   |

## 2022/07/06 git-github

### github 원격 저장소를 생성하는 과정

- github에서 New Repositiory 클릭

- 저장소 설정하기 (가급적 공개로 설정)

- 완성되었는지 확인해보기

- 원격 저장소 정보를 로컬 저장소에 추가
  
  - $ git remote add (원격저장소이름) (url)
* $ git remote -v를 입력해 정보 확인

* ### $ git push (원격저장소이름) (브랜치이름[보통 master]) 를 입력
  
  - 원격 저장소로 로컬 저장소에 기록된 커밋을 업로드
  
  - #### 파일이나 폴더가 업로드 되는 것이 아니다!
- push했을 경우에는 인증 정보를 하게 됨
  
  - windows의 경우에는 브라우저를 통해 인증을 한다.
  - Authentication failed 메세지가 뜰 경우 자격증명관리자에서 확인

- $ git pull
  
  - push와는 반대로 원격에서 로컬로 커밋을 받아와서 병합을 한다.

## 원격저장소 기본 명령어

| 명령어                       | 내용                       |
|:-------------------------:|:------------------------:|
| git clone (url)           | 원격 저장소 복제                |
| git remote -v             | 원격 저장소 정보 확인             |
| git remote add (원격) (url) | 원격 저장소 추가 (일반적으로 origin) |
| git remote rm (원격)        | 원격 저장소                   |
| git push (원격) (브랜치)       | 원격 저장소에 커밋 업로드           |
| git pull (원격) (브랜치)       | 원격 저장소로부터 커밋을 받아옴        |

## push 실패하는 경우

- 보통 로컬과 원격의 커밋 이력이 다른 경우에 발생된다.
- $ git pull을 입력해서 원격의 커밋을 가져온다.
- 로컬에서 두 커밋을 병합시킨다.
- 다시 github로 push를 한다.

## 버전관리를 별도로 사용하지 않는 파일이 있는 경우

- git 저장소에 .gitignore 파일을 생성한다.

- 예를 들어
  
  - 특정 파일 : .txt 등등
  - 특정 디렉토리 : /secret
  - 특정 확장자 : .exe
  - 예외 처리 : !b.exe

- ### (**이미 커밋된 파일은 반드시 삭제를 해야 적용이 된다.**)
  
  - #### 반드시 프로젝트 시작전에 미리 설정해 놓기

- .gitignore 참고 사이트
  
  - [.gitignore](https://gitignore.io)
