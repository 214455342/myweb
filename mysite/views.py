from django.shortcuts import render

# Create your views here.


def fiter_test(request):
    return render(request, 'filter.html', {'letters': 'abc', 'number': 1})


def news_list(request, news_type):
    news_dict = {'economic': '经济', 'sport': '体育'}
    news_titles = []
    if news_type == 'economic':
        news_titles = [('12/5', '齐文豹成为全国首富。'), ('12/4', '齐文豹成为全省首富。'),
                       ('12/3', '齐文豹成为全市首富。'), ('12/2', '齐文豹成为镇里首富。'), ('12/1', '齐文豹成为村里首富。')]
    return render(request, 'news_list.html', {'news_type': news_dict[news_type], 'news_titles': news_titles})

