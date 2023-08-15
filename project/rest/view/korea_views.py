from django.shortcuts import render
import requests
from django.core.paginator import Paginator


def korea_food(request):
    # 서울시 오픈API에 요청을 보냅니다.
    MIN_PRIDE_LENGTH =5
    query = request.GET.get("search","")
    page = int(request.GET.get('page',1))
    start = (page -1)*12 +1 # 시작 인덱스 계산
    end = start + 11 # 끝 인덱스 계산
    category = request.GET.get('category','001')
    items = []
    # SH_PRIDE 가 있는 거만 선택해서 보여줌
    #while len(items) < 12:
    url = "http://openAPI.seoul.go.kr:8088/72434549796b67313637755a546279/json/ListPriceModelStoreService/{}/{}/{}/".format(start,end,category)

    #url = "http://openAPI.seoul.go.kr:8088/72434549796b67313637755a546279/json/ListPriceModelStoreService/1/10/001/"
    
    response = requests.get(url)

    if response.status_code ==200:
        

        r = response.json()
        items = r["ListPriceModelStoreService"]['row']
        if query:
            items = [item for item in items if query.lower() in item["SH_NAME"].lower()]
        # 화면에 보여줄 데이터
#        items = [item for item in itemss if len(item['SH_PRIDE']) >= MIN_PRIDE_LENGTH]


    list_total_count = r["ListPriceModelStoreService"]["list_total_count"]
    items_count = len(items)
    paginator = Paginator(range(list_total_count),items_count)
    page_obj = paginator.get_page(page)
        # 전체 개수


    # 'items' 변수를 컨텍스트에 추가하여 템플릿에 전달합니다.
    context = {
        'items': items,
        'page_obj':page_obj,
        'query':query
    }

    return render(request, 'rest/korea_food.html',context)

def food_detail(request,SH_ID):

    url = "http://openAPI.seoul.go.kr:8088/72434549796b67313637755a546279/json/ListPriceModelStoreService/1/1/{}/".format(SH_ID)
    response =requests.get(url)
    data = response.json()
    try:

        item = data["ListPriceModelStoreService"]['row']
    except KeyError:
        item = None
    context={'item':item}
    return render(request,'rest/food_detail.html',context)
