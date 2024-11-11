from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserRegistrationForm
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
import qrcode,json
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO
from email.mime.image import MIMEImage
from .firebase_config import db  # Ensure this points to the Realtime Database

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        age = request.POST.get('age')
        occupation = request.POST.get('occupation')
        interests = request.POST.get('interests')

        # Check if a user with this mobile number already exists
        existing_user = db.reference('users').child(mobile_number).get()
        if existing_user:
            # Resend the QR code if the user already exists
            resend_qr_code(mobile_number, email)
            return JsonResponse({'status': 'success', 'message': 'QR code resent to your email.'})

        # Create user entry in Firebase with mobile number as key
        user_data = {
            'full_name': full_name,
            'email': email,
            'age': age,
            'mobile' : mobile_number,
            'occupation': occupation,
            'interests': interests
        }
        user_ref = db.reference('users').child(mobile_number)
        user_ref.set(user_data)
        json_data = json.dumps(user_data)
        print(f"Json Data is {json_data}")
        # Generate and send QR code for new user
        qr_data = json_data  # Adjust the data as needed
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_code_file = ContentFile(buffer.read(), name=f"{mobile_number}_qr.png")

        # Send the QR code via email
        email_subject = "Your Registration QR Code"
        email_body = "Thank you for registering. Here is your QR code."
        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email]
        )
        email_message.attach(qr_code_file.name, qr_code_file.read(), 'image/png')
        email_message.send()

        return JsonResponse({'status': 'success', 'message': 'Your registration QR code has been sent to your email!'})
    else:
        form = UserRegistrationForm()

    return render(request, 'user_registration/registration_form.html', {'form': form})


def resend_qr_code(mobile_number, email):
    # Retrieve user data from Firebase
    existing_user = db.reference('users').child(mobile_number).get()

    if existing_user:
        json_data = json.dumps(existing_user)
        print(f"Json Data is {json_data}")
        
        # Generate QR code with the existing user data
        qr_data = json_data  # Adjust the data as needed
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_code_file = ContentFile(buffer.read(), name=f"{mobile_number}_qr.png")

        # Send the QR code via email
        email_subject = "Your Registration QR Code"
        context = {
            "qr_code_cid": "qr_code_image_cid",  # Reference to the CID in the email template
        }
        email_body = render_to_string('user_registration/template.html', context)
        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email]
        )
        email_message.content_subtype = "html"  # Set the email content type to HTML

        # Create the MIMEImage object and set the Content-ID header
        buffer.seek(0)  # Reset buffer position
        mime_image = MIMEImage(buffer.read(), _subtype='png') 
        mime_image.add_header('Content-ID', '<qr_code_image_cid>')  # Content-ID header for inline image

        # Attach the MIMEImage object to the email message
        email_message.attach(mime_image)

        # Send the email
        email_message.send()

        return True
    return False

def render_template(request):
    return render(request, 'user_registration/template.html')