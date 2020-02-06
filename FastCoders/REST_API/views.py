from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from easyjob.models import Company
import json

@csrf_exempt
def view_get_post_airport(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        company = Company.objects.all()
        print("QuerySet objects => ",company)
        list_of_company = list(company.values("cCompanyName","cVacantPost"))
        print("List of Company objects => ",list_of_company)
        dictionary_name = {
        "company":list_of_company
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['cCompanyName'])
        print(python_dictionary_object['cVacantPost'])
        Company.objects.create(cCompanyName=python_dictionary_object['cCompanyName'],cVacantPost=python_dictionary_object['cVacantPost'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        com = Company.objects.get(id = ID)
        print(type(com.cCompanyName))
        return JsonResponse({
            "id":com.id,
            "cCompanyName":com.cCompanyName,
            "cVacantPost":com.cVacantPost
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })