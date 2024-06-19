import pytest

from django.contrib.auth import get_user_model
from account.models import UserData


User = get_user_model()


@pytest.fixture
def user_1(db):
    user = User.objects.create_user(username="test", password="test")
    return user


@pytest.fixture
def user_2(db):
    user = User.objects.create_user(username="test2", password="test")
    return user


@pytest.fixture
def user_3(db):
    user = User.objects.create_user(username="test3", password="test")
    return user


@pytest.fixture
def user_data_1(db, user_1):
    user_data = UserData.objects.create(user=user_1, index=1)
    return user_data
