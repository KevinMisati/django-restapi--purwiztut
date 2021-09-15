from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, article_list,article_detail,ArticleApiView,ArticleDetails,GenericApiView

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    #path('article/',article_list ),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    path('article/',ArticleApiView.as_view() ),
    path('generic/article/',GenericApiView.as_view() ),
    path('generic/article/<int:id>',GenericApiView.as_view() ),
    #path('detail/<int:pk>/',article_detail ),
    path('detail/<int:id>/',ArticleDetails.as_view() ),
]
