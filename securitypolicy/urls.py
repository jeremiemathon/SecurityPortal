"""SecurityPortal URL Configuration

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

from django.urls import path
from django.conf.urls import include

from .views import SectionListView, SectionDetailView, RuleDetailView, RuleCreateView, RuleUpdateView, RuleDeleteView, RuleSearch, SectionListViewAPI, RuleListViewAPI
from .admin import securitypolicy_admin_site

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'section', SectionListViewAPI)
router.register(r'rule', RuleListViewAPI)


urlpatterns = [
    path('', SectionListView.as_view(), name='policy-home'),
    path('section/', SectionDetailView.as_view(), name='section-detail'),
    path('section/<int:pk>', SectionDetailView.as_view(), name='section-detail'),

    path('results/', RuleSearch.as_view(), name='rule-search'),

    path('rule/<int:pk>$', RuleDetailView.as_view(), name='rule-detail'),
    path('rule/new', RuleCreateView.as_view(), name='rule-create'),
    path('rule/<int:pk>/update/', RuleUpdateView.as_view(), name='rule-update'),
    path('rule/<int:pk>/delete/', RuleDeleteView.as_view(), name='rule-delete'),

    path('api/', include(router.urls)),

    path('admin/', securitypolicy_admin_site.urls),
]

