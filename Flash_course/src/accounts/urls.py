"""
FlashCourses Accounts URLs

Created By:     Patrick R. McElhiney
Modified Date:  4/6/2018
"""
from django.urls import path, re_path, include

app_name = 'accounts'

urlpatterns = [
    path('api/', include('accounts.api.urls', namespace='accounts_api')),
]
