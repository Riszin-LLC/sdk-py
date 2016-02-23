# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function

from predicthq.endpoints.base import BaseEndpoint
from predicthq.decorators import accepts, returns

from .schemas import SearchParams, EventResultSet


class EventsEndpoint(BaseEndpoint):

    @accepts(SearchParams)
    @returns(EventResultSet)
    def search(self, **params):
        return self.client.get('/v1/events', params=params)

    @accepts(SearchParams)
    def count(self, **params):
        return self.client.get('/v1/events/count/', params=params).get('count')
