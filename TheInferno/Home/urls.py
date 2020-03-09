
from django.urls import path
from .views import home, profile_view, Show_profile_view,Edit_profile_view, Bookclub_view, show_booking, contact, Feedback

app_name = 'Home'

urlpatterns = [
    path('', home, name='home'),
    path('add_profile', profile_view, name="add_profile"),
    path('profile', Show_profile_view, name="view_profile"),
    path('edit_profile/<int:pk>', Edit_profile_view, name="edit_profile"),
    path('add_bookings', Bookclub_view, name='add_booking'),
    path('show_bookings', show_booking.as_view(), name="view_booking"),
    path('contact_us', contact, name='contact_us'),
    path('feedback', Feedback, name='Feedback'),

]
