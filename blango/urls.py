import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

import blog.views
import blango_auth.views

urlpatterns = [path("api/v1/", include("blog.api_urls")),]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('ip/', blog.views.get_ip),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    
    path('accounts/profile/', blango_auth.views.profile, name='profile'),
    path(
    'accounts/register/',
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name='django_registration_register',
    ),
    path('post/<slug>/', blog.views.post_detail, name="blog-post-detail"),
    
    path('', blog.views.index),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]