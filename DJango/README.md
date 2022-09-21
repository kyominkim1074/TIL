# django 개발 환경 설정
## python 설치
django는 웹 서비스를 쉽고 빠르게 개발할 수 있는 툴을 제공하는 프레임워크이다.
django를 이용하기 위해서는 python이 필요하기 때문에 python을 설치할 필요가 있다.

## 터미널 기초 명령어
* cd : 원하는 디렉토리로 이동한다.(change directory)
* ls : 현재 터미널 위치의 디렉토리 경로 확인(list segments)
* pwd : 현재 작업중인 디렉토리 경로 확인(print working directory)
* clear : 터미널 지우기

## 가상환경 설정
일반적으로 프로젝트를 진행하다보면 여러 라이브러리와 패키지를 다운받아야 하고 버전이 다르면
충돌이 일어날 수 있다. 따라서 이런 불편함 없이 독립적인 개발 환경을 설정하기 위해 필요한 것이
가상환경이다.


### 가상환경 생성하기
```bash
$ python -m venv (가상환경명)
즉
$ python -m venv myvenv
```

### 가상환경 사용하기
```bash
$ source (가상환경명)/Scripts/activate
```
아랫줄에 (가상환경명)이 나오면 가상환경에 진입되었음을 의미한다.

### 가상환경에서 빠져나오기
```bash
$ deactivate
```

### 장고 설치
```bash
$ pip install django
# 버전을 지정하려면
$ pip install django==3.2.13
```
가상환경에서 설치하면 글로벌에 설치하지 않는다.

### 장고 제거
```bash
$ pip uninstall django
```

## django 기본
### 프로젝트 생성
```bash
$ django-admin startproject (프로젝트 이름)
```
현재 폴더를 기준으로 프로젝트를 생성한다면
```bash
$ django-admin startproject (프로젝트명) .
```

### 서버 구동
```bash
$ python manage.py runserver
```
이 명령어를 입력하면
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 21, 2022 - 14:51:51
Django version 4.1.1, using settings 'firstpjt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
여기에서 마지막의 두 줄을 보면
서버가 http://127.0.0.1:8000/ 이 주소로 시작되었다는 것과 중지하려면 CTRL-C를 입력하라는 내용이다.
브라우저에 http://127.0.0.1:8000/를 입력하면
[서버](./django_sucess.png)
위 이미지 처럼 나온다.
주소를 http://127.0.0.1:8000/ 대신에 http://localhost:8000/ 라고 입력해도 동일한 결과를 볼 수 있다.
