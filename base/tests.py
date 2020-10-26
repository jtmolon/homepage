import pytest

from django.apps import apps

from wagtail.images.models import Image
from wagtail.images.tests.utils import get_test_image_file

from base.apps import BaseConfig
from base.models import People

# Test models

@pytest.fixture()
def person(db):
    return People.objects.create(first_name="Foo", last_name="Bar")

@pytest.mark.django_db
def test_people_str(person):
    assert str(person) == "Foo Bar"

@pytest.mark.django_db
def test_people_thumb_image(person):
    image = Image(
        title="Test image",
        file=get_test_image_file()
    )
    image.save()
    person.image = image
    assert person.thumb_image == image.get_rendition("fill-50x50").img_tag()

@pytest.mark.django_db
def test_people_thumb_no_image(person):
    assert person.thumb_image == ""

# Test apps

def test_base_app():
    assert BaseConfig.name == "base"
    assert apps.get_app_config("base").name == "base"
