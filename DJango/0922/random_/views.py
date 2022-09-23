from multiprocessing import context
from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, "index.html")

def dinner(request):
    dinner_list = [
        {"name" : '삼겹살', 'src':'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg'},
        {"name" : '마라탕', 'src':'https://upload.wikimedia.org/wikipedia/commons/3/3b/Malatang_from_South_Korea.jpg'},
        {"name" : '스파게티', 'src':'https://w.namu.la/s/41f33b159c88d0472e7c726a2c0ed7cbb159ba541fa2acfd4ae63f40c9c15fcfd55f80533780d15aa09a47bfed32e09b4b8bfe9ac68f2e5d63586277df859121358d3d9d1c9f654f09bc026565710f7357c09bb5a539b85e3b3447bdf37b576ff2202836ecd744fd8ccb55fbd9a5d305'}
    ]
    context = {
        'dinner' : random.choice(dinner_list)
    }
    return render(request, "today_dinner.html", context)

def lotto(request):
    lotto_list=[]
    
    for _ in range(5):
        lotto = random.sample(range(1, 46),6)
        lotto_list.append(lotto)
    context = {
        "lotto_list": lotto_list,
    }
    return render(request, 'lotto.html', context)