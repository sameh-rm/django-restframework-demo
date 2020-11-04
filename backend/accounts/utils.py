

import six

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from enum import Enum


class TokenTypes(Enum):
    EMAIL_TOKEN = "EMAIL_TOKEN"
    CHANGE_PASSWORD_TOKEN = "CHANGE_PASSWORD_TOKEN"


class TokenGenerator(PasswordResetTokenGenerator):

    def __init__(self, type, **kwargs):
        self.type = type

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) +
            six.text_type(timestamp) +
            six.text_type(user.is_active) +
            # self.type[0] the first element of token type EMAIL_TOKEN OR CHANGE_PASSWORD_TOKEN
            six.text_type(self.type)
        )
