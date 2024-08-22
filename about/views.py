from django.shortcuts import render
from.models import About
from .forms import CollaborateForm
from django.contrib import messages


# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    # Get the latest About instance and its associated CollaborateRequest form.
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_request = collaborate_form.save()
            collaborate_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )


    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
         },
    )