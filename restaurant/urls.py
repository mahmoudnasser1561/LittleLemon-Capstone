from django.urls import path, include
from rest_framework import routers
from . import views

# Initialize DefaultRouter for ViewSets
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # Router routes (includes /users/ endpoints)
    path('', include(router.urls)),

    # API authentication for browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Class-Based Views (CBVs)
    path('booking/', views.bookingview.as_view(), name='booking'),
    # path('menu/', views.menuview.as_view(), name='menu'),
    
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]