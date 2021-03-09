from django.shortcuts import render

# Create your views here.
#여기를 menu ='default' / pepole = 10 이런식으로 기본값을 설정해줘서 기본적으로 이런 값을 반환할 수 도 이싿.
def dinner(request,menu='pizza',people=10):
    context ={
        'menu' : menu,
        'people' : people,
    }
    return render(request,'dinner/dinner.html',context)