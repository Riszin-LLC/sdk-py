# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function

from predicthq.decorators import returns
from predicthq.endpoints.base import BaseEndpoint

from .schemas import Account


class AccountsEndpoint(BaseEndpoint):

    @returns(Account)
    def self(self):
        return self.client.get('/v1/accounts/self/')
