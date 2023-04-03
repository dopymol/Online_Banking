
from django.shortcuts import render,redirect
from .models import Ways


# Create your views here.
def home(request):
    obj = Ways.objects.all()
    return render(request, 'index.html',{'results':obj})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request,'services.html')

def newpage(request):
    return render(request,'newpage.html')

def formp(request):
    return render(request,'formpage.html')



from .forms import NameForm

def thank(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return redirect('e_bank:thank')
    else:
        form = NameForm()
    return render(request, 'thankyou.html', {'form': form})




