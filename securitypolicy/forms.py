from django import forms
from django_select2.forms import ModelSelect2Widget
from .models  import Rule, Section, SubSection, Policy


class RuleForm(forms.ModelForm):
    policy = forms.ModelChoiceField(
        queryset=Policy.objects.all(),
        label=u"Policy Select2",
        widget=ModelSelect2Widget(
            model=Policy,
            search_fields=['title__icontains'],
        )
    )

    section = forms.ModelChoiceField(
        queryset=Section.objects.all(),
        label=u"Section Select2",
        widget=ModelSelect2Widget(
            model=Section,
            search_fields=['title__icontains'],
            dependent_fields={'policy': 'policy'},
            max_results=5,
        )
    )
    subsection = forms.ModelChoiceField(
        queryset=SubSection.objects.all(),
        label=u"SubSection Select2",
        widget=ModelSelect2Widget(
            model=SubSection,
            search_fields=['title__icontains'],
            dependent_fields={'section': 'section'},
            max_results = 5,
        ),
        required=False,
    )
    class Meta:
        model = Rule
        fields = ('title', 'section', 'policy', 'subsection', 'content', 'reference')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subsection'].queryset = SubSection.objects.none()



class PolicyForm(forms.ModelForm):

    class Meta:
        model = Policy
        fields = ('title', 'description',)
