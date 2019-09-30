from django import forms
from .models import Page
from .models import Tag
# from codemirror import CodeMirrorTextarea
from django.utils.crypto import get_random_string
from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.fields import CodeMirrorField


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['user', 'title', 'description', 'slug', 'public', 'sample', 'assignment', 'tags', 'htmlHead',
                  'htmlBody', 'css', 'javascript', 'useCodeMirror']

    # htmlHead = forms.CharField(widget= CodeMirrorWidget(mode = "xml"), required = False,)
    # htmlBody = forms.CharField(widget= CodeMirrorWidget(mode = "xml"), required = False,)
    # css = forms.CharField(widget= CodeMirrorWidget(mode = "css"), required = False,)
    # javascript = forms.CharField(widget= CodeMirrorWidget(mode = "javascript"), required = False,)

    # htmlHead = forms.CharField(widget= CodeMirrorWidget(), required = False,)
    # htmlBody = forms.CharField(widget= CodeMirrorWidget(), required = False,)
    # css = forms.CharField(widget= CodeMirrorWidget(), required = False,)
    # javascript = forms.CharField(widget= CodeMirrorWidget(), required = False,)

    htmlHead = CodeMirrorField(required=False, config_name='html')
    htmlBody = CodeMirrorField(required=False, config_name='html')
    css = CodeMirrorField(required=False, config_name='css')
    javascript = CodeMirrorField(required=False, config_name='javascript')

    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all(),
                                          required=False)
