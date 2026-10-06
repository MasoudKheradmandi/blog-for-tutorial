from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User
from django.db import transaction
from django.contrib import messages
from .forms import ProfileForm
# Create your views here.

def bomb_view(phone_number):
    with transaction.atomic():
        user = User.objects.create_user(phone_number=phone_number)
        raise ValueError("VALUE error")
    
    return {
        "user":phone_number
    }


@login_required()
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # Process the form data and save it to the database
            image = form.cleaned_data.get('image')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            bio = form.cleaned_data.get('bio')

            # Assuming you have a Profile model related to the User model
            profile = request.user.profile  # Get the user's profile
            profile.image = image
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.bio = bio
            profile.save()
            messages.success(request, "Profile updated successfully.")
        else:
            # Handle form validation errors
            print(form.errors)
            messages.error(request, "Please correct the errors below.")
    context = {"form": ProfileForm(),"user_profile":request.user.profile}
    return render(request,"profile.html", context)