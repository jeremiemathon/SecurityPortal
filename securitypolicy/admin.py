from django import forms
from django.contrib.admin import AdminSite
from ckeditor.widgets import CKEditorWidget

from adminsortable.admin import SortableAdmin

from .models import Rule, Section, Needs, SubSection


class SecurityPolicyAdmin(AdminSite):
    site_header = 'Security Policy Admin Site'


class SectionAdmin(SortableAdmin):
    list_display = ('title', 'description', 'order', )
    # list_filter = ('title', )


class SubSectionAdmin(SortableAdmin):
    list_display = ('title', 'description', 'order', 'section', )
    # list_filter = ('title', )


class RuleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Rule
        fields = '__all__'


class RuleAdmin(SortableAdmin):
    list_display = ('title', 'author', 'date_posted', 'order', 'subsection')

    form = RuleAdminForm


securitypolicy_admin_site = SecurityPolicyAdmin(name='securitypolicy-admin')
securitypolicy_admin_site.register(Section, SectionAdmin)
securitypolicy_admin_site.register(SubSection, SubSectionAdmin)
securitypolicy_admin_site.register(Rule, RuleAdmin)
securitypolicy_admin_site.register(Needs)
