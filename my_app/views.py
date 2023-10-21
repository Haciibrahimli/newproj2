from django.shortcuts import render
from my_app.models import Category,Author,Keywords
# Create your views here.

def index_view(request):
    my_datas = Category.objects.all()
    my_obj = Author.objects.all()
    my_obj1 = Keywords.objects.all()
    context = {
               
    'my_datas': my_datas,
    'my_obj':my_obj,
    'my_obj1':my_obj1 

    }
    return render(request,'index.html',context)

