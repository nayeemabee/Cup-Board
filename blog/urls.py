from django.urls import path, include
from blog.views import ContactFormViewSet
from rest_framework import routers
from .views import(
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
)


urlpatterns = [
    path('', blog_post_list_view),
    path('blog/<str:slug>/', blog_post_detail_view),
    path('blog/<str:slug>/edit', blog_post_update_view),
    path('blog/<str:slug>/delete', blog_post_delete_view)

]

router = routers.DefaultRouter()
router.register(r'contactform', ContactFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact_images', include(router.urls))
]
