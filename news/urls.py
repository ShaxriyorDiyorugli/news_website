from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import (
detail,
home,
region_detail,
category_detail,
AllViews
)

urlpatterns = [
    path('', home, name='home'),
    path('all-news/', AllViews.as_view(), name='all-news'),
    path('category/<int:id>', category_detail, name='category-news'),
    path('region/<int:id>', region_detail, name='region-news'),
    path('detail/<int:id>', detail, name='detail')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)