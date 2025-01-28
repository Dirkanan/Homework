from django.contrib import admin
from django.urls import path
from task1.views import head, games, basket, sign_up_by_html, sign_up_by_django, news


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', head),
    path('games/', games),
    path('basket/', basket),
    path('reg/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
    path('platform/news/', news),
]
