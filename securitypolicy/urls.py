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

from .views import (
    SectionListView,
    SubSectionListView,
    RuleDetailView,
    RuleCreateView,
    RuleUpdateView,
    RuleDeleteView,
    RuleSearch,
    SectionListViewAPI,
    RuleListViewAPI,
    RuleListView,
    PolicyListView,
    PolicyCreateView,
    PolicyUpdateView,
    PolicyDeleteView,
    load_subsection
)

from .admin import securitypolicy_admin_site

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'section', SectionListViewAPI)
# router.register(r'rule', RuleListViewAPI)


urlpatterns = [
    path('', PolicyListView.as_view(), name='policy-list'),
    path('policy/<int:p_id>', SectionListView.as_view(), name='section-list'),
    path('policy/<int:p_id>/section/<int:s_id>', SubSectionListView.as_view(), name='subsection-list'),
    path('policy/<int:p_id>/section/<int:s_id>/subsection/<int:ss_id>', RuleListView.as_view(), name='subsection-detail'),
    path('policy/new', PolicyCreateView.as_view(), name='policy-create'),
    path('policy/<int:pk>/update/', PolicyUpdateView.as_view(), name='policy-update'),
    path('policy/<int:pk>/delete/', PolicyDeleteView.as_view(), name='policy-delete'),

    path('results/', RuleSearch.as_view(), name='rule-search'),

    path('rule/<int:pk>', RuleDetailView.as_view(), name='rule-detail'),
    path('rule/new', RuleCreateView.as_view(), name='rule-create'),
    path('rule/<int:pk>/update/', RuleUpdateView.as_view(), name='rule-update'),
    path('rule/<int:pk>/delete/', RuleDeleteView.as_view(), name='rule-delete'),
    path('ajax/load-sub_sections/', load_subsection, name='ajax_load_subsections'),

    path(r'select2/', include('django_select2.urls')),
    path('api/', include(router.urls)),

    path('admin/', securitypolicy_admin_site.urls, name='securitypolicy-admin'),
]
