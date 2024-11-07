# from django.contrib import admin
# from .models import Post,Category,Tag,Comment

# # Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id','category','tag_list','title','description','image','create_date','update_date','like')
#     def tag_list(self, obj): #태그 여러개를 하나의 문자열로 만들어서 리턴
#         return ','.join([t.name for t in obj.tags.all()])
#     def get_queryset(self, request): #ModelAdmin에 있는 get_queryset 오버라이딩
#         return super().get_queryset(request).prefetch_related('tags') #prefetch_related('tags')함수 추가 -> tags 테이블과 join
#         #post의 레코드 하나에서 tag로 참조할 수 있는 값이 여러개 있을 때, 레코드를 통해서 tags를 참조한다면 id마다 tags테이블을 참조해야 한다.(tag가 10개 있다면 10번 참조)
#         #이게 post테이블과 tag테이블이 직접 연결 돼있다면 참조가 빠르지만 보통 그렇지 않음. 사이에 여러개의 테이블이 있고 테이블들을 거쳐서 참조해야 함.
#         #이런 경우 데이터를 참조하는데 너무 많은 리소스가 소모됨. 따라서 tags에서 갖는 값을 미리 join해서 직접 참조할 수 있는 가상의 테이블을 놓고 값을 바로바로 참조할 수 있도록 하는 코드.
#         #좀 어려운 개념임
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id','name','description')

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display=('id','name')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id','post','short_content','create_date','update_date')


from django.contrib import admin
from .models import Post, Category, Tag, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title',
                    'description', 'image', 'create_date','update_date', 'like')
    
    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_date',
                    'update_date')