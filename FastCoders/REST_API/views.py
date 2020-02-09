from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from easyjob.models import Company
import json

# method to view records, and add records
@csrf_exempt
def view_get_post_company(request):
# To view records from GET
    if request.method == "GET":
        company = Company.objects.all()
        list_of_company = list(company.values("id","cCompanyName","cVacantPost","cVacancyNumber","cEmail","cMobile","cLocation"))
        dictionary_name = {
        "company":list_of_company
    }
        return JsonResponse(dictionary_name)
# To add records from POST 
    elif request.method == "POST":
        python_dictionary_object = json.loads(request.body)
        get_cCompanyName=python_dictionary_object['cCompanyName']
        get_cVacantPost=python_dictionary_object['cVacantPost']
        get_cVacancyNumber=python_dictionary_object['cVacancyNumber']
        get_cEmail=python_dictionary_object['cEmail']
        get_cMobile=python_dictionary_object['cMobile']
        get_cLocation=python_dictionary_object['cLocation']
        company_object = Company(cCompanyName=get_cCompanyName,cVacantPost=get_cVacantPost,cVacancyNumber=get_cVacancyNumber,cEmail=get_cEmail,cMobile=get_cMobile,cLocation=get_cLocation)
        company_object.save()
    
        return JsonResponse({
            "message":"Successfully posted!!"
        })
# for other API method
    else:
        return HttpResponse("Other HTTP verbs are not describe in views")

# method to view record, update record, and delete record by id 
@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
# To read single record using GET through id
    if request.method == "GET":
        company_object = Company.objects.get(id = ID)
        print(type(company_object.cCompanyName))
        return JsonResponse({
            "id":company_object.id,
            "cCompanyName":company_object.cCompanyName,
            "cVacantPost":company_object.cVacantPost,
            "cVacancyNumber":company_object.cVacancyNumber,
            "cEmail":company_object.cEmail,
            "cMobile":company_object.cMobile,
            "cLocation":company_object.cLocation
        })

#To update records using PUT
    elif request.method=="PUT":
        company_object = Company.objects.get(id = ID)
        python_dictionary_object = json.loads(request.body)
        company_object.cCompanyName=python_dictionary_object['cCompanyName']
        company_object.cVacantPost=python_dictionary_object['cVacantPost']
        company_object.cVacancyNumber=python_dictionary_object['cVacancyNumber']
        company_object.cEmail=python_dictionary_object['cEmail']
        company_object.cMobile=python_dictionary_object['cMobile']
        company_object.cLocation=python_dictionary_object['cLocation']
        company_object.save()
        return JsonResponse({
        "message":" update successfully"
        })

# To delete records using DELETE
    elif request.method == "DELETE":
        company_object = Company.objects.get(id = ID)
        company_object.delete()
        return JsonResponse({
        "message":" Deleted successfully"
        })
# for other API method
    else:
        return HttpResponse("Other HTTP verbs are not describe in views")


   