### 05_Django_workshop

---

* Django Model Form

  아래 코드들을 참고하여 각 문항에 답하시오

```python
# models.py
class Reservation(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
```



1)  모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm): # 암기법: forms에서 ModelForm은 만들어진다
    
    class Meta: # 암기법 : ModelForm 에 `대한` Data가 필요하다.
        model = Reservation
        filed = '__all__' # "Reservation 모델에 있는 name,date를 모두 form에 담는다." 라는 뜻
```





2) 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.



```python
def create(request):
    if request.method =="POST":
        # form 인스턴스를 생성하고, request에 의한 (POST형식) 데이터로 가득 채운다.
        form = ResevervationForm(request.POST)
        if form.is_vaild:
            resevervation = form.save()
            return redirect('reservations:detail', reseveration.pk)
   else:
   		form = ReservationForm()
        context = {
            'form' : form,
        }
        return render(request,'reservation/create.html',context)
```



* 유효성 검사를 통과하지 못한 form이 return 되지 않는 문제가 발생하였을 것이다. (return할 수 있는 경로가 없으므로,)



* 해결책

  ```python
  # context 스위트를 밖으로 빼준다.
  def create(request):
      if request.method =="POST":
          # form 인스턴스를 생성하고, request에 의한 (POST형식) 데이터로 가득 채운다.
          form = ResevervationForm(request.POST)
          if form.is_vaild:
              resevervation = form.save()
              return redirect('reservations:detail', reseveration.pk)
     else:
     		form = ReservationForm()
          
  
  	context = {
        'form' : form,
       }
  	return render(request,'reservation/create.html',context)
  ```

  

3) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오



```python
def update(request,pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method =='POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
   else:
    form  = ReservationForm(instance=reservation) # 인스턴스를 넣어주는 이유: 인스턴스의 데이터를 이용해서 ModelForm으로 만들어주기 위해.
   context ={
       'reservation' : reservation,
       'form' : form
   }
	return render(request,'reservations/update.html',context)
```





4) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

```django
<h2>edit</h2>
<form action="{% url 'reservations:update' reservation.pk %}" method="POST">
    {% csrf_token %}
    {{form.name}} 
    {{form.date}}
    <input type="submit" value = "submit">
</form>
```

* for문으로도 처리할 수 있다.