from django.shortcuts import render, redirect  
from easyjob.forms import CompanyForm  
from easyjob.models import Company  
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib import messages

# create Records   
def create_Records(request):  
    if request.method == "POST":  
        form = CompanyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CompanyForm()  
    return render(request,'company.html',{'form':form})


# Read Records  
def show_Records(request):  
    employer = Company.objects.all()  
    return render(request,"show.html",{'employer':employer})


# Edit Records  
def edit_Records(request, id):  
    employer = Company.objects.get(id=id)  
    return render(request,'edit.html', {'employer':employer})


# update Records  
def update_Records(request, id):  
    employer = Company.objects.get(id=id)  
    form = CompanyForm(request.POST, instance = employer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employer': employer})


# Delete Records  
def destroy_Records(request, id):  
    employer = Company.objects.get(id=id)  
    employer.delete()  
    return redirect("/show")  





# Search Records
def search(request):
    if request.method == "POST": 
        srch = request.POST['srh']

        if srch:
            match = Company.objects.filter(Q(cCompanyName__icontains=srch)|Q(cEmail__icontains=srch)|Q(cVacantPost__icontains=srch)|Q(cMobile__icontains=srch))


            if match:
                return render(request,'search.html',  {'object_list':match})
            else:
                 messages.error(request,'no result found')
               
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'search.html')

# for Login
def login(request):
    return render(request,'login.html')

# Show company.html page
def company(request):
    return render(request,'company.html')

# upload files
def applicant(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'profile.html')

# Search Records
def firstPage(request):
    search = request.GET.get('search', False)
    if search:
        pass
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')