from rest_framework import filters


class DrugSearchFilter(filters.SearchFilter):
    search_param = 'name'
