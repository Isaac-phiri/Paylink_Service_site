from django.shortcuts import redirect, render
from .form import ReviewModelForm
from django.core.mail import send_mail

# Create your views here.

def reviews(request):
    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()

            #send email to the reviewed user
            subject = ""
            message = ""
            from_email =""
            to_email = ""

            send_mail(subject, message, from_email, [to_email])

            return redirect("Thanks for you Views")
        else:
            form = ReviewModelForm
    return render(request, "review.html")


def homepage(request):
    return  render(request, "homepage.html")


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")