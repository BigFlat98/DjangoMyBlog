from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from api.utils import obj_to_post
from blog.models import Post
# Create your views here.


class ApiPostLV(BaseListView):#BaseListView DB에서 레코드 가져오는 클래스
    model = Post
    def render_to_response(self, context, **response_kwargs): #내 데이터 형식에 맞에 오버라이딩. 
        qs = context['object_list']
        postList = [obj_to_post(obj,False) for obj in qs] 
        return JsonResponse(data=postList, safe=False, status=200) #json형식으로 데이터(postList) 전달, 장고에서 json형태의 데이터 전달시 각 속성의 값별로 저장이 돼있는 데이터를 하나의 문자열 느낌으로 바꿔서 전달해야 함. 이때 정상적으로 데이터가 작업이 됐는지 확인하는 과정이 있는데 safe=flase로 하면 이 작업 수행을 안함.
                                                                    #status -> http통신시 200번으로 고정, 장고측에서 response는 끝났기 때문에 200번 쏴주고 연결 종료.
    