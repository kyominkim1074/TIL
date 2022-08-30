import sys
from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()
    
class Genre(models.Model):
    title = models.TextField()

1.
Director.objects.create(name='봉준호', debut='1993-01-01', country='KOR')
Director.objects.create(name='김한민', debut='1999-01-01', country='KOR')
Director.objects.create(name='최동훈', debut='2004-01-01', country='KOR')
Director.objects.create(name='이정재', debut='2022-01-01', country='KOR')
Director.objects.create(name='이경규', debut='1992-01-01', country='KOR')
Director.objects.create(name='한재림', debut='2005-01-01', country='KOR')
Director.objects.create(name='Joseph Kosinski', debut='1999-01-01', country='KOR')
Director.objects.create(name='김철수', debut='2022-01-01', country='KOR')

2.
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
    Director.objects.create(name=name_,debut=debut_,country=country_)

1.
genre = Genre()
genre.title = '액션'
genre.save()

genre = Genre()
genre.title = '드라마'
genre.save()

genre = Genre()
genre.title = '사극'
genre.save()

genre = Genre()
genre.title = '범죄'
genre.save()

genre = Genre()
genre.title = '스릴러'
genre.save()

genre = Genre()
genre.title = 'SF'
genre.save()

genre = Genre()
genre.title = '무협'
genre.save()

genre = Genre()
genre.title = '첩보'
genre.save()

genre = Genre()
genre.title = '재난'
genre.save()

2.
genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]
for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

Director.objects.all()

for director in directors:
    print(director.name,director.debut,director.country)



director = Director.objects.get(name='Joseph Kosinski')
director.country = 'USA'
director.save()

Director.objects.get(name='Joseph Kosinski')

Director.objects.get(country='KOR')
## get은 결과가 하나여야 한다. filter를 활용해야 한다.
Director.objects.filter(country='KOR')

director = Director.objects.get(name='김철수')
director.delete()