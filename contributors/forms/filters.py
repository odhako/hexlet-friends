import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from contributors.models.contribution import Contribution

from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

CHOICES = (
    ('open', 'Open'),
    ('merged', 'Merged'),
    ('closed', 'Closed')
)


class PullRequestSortSearchFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='full_search',
        label=False
    )
    state = django_filters.ChoiceFilter(
        label=False,
        choices=CHOICES,
        empty_label=_('Full list'),
        method='state_filter',
    )

    def full_search(self, queryset, name, value):
        return queryset.filter(
            Q(info__title__icontains=value) \
            | Q(repository__full_name__icontains=value) \
            | Q(contributor__login__icontains=value)
        )

    def state_filter(self, queryset, name, value):
        return queryset.filter(info__state=value)

    class Meta:
        model = Contribution
        fields = ['search', 'state']

    @property
    def helper(self):
        """Control form attributes and its layout."""
        helper = FormHelper()
        helper.form_method = 'get'
        helper.form_class = 'd-flex'
        helper.layout = Layout(
            Field('search', placeholder=_("Filter by name")),
            Field('state'),
            StrictButton(
                    _("Search"),
                    type='submit',
                    css_class='btn btn-outline-primary',
            ),
        )
        return helper
