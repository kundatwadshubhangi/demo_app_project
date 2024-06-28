import datetime
from django.http import HttpResponse
from django.shortcuts import render





# Create your views here.
def area(request,side):
    diff1=side*side
    diff=4*side
    #return HttpResponse("<h1> area of square = %s" %(diff1),"<br> perimeter of square = %s</h1>"%(diff))
    return HttpResponse("<p>Area of a square = %d sq cms<br>""Perimeter of a square = %d cms</p>"%(diff1,diff))
#define a function to find parameter of square

    
    
# define a function for check if a person can vote from home or not
def votefromhome(request,age):
    if age>=60:
        diff=age-60
        return HttpResponse("<h1> you can vote from home as you are %s years above limit"%(diff))
    else:
        diff=60-age
        return HttpResponse("<h1> you cannot vote from home as you are %s years below limit"%(diff))

# definen a function for display date and time 45 min ahead 
       

def timeanddate(request):
    currenttime24=datetime.datetime.now()
    ahead45min=currenttime24+datetime.timedelta(hours=1-1/4)
    result="<h2>time now in 24 hr format is %s<br>time 45 min ahead will be %s"%(currenttime24,ahead45min)
    return HttpResponse(result)   



def view(request):
    currenttime24=datetime.datetime.now()
    ahead45min=currenttime24+datetime.timedelta(hours=1-1/4)
    return render(request,'home.html',{'currenttime24':currenttime24,'ahead45min':ahead45min})
