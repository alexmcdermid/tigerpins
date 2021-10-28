from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pins/', views.pins_index, name='index'),
    path('pins/<int:pin_id>/', views.pins_show, name='show'),
    path('pins/create/', views.PinCreate.as_view(), name='create'),
    path('pins/<int:pk>/update/', views.PinUpdate.as_view(), name='update'),
    path('pins/<int:pk>/delete/', views.PinDelete.as_view(), name='delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hidden',views.hidden, name='hidden')
]