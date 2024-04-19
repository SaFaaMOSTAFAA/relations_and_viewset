from myapp import views
from django.urls import path,include
from .views import Viewset_Student,Viewset_subject,Viewset_Department
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('student',views.Viewset_Student,basename='student')
router.register('subject',views.Viewset_subject,basename='subject')
router.register('department',views.Viewset_Department,basename='department')



urlpatterns = [
    path('',include(router.urls))
    
]
