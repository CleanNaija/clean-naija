from django.urls import path 


from .views import (
    RegisterView,
    LoginView,
    TokenRefreshView,
    ForgotPasswordView,
    ResetPasswordView,
    ChangePasswordView,
    LogoutView,
    ProfileView,
    UpdateProfileView,
    WasteBinView,
    WasteCollectionRequestView,
    WasteTypeView, CollectionPointView, 
    CollectionRequestView, ReportView,
    WasteAnalyticsView
    
)




urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),  # Forgot password
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),  # Reset password

    # Authenticated Views (Protected)
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),  # Change password
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout (blacklist refresh token)

      # Profile Views
    path('profile/', ProfileView.as_view(), name='profile'),  # View user profile
    path('profile/update/', UpdateProfileView.as_view(), name='update-profile'),  # Update user profile


    #### Main Business Logic 

    path('waste-bins/', WasteBinView.as_view(), name='waste-bins'),
    path('collection-requests/', WasteCollectionRequestView.as_view(), name='collection-requests'),
    path('waste-types/', WasteTypeView.as_view(), name='waste-types'),
    path('collection-points/', CollectionPointView.as_view(), name='collection-points'),
    path('requests/', CollectionRequestView.as_view(), name='requests'),
    path('reports/', ReportView.as_view(), name='reports'),
    path('analytics/', WasteAnalyticsView.as_view(), name='analytics'),



]




