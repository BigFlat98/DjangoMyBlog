#views에서 데이터를 가져올 때 사용하는 함수를 모아서 관리하기 위한 모델 파일.

def obj_to_post(obj,flag=True):
    #가져온 테이터를 Json 형태로 pathing할 수 있도록 데이터를 하나의 긴 문자열 형태로 변경해줘야함.
    post = dict(vars(obj))#obj로 들어오는 속성들을 dictionary 형태로 저장하겠다.

    if obj.category:#값이 있으면
        post['category'] = obj.category.name
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
    
    del post['_state'],post['category_id'],post['create_date']

    if not flag:
        del post['tags'],post['update_date'],post['description'],post['content']
    
    return post