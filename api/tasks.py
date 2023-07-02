from celery import app
from django.core.mail import send_mass_mail
from .models import UserData


@app.shared_task
def follow_collision_email(u1, u2):
    u1, u2 = UserData.objects.filter(pk__in=[1, 4])[:2]
    print(u1)
    print(u2)
    message1 = (
        "Взаимная симпатия!",
        f"Вы понравились {u2.name}! Почта участника: {u2.email}",
        "from@example.com",
        ["first@example.com", "other@example.com"],
    )
    message2 = (
        "Взаимная симпатия!",
        f"Вы понравились {u1.name}! Почта участника: {u1.email}",
        "from@example.com",
        ["second@test.com"],
    )

    send_mass_mail((message1, message2), fail_silently=False)
