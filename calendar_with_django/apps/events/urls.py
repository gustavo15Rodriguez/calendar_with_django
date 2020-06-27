from django.urls import path
from calendar_with_django.apps.events.views import CalendarView, event

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar_list'),
    path('event/new/', event, name='new_event'),
    path('event/edit/<int:event_id>', event, name='edit_event'),
]
