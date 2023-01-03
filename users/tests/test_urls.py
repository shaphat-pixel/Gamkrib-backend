from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import ProfileView


class TestUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url = reverse('user-profile')
        self.assertEquals(resolve(url).func, ProfileView)