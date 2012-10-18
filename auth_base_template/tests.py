from django.test import TestCase
from django.test.client import RequestFactory
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from auth_base_template.context_processors import auth_base_template


class ContextProcessorTestCase(TestCase):

    def setUp(self):
        self.rf = RequestFactory()

    def test_logged_out(self):
        request = self.rf.get('/')
        request.user = AnonymousUser()
        context = auth_base_template(request)
        self.assertEqual(context['auth_base_template'], settings.LOGGED_OUT_BASE_TEMPLATE)

    def test_logged_in(self):
        request = self.rf.get('/')
        request.user = User()
        context = auth_base_template(request)
        self.assertEqual(context['auth_base_template'], settings.LOGGED_IN_BASE_TEMPLATE)
