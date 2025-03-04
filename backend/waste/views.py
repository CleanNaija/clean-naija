from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import permissions
from .serializers import CustomUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes=(permissions.AllowAny,)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes=(permissions.AllowAny,)


###################################### Authentication Logic #################################################
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    """
    Register a new user and return JWT tokens
    """
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the registration endpoint

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This will hash the password
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'user': serializer.data,
                'access': access_token,
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class RegisterView(APIView):
    """
        Register a new user and return JWT tokens

    """
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the registration endpoint
    def post(self,request,*args,**kwargs):
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh=RefreshToken.for_user(user)
            access_token=str(refresh.access_token)
            return Response({
                'user':serializer.data,
                'access':access_token,
                'refresh':str(refresh),
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    """
        Login a user and return JWT tokens
    """

    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the login endpoint
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=get_user_model().objects.filter(username=username).first()


        if user and user.check_password(password):
            refresh=RefreshToken.for_user(user)
            access_token=str(refresh.access_token)
            return Response({
                'access':access_token,
                'refresh':str(refresh),
            })
        return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
'''  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the login endpoint

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Debug: Print the username and password
        print(f"Username: {username}, Password: {password}")

        user = get_user_model().objects.filter(username=username).first()

        # Debug: Print the user object and hashed password
        if user:
            print(f"User: {user}")
            print(f"Stored hashed password: {user.password}")
        else:
            print("User not found")

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'access': access_token,
                'refresh': str(refresh),
            })
        else:
            # Debug: Print why the login failed
            if not user:
                print("User not found")
            else:
                print("Password is incorrect")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
class TokenRefreshView(APIView):
    """
        Refresh JWT token using refresh token 
    """
    def post(self,request,*args,**kwargs):
        refresh_token=request.data.get('refresh')
        if refresh_token:
            try:
                refresh=RefreshToken(refresh_token)
                access_token=str(refresh.access_token)
                return Response({
                    'access':access_token
                })
            except Exception as e:
                return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"Refresh token is required"},status=status.HTTP_400_BAD_REQUEST)


###Logout View 
class LogoutView(APIView):
    """
        Logout the user by blacklisting the refresh token
    """
    def post(self,request,*args,**kwargs):
        try:
            refresh_token=request.data.get('refresh')
            if refresh_token:
                #Blacklist the refresh token 
                RefreshToken(refresh_token).blacklist()
                return Response({"message":"Successfully logged out"},status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response({"error":"Refresh token is required"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
"""
    Complete Flow: From Forgot Password to Successful Password Reset
Forgot Password: User submits email.
Send Reset Link: System generates a token, sends it via email.
User Clicks Reset Link: User is directed to the reset page.
Validate Token: The system validates the token and the user ID.
Password Reset: User sets a new password, and the password is updated.
Logout or Login: After password reset, the user can log in with the new password.
"""

######Forgot password 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings

class ForgotPasswordView(APIView):
    """
        Handle forgot password and send password reset email
    """
    def post(self,request,*args,**kwargs):
        email=request.data.get('email')
        if email:
            try:
                user=get_user_model().objects.get(email=email)
                #Generate token and encode uid
                token=default_token_generator.make_token(user)
                uid=urlsafe_base64_encode(str(user.pk).encode('utf-8'))
                reset_url=f"{settings.FRONTENDURL}/reset-password/{uid}/{token}/" #Frontend URL should handle this 
                #Send password reset email 
                send_mail(
                    "Password Reset Request",
                    f"Click here to reset your password: {reset_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                return Response({"mesage":"Password reset email sent"},status=status.HTTP_200_OK)
            except get_user_model().DoesNotExist:
                return Response({"error":"No user found with this email address"},status=status.HTTP_404_NOT_FOUND)
        return Response({"error":"Email is required"},status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework import serializers

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField()
    uid = serializers.CharField()

class ResetPasswordView(APIView):
    """
        View to handle password reset via a token and uid 
    """
    def post(self,request,*args,**kwargs):
        serializer=ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            uid=serializer.validated_data.get('uid')
            token = serializer.validated_data.get('token')
            password = serializer.validated_data.get('password')

            try:
                #Decode UID
                uid=urlsafe_base64_decode(uid).decode('utf-8')
                user=get_user_model().objects.get(pk=uid)

                #Validate token
                if default_token_generator.check_token(user,token):
                    user.set_password(password)
                    user.save()
                    return Response({"message":"Password reset successful"},status=status.HTTP_200_OK)
                return Response({"error":"Invalid token"},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    




##Change password 
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

class ChangePasswordView(APIView):
    """
    Allow users to change their password
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




####### The Profile View s
class ProfileView(APIView):
    """
    Retrieve the user's profile (authenticated user only)
    """
    permission_classes = [IsAuthenticated]  # Only authenticated users can access their profile
    
    def get(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user (CustomUser model)

        # Return the user details including custom fields
        return Response({
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,  # Custom field
            'phone_number': user.phone_number,  # Custom field
            'address': user.address,  # Custom field
            # Add any other custom fields you want to return
        })
    



####Update view 
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This refers to the CustomUser model
        fields = ['role', 'phone_number', 'address']  # Add any other fields you want to update

    def update(self, instance, validated_data):
        # Update the user instance with the validated data
        instance.role = validated_data.get('role', instance.role)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UpdateProfileSerializer

class UpdateProfileView(APIView):
    """
    Update the user's profile (authenticated users only)
    """
    permission_classes = [IsAuthenticated]  # Only authenticated users can update their profile
    
    def get(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user (CustomUser model)
        # Serialize and return the current user data (for display purposes)
        serializer = UpdateProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user (CustomUser model)
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)  # `partial=True` allows partial updates
        
        if serializer.is_valid():
            serializer.save()  # Save the updated profile details
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated user data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings

class EmailVerificationView(APIView):
    """
    Verify the user's email after registration
    """
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode('utf-8')
            user = get_user_model().objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_verified = True
                user.save()
                return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




############################################################# Main Part of the Business Logic ################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import WasteBin, WasteCollectionRequest, WasteType, CollectionPoint, CollectionRequest, Report, WasteAnalytics
from .serializers import WasteBinSerializer, WasteCollectionRequestSerializer, WasteTypeSerializer, CollectionPointSerializer, CollectionRequestSerializer, ReportSerializer, WasteAnalyticsSerializer

# WasteBin View
class WasteBinView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        waste_bins = WasteBin.objects.all()
        serializer = WasteBinSerializer(waste_bins, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = WasteBinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WasteCollectionRequest View
class WasteCollectionRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        requests = WasteCollectionRequest.objects.filter(user=request.user)
        serializer = WasteCollectionRequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = WasteCollectionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WasteType View
class WasteTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        waste_types = WasteType.objects.all()
        serializer = WasteTypeSerializer(waste_types, many=True)
        return Response(serializer.data)

# CollectionPoint View
class CollectionPointView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        collection_points = CollectionPoint.objects.all()
        serializer = CollectionPointSerializer(collection_points, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CollectionPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CollectionRequest View
class CollectionRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        collection_requests = CollectionRequest.objects.filter(user=request.user)
        serializer = CollectionRequestSerializer(collection_requests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CollectionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Report View
class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        reports = Report.objects.filter(user=request.user)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WasteAnalytics View
class WasteAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        analytics = WasteAnalytics.objects.all()
        serializer = WasteAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)
