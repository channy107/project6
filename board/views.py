from django.http import HttpResponse
from django.shortcuts import render

from board.models import Member


def join(request):
    if request.method == 'GET':
        return render(request,
                      'board/join.html',
                      {})
    else:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']

        Member(user_id=user_id,
               user_name=user_name).save()
        return HttpResponse('OK')




def login(request):

    if request.method == "GET":
        return render(request,'board/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        try:
            Member.objects.get(user_id=user_id,
                       user_name=user_name)
        except Member.DoesNotExist:
            return HttpResponse('로그인 실패')

        return HttpResponse('로그인 완료')

import requests

def translate(request):
    if request.method == 'GET':
        return render(request, 'board/translate.html',
                      {})
    else :

        headers = {'Authorization': 'KakaoAK 27cd3e3235427c8b27375ddbb2ebe772' + ''
                   }
        params = {
            'query': request.POST['query'],
            'src_lang':'kr',
            'target_lang': request.POST['target_lang']

        }
        res = requests.get('https://kapi.kakao.com/v1/translation/translate',headers=headers, params=params)

        return HttpResponse(res.text)