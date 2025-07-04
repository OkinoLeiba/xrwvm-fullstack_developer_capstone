# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route="register", view=views.registration, name="register"),
    # path for login
    path(route="login", view=views.login_user, name="login"),

    #path for logout
    path(route="logout", view=views.logout_request, name="logout"),

    # path for getting cars
    path(route="get_cars", view=views.get_cars, name="get_cars"),

    # path for dealer reviews view
    # path(route="dealer_reviews", view=views.dealer_reviews, name="dealer_reviews"),

    # path for add a review view
    # path(route="add_review", view=views.add_review, name="add_review"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
