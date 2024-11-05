from django.views.generic import TemplateView

class HomeView(TemplateView): #TemplateView url로 호출했을 때 여러 경우를 리턴할 수 있는 뷰 클래스.
    #as_view() -> url에서 확인 가능. 클래스에 있는 모든 함수를 실행해 주는 함수
    #그동안과 다른 클래스 뷰
    #클래스 뷰 -> 더 큰 프로젝트에 유용. 확장성 및 재사용이 좋고, 복잡한 로직이 필요한 경우 유용함.
    template_name = 'myindex.html'