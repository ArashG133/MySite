from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path("", blog, name='blog'),
    path("<int:pid>/", single_blog, name='single_blog'),
    # path("<int:pid>/", test, name='test'),

    path("resume/", resume_view, name="resume")

]