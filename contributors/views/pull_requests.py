from django.views import generic

from contributors.models.contribution import Contribution
from contributors.views.mixins import TableSortSearchAndPaginationMixin

from django_filters.views import FilterView
from contributors.forms.filters import PullRequestSortSearchFilter


# class ListView(TableSortSearchAndPaginationMixin, generic.ListView):
#     """A view for a list of all pull requests."""
#
#     sortable_fields = (
#         'info__title',
#         'repository__full_name',
#         'contributor__login',
#         'created_at',
#         'info__state',
#     )
#     searchable_fields = (
#         'info__title',
#         'repository__full_name',
#         'contributor__login',
#         'info__state',
#     )
#     ordering = sortable_fields[0]
#
#     template_name = 'pull_requests_list.html'
#     queryset = Contribution.objects.filter(type='pr')


class ListView(FilterView):
    template_name = 'pull_requests_list.html'
    queryset = Contribution.objects.filter(type='pr')
    filterset_class = PullRequestSortSearchFilter
    context_object_name = 'data'
