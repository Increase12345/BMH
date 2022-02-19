from django.shortcuts import render
from django.core.mail import send_mail

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        phone = request.POST.get("phone")

        data = {
            "name": name,
            "email": email,
            "message": message,
            "phone": phone,
        }
        
        message = '''
        New message: {}
        
        From: {}

        Phone: {}
        '''.format(data["message"], data["email"], data["phone"])
        send_mail(data["name"], message, '', ["iamdjpavlov@gmail.com"])
        return render(request, "form/ty.html")

    return render(request, "form/form.html")


def ty(request):
    return render(request, "form/ty.html")