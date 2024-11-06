from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from api.utils import obj_to_post,prev_next_post
from blog.models import Post,Category,Tag
from django.views.generic.detail import BaseDetailView
from django.views import View
# Create your views here.


class ApiPostLV(BaseListView):#BaseListView DB에서 레코드 전부 가져오는 클래스
    model = Post
    def render_to_response(self, context, **response_kwargs): #내 데이터 형식에 맞에 오버라이딩. 
        qs = context['object_list'] #context의 object_list key의 value에 모든 레코드들이 저장돼서 들어오는데 그 리스트를 qs에 저장
        postList = [obj_to_post(obj,False) for obj in qs] 
        return JsonResponse(data=postList, safe=False, status=200) #json형식으로 데이터(postList) 전달, 장고에서 json형태의 데이터 전달시 각 속성의 값별로 저장이 돼있는 데이터를 하나의 문자열 느낌으로 바꿔서 전달해야 함. 이때 정상적으로 데이터가 작업이 됐는지 확인하는 과정이 있는데 safe=flase로 하면 이 작업 수행을 안함.
                                                                    #status -> http통신시 200번으로 고정, 장고측에서 response는 끝났기 때문에 200번 쏴주고 연결 종료.
                                                                    #safe -> dictionary형태면 True, 아니면 false 리턴하는 검사 기능이 있는데, 여기서 safe=false 는 그 기능을 끄겠다는 의미


class ApiPostDV(BaseDetailView):#pk값을 사용하지 않았는데 어떻게 특정 레코드를 찾는건지?
                                #BaseDetailView에서 url에 pk로 들어오는 값을 기본적으로 찾아서 테이블에서 검색하는 기능이 있음 신통방통
                                #만약 다른 변수명으로 사용하고 싶다면 pk_url_kwarg 이 속성의 값을 원하는 변수명으로 넣어주면 됨.
    model = Post
    def render_to_response(self,context,**response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        jsonData = {
            'post':post,
            'prevPost':prevPost,
            'nextPost':nextPost,
        }
        return JsonResponse(data = jsonData, safe = True, status=200)
        #json 데이터는 긴 문자열로 이뤄져 있으며 키와 값이 괄호로 묶여서 구분되게 적혀있음. 어떤 데이터를 그러한 형식으로 변환하기 위해서는 변환 시킬 수 있는 형태여야함.
        #파이썬은 json과 형태가 거의 동일한 딕셔너리가 있기 때문에 딕셔너리 형태로 데이터를 가공해서 파라미터로 사용해 주면 됨.
    
class ApiCateTagView(View):#
    def get(self,request,*args,**kwargs):
        qs1 = Category.objects.all()
        qs2 =Tag.objects.all()
        cateList = [cate.name for cate in qs1]
        tagList = [tag.name for tag in qs2]
        jsonData = {
            'cateList':cateList,
            'tagList':tagList,
        }
        return JsonResponse(data=jsonData,safe=True,status=200)


