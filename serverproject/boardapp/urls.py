from django.urls import path
from django.urls import path
from .views import BoardViewSet

board_list = BoardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


board_detail = BoardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('board/', board_list),
    path('board/<int:pk>/', board_detail),
]