#views.py
from django.shortcuts import render, redirect  
from memberlist.forms import MemberForm
from memberlist.models import Member
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = MemberForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = MemberForm()
    return render(request,'index.html',{'form':form})  
def index(request):  
    employees = Member.objects.all()
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Member.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Member.objects.get(id=id)
    form = MemberForm(request.POST, instance = employee)
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Member.objects.get(id=id)
    employee.delete()  
    return redirect("/")  