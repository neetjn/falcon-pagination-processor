import falcon
from falcon_pagination_processor import PaginationProcessor
from tests.falcon.resources import TestResourceCollection


api = falcon.API(middleware=[PaginationProcessor()])
api.add_route(TestResourceCollection.route, TestResourceCollection())
