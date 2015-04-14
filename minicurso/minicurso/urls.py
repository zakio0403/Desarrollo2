from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import HomeView
from main.views import cuerpo


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minicurso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', cuerpo),
    # url(r'^', HomeView.as_view()),
)
