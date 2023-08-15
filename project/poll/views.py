from django.shortcuts import render


def book_data(request):
    url = "http://api.kcisa.kr/openapi/service/rest/meta13/getKPEF0103"
    params = {
        'serviceKey':'a7218822-097a-4e77-9f11-977c0c72f06e',
        'numOfRows':10,
        'pageNo':1
    }
    response = request.get(url,params=params)

    if response.status_code ==200:
        data = response.json()
        items = data['body']['items']['item']

        parsed_data = []

        for item in items:
            title = item['title']
            creator = item['creator']
            description = item['description']
            parsed_data.append({
                'title':title,
                'creator':creator,
                'description':description
            })
        return render(request,'book_uni.html',{"data":parsed_data})
    
    return render(request,'error.html')