from django.http import HttpResponse


def index(request):
    return HttpResponse('안녕하세요!! 아 된다!!')


def greeting(request):
    return HttpResponse('반갑습니다.')