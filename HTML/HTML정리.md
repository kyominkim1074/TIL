# HTML:HyperText Markup Language

## HTML??

HTML(HyperText Markup Language)는 웹을 이루는 가장 기초적은 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 상요한다. HTML 이외의 다른 기술은 일반적으로 웹페이지의 모양/표현(CSS), 또는 기능/동작(JavaScript)을 설명하는 데 사용된다.

"Hypertext(하이퍼텍스트)" : 웹페이지를 다른 페이지로 연결하는 링크

#### Markup

HTML은 웹 브라우저에 표시되는 글과 이미지 등의 콘텐츠르 표시하기 위해 markup을 사용하는데, markup은 다양한 요소를 사용한다.

    요소에는

```html
<head>, <title>, <body>, <header>, <footer>, <article>, <section>,
<p>, <div>, <span>, <img>, <aside>, <audio>, <canvas>, <datalist>,
<details>, <embed>, <nav>, <outpit>, <progress>, <video>, <ul>, <ol>, <li>
```

등등 많은 종류가 있다.

HTML 요소는 "태그"를 사용해서 문서의 다른 텍스트와 구분한다. 태그는 <태그 이름>으로 이루어진다. 그리고 대소문자를 구분하지 않아 대문자와 소문자를 섞어서도 작성이 가능하다.

# HTML 기본

## HTML??

HTML은 컨텐츠의 서로 다른 부분들을 씌우거나 감싸서 다른 형식으로 보이게 하거나 특정한 방식으로 동작하도록 하는 일련의 "요소"오 이루어져 있다. 태그로 감싸는 것으로 단어나 이미지를 다른 주소로 하이퍼링크(hyperlink)하거나 단어들을 이탤릭체로 표시하고 글씨체를 크게 또는 작게 만드는 등의 일을 할 수 있다.

### 예)

```html
Microsoft Windows
```

예의 한 줄의 문장이 독립적인 구문이길 원하는 경우에 문단 태그를 이용해 하나의 문단임을 명시할 수 있다.

```html
<p>Microsoft Windows</p>
```

## HTML 요소(element)

1. 여는 태그(opening tag) : 요소의 이름으로 구성되고 여닫는 꺾쇠괄호로 감싸진다.(<>) 여는 태그는 요소가 시작되는 곳, 또는 효과를 시작하는 곳이다.

2. 닫는 태그(closing tag) : 여는 태그와 비슷하지만, 이름 앞에 슬래시(/)가 포함되어야 한다. 요소의 끝을 나타낸다.

3. 컨텐츠(content) : 요소의 내용

4. 요소(element) : 요소는 여는 태그와 닫는 태그, 컨텐츠로 이루어 진다.

### 요소는 속성도 가질 수 있다.

속성이 항상 가져야 하는것:

1. 요소이름(또는 요소가 하나 이상 속성을 이미 가지고 있다면 이전 속성)과 속성 사이에 공백이 있어야 한다.

2. 속성 이름 뒤에는 등호(=)가 있어야 한다.

3. 속성 값의 앞 뒤에 열고 닫는 인용부호(따옴표)가 있어야 한다.

## 요소 중첩

요소를 다른 요소의 안에 놓을 수 있는데, 이걸 중첨(nesting)이라고 한다.

### 예)

```html
<p>Microsoft <strong>Windows</strong> 10 Home Edition</p>
```

#### 잘못된 경우

```html
<p>Microsoft <strong>Windows 10 Home Edition</p></strong>
```

## 빈 요소(empty elements)

요소들 중에 내용을 갖지 않는 요소를 말한다. (예. img)

```html
<img src="images/firefox-icon.png" alt="My test image">
```

두개의 요소를 포함하고 있지만 닫는 태그가 없는데 이미지는 효과를 주기 위해 컨텐츠를 감싸지 않기 때문이다. 목적은 HTML 페이지에서 이미지가 나타날 위치에 이미지를 끼워 넣는 것이다.

## HTML 문서

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>My test page</title>
    </head>
    <body>
        <img src="images/firefox-icon.png" alt="My test image">
    </body>
</html>
```

* DOCTYPE : HTML문서에서 <html>태그를 정의하기 전에 먼저 선언되어야 한다.
  HTML태그는 아니지만 선언된 페이지의 HTML버전이 무엇인지를 브라우저에 알려주는 역할을 한다. 대소문자 구분하지 않는다.

* <html></html> : 페이지 전체를 감싸며, 루트 요소라고도 한다.

* <head></head> : HTML 페이지에 포함되어 있는 모든 것들의 컨테이너 역할을 한다.
  (keywords)와 검색 결과에 표시되길 원하는 페이지 설명, 컨텐츠를 꾸미기 위한 CSS, 문자 집합 선언 등과 같은 것들이 포함된다.

* (<head></head>) : 페이지에 방문한 모든 웹 사용자들에게 보여주길 원하는 모든 컨텐츠를 담고 있으며, 텍스트, 이미지, 비디오, 게임, 플레이할 수 있는 오디오 트랙이나 다른 무엇이든 될 수 있다.

* (<meta charset-"utf-8">) : 문서가 사용해야 할 문자 집합을 utf-8로 설정한다. 

* (<title></title>) : 페이지의 제목을 설정하는 것으로 페이지가 로드되는 브라우저의 탭에 표시된다. 북마크나 즐겨찾기에서 페이지를 설명하는 것으로도 사용된다.

## 이미지

```html
<img src="images/firefox-icon.png" alt="My test image">
```

이미지 요소는 이미지가 나타나야 할 위치에 이미지를 끼워 넣는다. 이미지 파일의 경로를 포함하는 src속성을 이용한다.

alt속성은 다음과 같은 이유로 이미지를 볼 수 없는 유저들을 위한 설명문을 지정할 수 있다.

1. 시각 장애인의 경우. 시각장애가 심한 사용자들은 alt 텍스트(대체 택스트)를 읽어주는 스크린 리더라는 도구를 자주 사용한다.

2. 무언가 잘못되어서 이미지를 표시할 수 없는 경우. 예를 들어 src속성 안의 경로가 맞지 않는 경우

## 문자 나타내기

### 제목

HTML은 여섯 단계의 제목을 갖고, <h1>에서 <h6>으로 표현한다.

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

## 문단

<p>요소는 문자의 문단을 포함하기 위해 사용한다.

```html
<p>Microsoft Windows 10</p>
```

## 목록(list)

1. 순서 없는 목록 : 항목의 순서에 관계가 없는 목록 <ul>요소

2. 순서 있는 목록 : 항목의 순서가 중요한 목록을 위해 사용한다. <ol> 요소

목록의 각 항목은 <li>(목록 항목) 요소 안에 작성해야 한다.

```html
<p>At Mozilla, we're a global community of technologists, thinkers,
and builders working together...</p>
```

```html
<p>At Mozilla, we're a global community of</p>


<ul>
    <li>technologists</li>
    <li>thinkers</li>
    <li>builders</li>
</ul>

<p>working together...</p>
```

# 연결(anchor)

문장 안의 어떤 단어를 링크로 만들기 위해 사용하는 요소이다.<a>

```html
<a href="https://www.microsoft.com/ko-kr/windows/">Microsoft Windows 10</a>
```
