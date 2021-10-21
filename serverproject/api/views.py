from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
@csrf_exempt
def test(request):
    if request.method=='POST':
        title=request.data["title"]
        content=request.data['content']
        context = {
            "re_title" : title,
            "re_content":content,
            "msg":"success"
        }
    return JsonResponse(context, status=200)