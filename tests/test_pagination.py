from falcon.testing import TestCase
from tests.falcon.app import api
from tests.falcon.resources import Resources, TestResourceCollection


class TestPagination(TestCase):

    def setUp(self):
        super(TestPagination, self).setUp()
        self.app = api

    def test_pagination(self):
        # testing base resource
        collection_res = self.simulate_get(TestResourceCollection.route)
        self.assertEqual(collection_res.status_code, 200)
        collection = collection_res.json
        self.assertEqual(len(collection), len(Resources))
        # testing paginated request
        paginated_res = self.simulate_get(TestResourceCollection.route, params={
            'start': 5,
            'count': 5
        })
        self.assertEqual(paginated_res.status_code, 200)
        paginated = paginated_res.json
        self.assertEqual(len(paginated), 5)
        self.assertEqual(collection[5:10], paginated)
        # testing pagination bounds
        paginated_res = self.simulate_get(TestResourceCollection.route, params={
            'start': 9,
            'count': 10
        })
        self.assertEqual(paginated_res.status_code, 200)
        paginated = paginated_res.json
        self.assertEqual(len(paginated), 1)
        self.assertEqual(collection[9:10], paginated)
