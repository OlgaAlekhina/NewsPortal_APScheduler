from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView, CategoryListView, subscribe_category
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*1)(NewsList.as_view()), name='news'),
    path('search', NewsSearch.as_view(), name='news_search'),
    path('add', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('<int:pk>/edit', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('category/<int:cats>/', cache_page(60*5)(CategoryListView.as_view()), name='post-category'),
    path('category/<int:cats>/subscribe_category', subscribe_category, name='subscribe-category')
    ]