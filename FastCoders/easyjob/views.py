from django.shortcuts import render, redirect  
from easyjob.forms import EmployeeForm  
from easyjob.models import Employee  
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'company.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  





# Create your views here.
def search(request):#searching
    if request.method == "POST": 
        srch = request.POST['srh']

        if srch:
            match = Employee.objects.filter(Q(cCompanyName__icontains=srch) )


            if match:
                return render(request,'search.html',  {'object_list':match})
            else:
                messages.error(request,'no result found')
               
        else:
            return HttpResponseRedrect('/search/')

    return render(request,'search.html')

def login(request):
    return render(request,'login.html')
def company(request):
    return render(request,'company.html')

def applicant(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'profile.html')

def firstPage(request):
    search = request.GET.get('search', False)
    if search:
        pass
    return render(request,'index.html')

