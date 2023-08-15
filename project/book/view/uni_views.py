from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.core.paginator import Paginator

# def book_data(request):

#     url = "http://api.kcisa.kr/openapi/service/rest/meta13/getKPEF0103"
#     params = {
#         'serviceKey': 'a7218822-097a-4e77-9f11-977c0c72f06e',
#         'numOfRows': 10,
#         'pageNo': 1       
#     }

    

#     response = requests.get(url, params=params)
#     print(response)

#     # data = response.json()

#     # if response.status_code == 200:
#     #     try:
#     #         data = response.json()
#     #         print("data", data)
#     #     except json.JSONDecodeError:
#     #         return JsonResponse({"error":f"Unable to decode JSON.Response:{response.text}"},status=400)


#     items = response['body']['items']['item']

#     print("items", items)


#     parsed_data = []

#     for item in items:
#         parsed_data.append({
#             'title': item['title'],
#             'creator': item['creator'],
#             'description': item['description'],
#             'subjectKeyword': item['subjectKeyword'],
#             'subjectCategory': item['subjectCategory'],
#             'regDate': item['regDate'],
#             'referenceIdentifier': item['referenceIdentifier'],
#         })

#         # 페이지 번호와 도서 수를 쿼리 파라미터에서 가져온다
#         # page_number = int(request.GET.get("page",1))
#         # books_per_load = int(request.GET.get('books_per_load',4))

#         # # Paginator 객체를 사용하여 데이터를 페이징 처리한다.
#         # paginator = Paginator(parsed_data,books_per_load)
#         # paged_books = paginator.get_page(page_number)
#         # # JsonResponse를 사용하여 파싱된 데이터 반환
#         # return JsonResponse(list(paged_books.object_list), safe=False)
#     return render(request,"book/book_uni.html",{"data":parsed_data})

#     # else:
#     #     return JsonResponse({'error': 'Unable to fetch data from the API'}, status=400)

def book_data(request):
    return render(request,"book/book_uni.html")