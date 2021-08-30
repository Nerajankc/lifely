from django.urls import path
from .views import career, index, about_us, blog, privacy_policy, terms_and_condition, user_policy

urlpatterns = [
    path('', index, name="index1"),
    path('about', about_us, name="about"),
    path('blog', blog, name="blog"),
    path('career', career, name="career"),
    path('privacy-policy', privacy_policy, name="privacy-policy"),
    path('user-policy', user_policy, name="user-policy"),
    path('terms-and-condition', terms_and_condition, name="terms-and-condition"),
]
