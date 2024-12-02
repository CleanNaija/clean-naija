#In case we are using actual email , we would update our logic as follow 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings

class RegisterView(APIView):
    """
        Register a new user and send an email verification link
    """
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the registration endpoint

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate the email verification token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode('utf-8'))

            # Create the verification URL (this is what will be sent in the email)
            verification_url = f"{settings.FRONTEND_URL}/verify-email/{uid}/{token}/"
            
            # Send email
            send_mail(
                "Email Verification",
                f"Click the link to verify your email: {verification_url}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )

            # Return response with message to check email
            return Response({
                "message": "Registration successful. Please check your email to verify your account."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
No JWT tokens yet: We don't issue tokens in the RegisterView because the user's email is not verified yet.
Verification link sent via email: After successful registration, a verification token is created and sent to the user via email.
verification_url: The verification link is sent to the frontend (or the user) via email. The frontend should direct the user to this URL to verify their email.

"""


##### Things will be naturally followed by EmailVerificationView 
class EmailVerificationView(APIView):
    """
        Verify the user's email after registration
    """
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            # Decode user id from the URL
            uid = urlsafe_base64_decode(uidb64).decode('utf-8')
            user = get_user_model().objects.get(pk=uid)
            
            # Check if the token is valid
            if default_token_generator.check_token(user, token):
                user.is_verified = True  # Mark email as verified
                user.save()
                return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

"""
Token validation: When the user clicks the verification link, the uid (user ID) and token are passed to the view. The view decodes the user ID, finds the user, and checks if the token is valid.
Activate user: If the token is valid, the user's email is marked as verified (user.is_verified = True), and the user can now log in.
Error handling: If the token is invalid, the user is notified via the response.

"""


"""
In case we are using send grid 

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Use the SMTP backend for email sending
EMAIL_HOST = 'smtp.sendgrid.net'  # SendGrid's SMTP server
EMAIL_PORT = 587  # The standard SMTP port for SendGrid
EMAIL_USE_TLS = True  # Enable TLS (recommended for secure email sending)
EMAIL_HOST_USER = 'apikey'  # SendGrid uses 'apikey' as the username
EMAIL_HOST_PASSWORD = 'your_sendgrid_api_key'  # Replace with your SendGrid API key
DEFAULT_FROM_EMAIL = 'your-email@example.com'  # This is the email address to send from
"""

###Send grid function 
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from django.conf import settings

def send_email_verification_email(user):
    sg = sendgrid.SendGridAPIClient(api_key=settings.EMAIL_HOST_PASSWORD)
    from_email = Email(settings.DEFAULT_FROM_EMAIL)  # Sender's email address
    to_email = To(user.email)  # Recipient's email address

    # Generate the verification token and UID
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(str(user.pk).encode('utf-8'))
    verification_url = f"{settings.FRONTEND_URL}/verify-email/{uid}/{token}/"  # The URL to verify email

    # Create the email content
    subject = "Email Verification"
    content = Content("text/plain", f"Click the link to verify your email: {verification_url}")
    
    # Create the mail object
    mail = Mail(from_email, to_email, subject, content)
    
    try:
        response = sg.send(mail)
        # Optionally log or process the response from SendGrid
        return response
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return None

####Then the register view comes in 
class RegisterView(APIView):
    """
    Register a new user and send an email verification link
    """
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow anyone to access the registration endpoint

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Send email verification after user creation
            send_email_verification_email(user)

            return Response({
                "message": "Registration successful. Please check your email to verify your account."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
