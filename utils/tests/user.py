from django.contrib.auth.models import User


def create_super_user(
    username='TestSuperUserUsername',
    password='TestSuperUserPassword123'
):

    User.objects.create_superuser(
        username=username,
        password=password
    )

    return username, password
