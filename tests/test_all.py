import pytest
from tests.app.models import User


@pytest.mark.django_db
def test_field_sqlite():
    User(email='Case@EXAMPLE.com').save()
    user = User.objects.filter(email='cAsE@eXample.com').first()
    assert user
    assert user.email == 'case@example.com'


@pytest.mark.django_db
def test_field_postgresql():
    User(email='Case@EXAMPLE.com').save(using='psql')
    user = User.objects.using('psql').filter(email='cAsE@eXample.com').first()
    assert user
    assert user.email == 'Case@EXAMPLE.com'
