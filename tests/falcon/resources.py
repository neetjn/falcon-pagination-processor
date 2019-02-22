import json

Resources = [{'_id': n, 'name': 'test_resource_{}'.format(n)} for n in range(10)]


def get_resources(start, count):
    """Get paginated list of resources"""
    if start and count:
        return Resources[start:start+count]
    return Resources


class TestResourceCollection(object):

    route = '/test/collection/'

    def on_get(self, req, resp):
        pagination = req.context.get('pagination')
        resp.body = json.dumps(get_resources(
            start=pagination.get('start'),
            count=pagination.get('count')))
