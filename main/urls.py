from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('subject', SubjectViewSet)
router.register('studentprofile', StudentProfileViewSet)
router.register('parentprofile', ParentProfileViewSet)
router.register('teacherprofile', TeacherProfileViewSet)
router.register('principalprofile', PrincipalProfileViewSet)
router.register('note', NoteViewSet)
router.register('message', MessageViewSet)
router.register('payment', PaymentViewSet)
router.register('subjectfetch', SubjectFetchViewSet, basename='subjectfetch')
router.register('studentprofilefetch', StudentProfileFetchViewSet, basename='studentprofilefetch')
router.register('parentprofilefetch', ParentProfileFetchViewSet, basename='parentprofilefetch')
router.register('teacherprofilefetch', TeacherProfileFetchViewSet,  basename='teacherprofilefetch')
router.register('principalprofilefetch', PrincipalProfileFetchViewSet,  basename='principalprofilefetch')
router.register('notefetch', NoteFetchViewSet, basename='notefetch')
router.register('messagefetch', MessageFetchViewSet, basename='messagefetch')
router.register('paymentfetch', PaymentFetchViewSet, basename='paymentfetch')
router.register('teachersalaryfetch', TeacherSalaryFetchViewSet, basename='teachersalaryfetch')
router.register('studentprofilefetchbyclass', StudentProfileFetchByClassViewSet, basename='studentprofilefetchbyclass')

urlpatterns = [
    path('', include(router.urls)),
]