
from django.shortcuts import render,redirect
from StudentinfoApp.models import StudentInfo, StudentAcademic
from StudentinfoApp.forms import StudentAcademicFrom, StudentInfoFrom

def studentcreate(request):
    try:
        if request.session["uname"]:
            if request.method == 'POST':
                form = StudentInfoFrom(request.POST)
                aform = StudentAcademicFrom(request.POST)

                if not form.is_valid():
                    return render(request, "student_info.html", {'aform': aform, 'form': form})
                else:
                    form.save()
                    # StudentInfo(roll_no=request.POST['roll_no'],name=request.POST['name'],
                    #             mobile=request.POST['mobile'],sclass=request.POST['sclass'],
                    #             school=request.POST['school'],add=request.POST['address']).save()
                    StudentAcademic(roll_no_id=request.POST['roll_no'], math=request.POST['math'],
                                    physic=request.POST['physic'], biology=request.POST['biology'],
                                    english=request.POST['english'], chemistry=request.POST['chemistry']).save()

            context = {}
            context['form'] = StudentInfoFrom()
            context['aform'] = StudentAcademicFrom()
            return render(request, "student_info.html", context)
        return redirect('login')
    except:
        return redirect('login')



def studentlist(request):
    try:
        if request.session["uname"]:
            data = StudentInfo.objects.all()
            return render(request, "Display.html", {'data': data})
        return redirect('login')
    except:
        return redirect('login')


def studentmark(request):
    try:
        if request.session["uname"]:
            roll_no = request.GET.get('roll_no')
            data = StudentAcademic.objects.filter(roll_no=roll_no)
            return render(request, "studentmark.html", {"data": data})
        return redirect('login')
    except:
        return redirect('login')


def deletestudentdata(request):
    try:
        if request.session["uname"]:
            roll_no = request.GET.get('roll_no')
            StudentInfo.objects.filter(roll_no=roll_no).delete()
            return redirect('studentlist')
        return redirect('login')
    except:
        return redirect('login')


def searchstudent(request):

    namea = request.POST['name']
    data = StudentInfo.objects.filter(name__icontains=namea)
    return render(request, 'Display.html', {'data': data})


def updatepage(request):
    try:
        if request.session["uname"]:
            if request.method == 'POST':
                StudentInfo.objects.filter(roll_no=request.POST['roll_no']).update(
                    name=request.POST["name"], sclass=request.POST["sclass"], school=request.POST["school"],
                    address=request.POST["address"], mobile=request.POST["mobile"]
                )
                StudentAcademic.objects.filter(roll_no__roll_no=request.POST["roll_no"]).update(
                    math=request.POST["math"], physic=request.POST['physic'], chemistry=request.POST["chemistry"],
                    english=request.POST["english"], biology=request.POST["biology"]
                )
                return redirect('studentlist')
            roll_no = request.GET.get('roll_no')
            data = StudentInfo.objects.filter(roll_no=roll_no).values('roll_no', 'name', 'sclass', 'school', 'address',
                                                                      'mobile', 'studentacademic__math',
                                                                      'studentacademic__biology',
                                                                      'studentacademic__chemistry',
                                                                      'studentacademic__english',
                                                                      'studentacademic__physic')
            return render(request, "Studentupdate.html", {"data": data})
        return redirect('login')
    except:
        return redirect('login')



