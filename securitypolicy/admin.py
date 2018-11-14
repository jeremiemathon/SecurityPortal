from django import forms
from django.contrib.admin import AdminSite

from ckeditor.widgets import CKEditorWidget
from adminsortable.admin import SortableAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Rule, Section, Needs, SubSection, Policy


class SecurityPolicyAdmin(AdminSite):
    site_header = 'Security Policy Admin Site'


class PolicyAdmin(SortableAdmin):
    list_display = ('title', 'description', 'order', )
    # list_filter = ('title', )

    class Meta:
        pass

class SectionAdmin(SortableAdmin):
    list_display = ('title', 'description', 'order', 'policy')
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
    list_display = ('title', 'section', 'subsection', 'author', )
    # readonly_fields = ('author', 'date_posted')
    search_fields = ('title', 'section__title', 'subsection__title',)
    form = RuleAdminForm
    list_filter = ('section', )
    list_editable = ('section', 'subsection',)

class RuleResource(resources.ModelResource):
    class Meta:
        model = Rule

class RuleResourceAdmin(ImportExportModelAdmin):
    resource_class = RuleResource

class RuleProxyModel(Rule):
    class Meta:
        verbose_name_plural = 'Import / Export Rules'
        proxy = True


securitypolicy_admin_site = SecurityPolicyAdmin(name='securitypolicy-admin')
securitypolicy_admin_site.register(Section, SectionAdmin)
securitypolicy_admin_site.register(Policy, PolicyAdmin)
securitypolicy_admin_site.register(SubSection, SubSectionAdmin)
securitypolicy_admin_site.register(Rule, RuleAdmin)
securitypolicy_admin_site.register(RuleProxyModel, RuleResourceAdmin)
securitypolicy_admin_site.register(Needs)
