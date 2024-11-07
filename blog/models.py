from django.db import models

# Create your models here.
##게시글
class Post(models.Model):
    category = models.ForeignKey('Category',blank=True, null=True,on_delete=models.SET_NULL)  #실제 테이블에서는 한필드에 테이터가 여러개 들어가는게 불가능 하지만 
                                    #이해하기 쉽게 그냥 한 필드에 외래키 형식을 갖는 값을 여러개 갖는다는 의미로 생각하면 될 것 같음.
                                    #지금처럼 1:n의 경우 category에 여러 id값을 갖는다고 생각하면 쉬움
                                    #on_delete=models.SET_NULL 카테고리가 삭제되면 null로 변경. 삭제는 cascade
                                    #'Category' -> 클래스 명을 문자열로 적은 이유는 인터프리터기 때문에 아직 Category가 정의되기 전임. 문자열로 정의 하면 순서에 상관 없이 참조가능.


    tags = models.ManyToManyField('Tag',blank=True) #여기처럼 n:m의 경우 서로 id를 갖는 필드가 존재한다고 이해하면 될 듯
    title = models.CharField('TITLE',max_length=50) #첫번째 파라미터는 테이블에 적용되는 필드명
    description = models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='simple one-line-text.')#simple one-line-text. -> 텍스트 박스 아래 나오는 텍스트문
    image = models.ImageField('IMAGE',upload_to='blog/%Y/%m/',blank=True,null=True) #upload_to='blog/%Y/%m/' ->이미지를 저장하게 되면 위치를 해당 형식으로 저장하겠다.
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField("CREATE DT",auto_now_add=True) #auto_now_add=True 자동으로 값이 들어오는데 초기화 안됨
    update_date = models.DateTimeField("UPDATE DT",auto_now=True) #auto_now=True 값을 초기화 할 수 있음
    like =models.PositiveIntegerField('LIKE',default=0) #PositiveIntegerField -> 자연수 필드
    def __str__(self):
        return self.title #post 객체를 생성했을 때 생성 완료 후 리턴되는 값

##게시글의 종류 지정
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True) #unique=True -> 중복 허용 안함
    description = models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='simple one-line-text.')
    def __str__(self):
        return self.name


##게시글의 태그(해시 태그 기능 구현)
class Tag(models.Model):
    name = models.CharField(max_length=50)
    #작동은 실제 RDB형태로 작동함 가운데 post id와 tag id를 외래키로 갖는 테이블이 하나 더 장고가 만들어 준다고 생각하면 됨.
    def __str__(self):
        return self.name

##댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('CREATE DT',auto_now_add=True)
    update_date = models.DateTimeField('UPDATE DT',auto_now=True)

    @property
    def short_content(self): #처음 리턴할 때 속성의 값의 처음 10글자만.
        return self.content[:10]
    
    def __str__(self): #문자열 반환해야 함.
        return self.short_content
