from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def index(request):
    if request.method == "POST":
        message_name = "ถึงคุณ " + request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            message_name,
            "เราได้รับข้อความคุณว่า '" + message + "' และจะเริ่มตอบสนองเร็วๆนี้",
            'admin@examplemail.com',
            [message_email],
        )

        return render(request, 'index.html', {'message_name': message_name})
    else:
        return render(request, 'home.html', {})
