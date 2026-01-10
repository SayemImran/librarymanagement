from rest_framework.routers import DefaultRouter
from member.views import MemberViewSet
from book.views import BookViewSet,AuthorViewSet
from borrowing.views import BorrowRecordViewSet
router = DefaultRouter()
router.register('member', MemberViewSet, basename='members')
router.register('book',BookViewSet, basename='books')
router.register('author', AuthorViewSet, basename='authors')
router.register('borrowrecord', BorrowRecordViewSet, basename='borrowrecord')
urlpatterns = router.urls
