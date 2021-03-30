from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'vote'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_pk>/<int:answer_pk>/counter/',views.counter,name='counter'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
