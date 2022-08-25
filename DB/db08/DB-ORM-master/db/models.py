from tkinter.tix import Tree
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()
    
    
    
Director.objects.create(name='봉준호', debut='1993-01-01', country='KOR')
Director.objects.create(name='김한민', debut='1999-01-01', country='KOR')
Director.objects.create(name='최동훈', debut='2004-01-01', country='KOR')
Director.objects.create(name='이정재', debut='2022-01-01', country='KOR')
Director.objects.create(name='이경규', debut='1992-01-01', country='KOR')
Director.objects.create(name='한재림', debut='2005-01-01', country='KOR')
Director.objects.create(name='Joseph Kosinski', debut='1999-01-01', country='KOR')
Director.objects.create(name='김철수', debut='2022-01-01', country='KOR')

directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()
    
genre = Genre()
genre.title = '재난'
genre.save()


director = Director.objects.get(name='봉준호')
print(director.id, director.name, director.debut, director.country)

genre = Genre.objects.get(title='드라마')
print(genre.id, genre.title)

director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date = '2019-05-30'
movie.running_time = 132
movie.screening = False

movie.save()

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movie in movies:
    director_name = movie[0]
    genre_title = movie[1]
    title_ = movie[2]
    opening_date_ = movie[3]
    running_time_ = movie[4]
    screening_ = movie[5]
    
    director_ = Director.objects.get(name=director_name)
    genre_ = Genre.objects.get(title=genre_title)
    
    movie_ = Movie()
    movie_.director = director_
    movie_.genre = genre_
    movie_.title = title_
    movie_.opening_date = opening_date_
    movie_.running_time = running_time_
    movie_.screening = screening_
    movie_.save()

movies = Movie.objects.all()

for movie in movies:
    print(
        movie.director,
        movie.genre,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )


movies = Movie.objects.all()

for movie in movies:
    print(
        movie.director.name,
        movie.genre,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

movies = Movie.objects.all()

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

movies = Movie.objects.order_by('-opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

movies = Movie.objects.order_by('opening_date')[0]
print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
)

movies = Movie.objects.filter(screening=True).order_by('opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

director_ = Director.objects.get(name='봉준호')
movies = Movie.objects.filter(director=director_).order_by('opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

director_ = Director.objects.get(name='봉준호')
movies = Movie.objects.filter(director=director_).order_by('opening_date')[1]
print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
)

movies = Movie.objects.filter(running_time__gt=119).order_by('running_time')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

movies = Movie.objects.filter(running_time__gte=119).order_by('running_time')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

movies = Movie.objects.filter(opening_date__gte='2022-01-01').order_by('opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )


director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')
movies = Movie.objects.filter(director=director_, genre=genre_).order_by('opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )

director_ = Director.objects.get(name='봉준호')
movies = Movie.objects.exclude(director=director_).order_by('opening_date')

for movie in movies:
    print(
        movie.director.name,
        movie.genre.title,
        movie.title,
        movie.opening_date,
        movie.running_time,
        movie.screening
    )