from django import forms
from django.contrib.admin import AdminSite
from ckeditor.widgets import CKEditorWidget

from adminsortable.admin import SortableAdmin

from .models import Rule, Section, Needs


class SecurityPolicyAdmin(AdminSite):
    site_header = 'Security Policy Admin Site'


class SectionAdmin(SortableAdmin):
    list_display = ('title','description','section_order',)


class RuleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Rule
        fields = '__all__'


class RuleAdmin(SortableAdmin):
    list_display = ('title', 'author', 'date_posted','rule_order','section')
    form = RuleAdminForm


securitypolicy_admin_site = SecurityPolicyAdmin(name='securitypolicy-admin')
securitypolicy_admin_site.register(Section, SectionAdmin)
securitypolicy_admin_site.register(Rule, RuleAdmin)
securitypolicy_admin_site.register(Needs)