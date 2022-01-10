from django.shortcuts import render, redirect

from UserLoginApp.models import User_data
from StudentinfoApp.models import StudentInfo

# Create your views here.
def homepage(request):
    data = StudentInfo.objects.all()
    return render(request, "home.html", {'data': data})


def signupp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pswd = request.POST.get('psw')

        data = User_data(name=name, username=uname, email=email, password=pswd)
        data.save()
        return redirect('login')

    else:
        return render(request, "signup.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        if User_data.objects.filter(username=uname,password=pswd).exists():
            request.session['uname'] = uname
            return redirect('studentlist/')
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def changepassword(request):
    if request.method == 'POST':
        pwd = request.POST.get('pwd')
        npwd = request.POST.get('npwd')
        data = User_data.objects.filter(password=pwd,username=request.session["uname"])
        if data.exists():
            data.update(password=npwd)
            return redirect('login')
        else:
            return render(request, "Changepassword.html", {'error': ' old password not match!'})
    # username = request.GET.get('username')
    # data = User_data.objects.filter(username=username).values('username')
    return render(request, "Changepassword.html",)


def logout(request):
    del request.session["uname"]
    return redirect('home')

'''search and Display all thelink/Url present in the  website '''
import requests
import bs4
from urllib.request import urljoin, urlparse
from bs4 import BeautifulSoup
import lxml

def test(request):
    print("here")
    try:
        if request.method == 'POST':
            links = []
            link = request.POST['link']
            website = requests.get(link)
            soup = bs4.BeautifulSoup(website.text, 'html.parser')

            for i in soup.find_all('a', href=True):
                li = i.get('href')
                if li[0:3] == "../" and li != "#":
                    links.append(link + li[2:len(li)])
                elif li != "#":
                    links.append(li)
            total = (len(links))
            context = {'total': total, 'links': links}
            return render(request, 'link.html', context)
        return render(request, 'link.html')
    except:
        return render(request, 'link.html')



