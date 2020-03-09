from django.urls import path
from .views import Home_view, Booking_view, New_Amenities_view, all_user_view, contact_user_view, show_feedback_view
app_name = 'Admin'

urlpatterns = [
    path('', Home_view, name="home"),
    path('all_user/', all_user_view, name="all_user"),
    path('booking/', Booking_view, name="all_booking"),
    path('contact_details/', contact_user_view, name="contact_details"),
    path('add_amenitie/', New_Amenities_view, name="new_amenitie"),
    path('show_feedback/', show_feedback_view, name="feedback_details"),

]
