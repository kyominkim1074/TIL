# Django CRUD

## 가상환경 / 장고 설치

1. 가상환경 생성하고 실행해보기
```bash
$ python -m venv venv
$ source venv/Scripts/activate

(venv)
$
```
<!-- (가상환경 실행 종료) -->
```bash
$ deactivate
```

2. 장고 설치 / 기록(requirements.txt)
```bash
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

3. 프로젝트 생성하기
```bash
$ django-admin startproject pjt
```
<!-- manage 파일을 프로젝트 폴더가 아니라 현재 파일에 생성시킬 경우 -->
```bash
$ django-admin startproject pjt .
```

## 앱
1. 앱 생성
```bash
python manage.py startapp articles
```

2. 앱 등록
프로젝트 폴더의 settings.py에서 INSTALLED_APPS에 앱 이름을 추가한다.

3. urls.py 설정
프로젝트 폴더의 urls.py에서
상단에 import path부분에 콤마를 넣어주고 그 뒤에 include를 추가시킨다.
그리고, urlpatterns에
```python
path('articles/', include('articles.urls')),
```
위 내용을 추가시킨다.
include는 좀 더 효율적으로 url을 등록하고 관리해주는 함수인데
위의 내용은 articles/로 시작하는 모든 url은 앱 내의 urls.py에서 관리한다는 의미이다.
그 다음, 앱 폴더에 urls를 생성한다.

## Model 정의

1. class 정의
```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
db를 구상해 본 걸 토대로 class를 정의해준다.

2. 마이그레이션 파일 생성
마이그레이션은 모델 변경 내역을 스키마에 적용시키는 방법이다.
models.py의 클래스를 통해 db 스키마를 생성하고 컨트롤을 하는데
git처럼 비슷하게 db 스키마를 버전으로 나눠서 관리 할 수 있게 해준다.

```bash
$ python manage.py makemigrations [app_name]
```

3. db 반영['migrate']
```bash
$ python manage.py migrate
```
위 명령어에서 뒤에 앱 이름을 지정하면 특정 앱만 반영이 되고,
앱 이름 뒤에 마이그레이션 파일 이름을 지정하면 파일 이름의 숫자(버전)의 마이그레이션이 적용된다.
즉, 버전을 낮추는 것도 가능하다.

## CRUD 구현
### 1. read 구현
1. 객체의 목록 보여주기
http://127.0.0.1:8000/articles/
2. 각 객체의 상세 페이지
http://127.0.0.1:8000/articles/pk/
detail 페이지의 경우 index와는 다르게
매개변수에 pk를 넣어주고 pk에 맞는 객체의 데이터를 불러와
보여준다는 것이다.
### 2. create 구현
1. 게시글을 작성하는 페이지(new)
http://127.0.0.1:8000/articles/new/
2. 작성한 데이터를 저장하는 기능(create)
http://127.0.0.1:8000/articles/create/
데이터를 저장하고 index에 redirect

### 3. update 구현
create와 유사하며 기존의 데이터를 불러와 덮어씌운다.
따라서 views에서 request뿐만 아니라 pk도 전달해야 한다.
1. 기존의 데이터 불러오기(detail)
특정 글을 볼 수 있는 페이지
http://127.0.0.1:8000/articles/pk/
2. 새로운 데이터로 갱신/저장(update)
http://127.0.0.1:8000/articles/pk/update/

### 4. delete 구현
기존의 객체의 pk를 불러와 삭제한 후에
index로 redirect시킨다.
http://127.0.0.1:8000/articles/pk/delete/