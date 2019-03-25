"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from core.views import BaseView

urls_base = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('favicon.ico', RedirectView.as_view(
            url=staticfiles_storage.url('favicon/favicon.ico'),
        ),
        name='favicon',
    ),
    # path('', BaseView.as_view(), name='base'),
]

catch_all_urls = [
    path('', BaseView.as_view(), name='base'),
    path('/', BaseView.as_view(), name='base'),
    path('<path:name>/', BaseView.as_view(), name='base'),
]

if settings.DEBUG:
    urls_base = urls_base + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urls_base = urls_base + catch_all_urls

urlpatterns = urls_base
