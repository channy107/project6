from django.http import HttpResponse
from django.shortcuts import render

def join(request):
    if request.method == 'GET':
        return render(request,
                      'board/join.html',
                      {})
    else:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        return HttpResponse('OK')
