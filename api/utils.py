#views에서 데이터를 가져올 때 사용하는 함수를 모아서 관리하기 위한 모델 파일.

def obj_to_post(obj,flag=True):#obj는 그냥 레코드 형태의 객체로 들어옴
    #가져온 테이터를 Json 형태로 parsing할 수 있도록 데이터를 하나의 긴 문자열 형태로 변경해줘야함.
    post = dict(vars(obj))#obj로 들어오는 속성들을 post dictionary의 Key로 저장하겠다.

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
