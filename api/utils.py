#views에서 데이터를 가져올 때 사용하는 함수를 모아서 관리하기 위한 모델 파일.

def obj_to_post(obj,flag=True):#obj는 그냥 레코드 형태의 객체로 들어옴
    #가져온 테이터를 Json 형태로 parsing할 수 있도록 데이터를 하나의 긴 문자열 형태로 변경해줘야함.
    post = dict(vars(obj))#obj로 들어오는 속성들을 post dictionary의 Key로 저장하겠다.
                          #여기서 값은 실제 값처럼 문자열 같은게 들어있는게 아닌 값을 참조할 수 있는 형태로 들어있음 obj.category 그냥 이런식으로
                          #이걸 json은 해독할 방법이 없음. 그래서 속성에 해당하는 값을 직접 참조해서 넣어주는 작업을 하는거임

    if obj.category:#속성이 있으면 
        post['category'] = obj.category.name #obj에 레코드 객체를 받을 때 해당 객체에는 연결돼있는 다른 레코드의 데이터도 함께 받아지는건지?
    else:
        post['category'] = "NoCategory"

    if obj.tags: 
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = "https://via.placeholder.com/900x300/"
    
    if obj.update_date: 
        post['update_date'] = obj.update_date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_date'] = '9999-12-31 00:00:00'
    
    del post['_state'],post['category_id'],post['create_date'] #레코드를 객체로 가져오면 레코드에 연결돼있는 다른 테이블의 데이터도 함께 모두 가져오는데
                                                               #그때 같이 가져와진 데이터의 속성들은 안쓰기 때문에 지워줌

    if not flag:
        del post['tags'],post['update_date'],post['description'],post['content']
    
    return post


def prev_next_post(obj):
    try:
        prevObj = obj.get_previous_by_update_date() #get_previous_by -> 지금 받은 레코드의 이전 레코드를 가져올 수 있음.by_update() -> 업데이트된 날짜순
        prevDict = {
            'id' : prevObj.id,
            'title' : prevObj.title,
        }
    except obj.DoesNotExist: #레코드에 내장돼있는 예외문. prevObj = obj.get_previous_by_update() -> 이게 오류가 발생했을 때 예외문 실행이기 때문에 이전 데이터가 없다는 것임.
        prevDict = {}
    
    try:
        nextObj = obj.get_next_by_update_date() 
        nextDict = {
            'id' : nextObj.id,
            'title' : nextObj.title,
        }
    except obj.DoesNotExist: #레코드에 내장돼있는 예외문. 
        nextDict = {}
    
    return prevDict,nextDict


def obj_to_comment(obj):
    comment = dict(vars(obj))
    if obj.update_date:
        comment['update_date'] = obj.update_date.strftime('%Y-%m-%d %H:%M:%S')
    else :
        comment['update_date'] = "9999-12-31 00:00:00"
    
    del comment['_state'],comment['post_id'],comment['create_date']
        #comment['_state'] -> foreign key를 통한 참조로 가져올 경우 가져와지는 속성. 필요없어서 삭제

    return comment
