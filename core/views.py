# import sys
# sys.path.insert(0, '/Volumes/For Me/django/core/services/')
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import calculator
from .forms import userForms
from .forms import evenod
from .forms import sheet
from services.models import titles
from roast.models import News
from board_form.models import Result

var=userForms()
edu = evenod()
cal=calculator()
sh=sheet()

def homePage(request):
    title_data=titles.objects.all()
    title_paginator=Paginator(title_data,3)
    page_number=request.GET.get('page')
    title_data_final_paginator=title_paginator.get_page(page_number)
    page_numbers=title_data_final_paginator.paginator.num_pages
    print(page_numbers)
    if request.method == 'POST':
        va=request.POST.get('search_title')
        if va != None:
            title_data=titles.objects.filter(main_title__icontains=va)
    newsData=News.objects.all()
    
    opdata={
        'titles':title_data_final_paginator,
        'new':newsData,
        'title_data':title_data,
        "actual_numbers":page_numbers,
        "total_numbers":[n+1 for n in range(page_numbers)]
        
    }
    for i in newsData:
        print(i.news_title)
    return render(request,"index.html",opdata)
def about_us(request):
    return render(request,"about.html")
def contact(request):
    meta = {'form': var}
    if request.method == "GET":
        output=request.GET.get('output')
    try:
        if request.method == "POST":
            num1=request.POST.get('num1')
            num2=request.POST.get('num2')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            print({{num1}}," ",{{num2}}, " ",phone, " ",message)
            meta={
                "form":var,
                "output": output
            }
    except:
        pass
    return render(request,"contact.html", meta)
def service(request):
    return render(request,"services.html")
def shop(request):
    return render(request,"shop.html")
def contact_data(request): #This is action function of form
    final_value=0

    data={}
    try:
        if request.method == "POST":
            full_name=request.POST.get('num1')
            email=request.POST.get('num2')
            age=request.POST.get('phone')
            message=request.POST.get('message')
            print(full_name, " ",age," ",message)
            final_value=f"My name is {full_name}, my email address is {email} ,and my message is {message}"
            print(final_value)
            data={

                "full_name":full_name,
                "email":email,
                "age":age,
                "output":final_value
            }
            print(data)
            url="/contact/?output={}".format(full_name,email,age)
            return HttpResponseRedirect(url)
    except:
        pass
def form_data(request): #This is action function of form
    final_value=0

    data={}
    try:
        if request.method == "POST":
            full_name=request.POST.get('full_name')
            email=request.POST.get('email')
            age=request.POST.get('age')
            print(full_name, " ",email," ",age)
            final_value=f"My name is {full_name}, my email address is {email} ,and my age is {age}"
            print(final_value)
            data={

                "full_name":full_name,
                "email":email,
                "age":age,
                "output":final_value
            }
            print(data)
            url="/contact/?output={}".format(full_name,email,age)
            return HttpResponseRedirect(url)
    except:
        pass
def form(request):
    #This is actual function of form
    return render(request,"form.html")
def calculator(request):
    defa={'fifa':cal}
    try:
        if request.method == "POST":
            value1=request.POST.get('value1')
            value2=request.POST.get('value2')
            opera=request.POST.get('operator')
            value1=int(value1)
            value2=int(value2)

            if opera == "+" :
                r_value=value1+value2
                print(r_value)
            elif opera == "-":
                r_value=value1-value2
                print(r_value)
            elif opera == "*":
                r_value=value1*value2
                print(r_value)
            elif opera == "/":
                r_value=value1/value2
                print(r_value)
            defa={
                'out':r_value,
                'fifa':cal
            }
    except:
        pass
    return render(request,"calculator.html",defa)
def evenodd(request):
    outpot=''
    edata={'pot':edu}
    try:
        if request.method == "POST":
            val=int(request.POST.get('evenodd'))
            print(val)
            if val%2 == 0 :
                outpot='Even'
            else:
                outpot="Odd"
            edata={
                'pot': edu,
                'final_data':outpot

            }
    except:
        pass
    return render(request,"evenodd.html",edata)
def sheet(request):
    sdata={'sho':sh}
    try:
        if request.method == "POST":
            maths=int(request.POST.get('maths'))
            eng=int(request.POST.get('eng'))
            urdu=int(request.POST.get('urdu'))
            phy=int(request.POST.get('phy'))
            chy=int(request.POST.get('chy'))
            biy=int(request.POST.get('biy'))
            ist=int(request.POST.get('ist'))
            ps=int(request.POST.get('ps'))
            image_selection=request.POST.get('image_selection')
            final=maths+eng+urdu+phy+chy+biy+ist+ps
            print("Total marks are:",final)
            percentage=final * 100 / 505
            print(percentage)
            if percentage>80:
                d="First Division"
            elif percentage > 65:
                d="Second Division"
            elif percentage > 35:
                d="Third Division"
            else:
                d = "Fail"
            for_save=Result(maths=maths,eng=eng,urdu=urdu,phy=phy,chy=chy,biy=biy,ist=ist,ps=ps,division=d,percentage=percentage,total_numbers=final,image_selection=image_selection)
            for_save.save()
            sdata={
                'p':percentage,
                'sho':sh,
                'full':final,
                'd':d
            }
    except:
        pass
    return render(request,"sheet.html",sdata)
def newsDetails(request,slug):
    news_data=News.objects.get(news_slug=slug)
    news_d={
        'news_data':news_data
    }
    return render(request,"newsletter.html",news_d)