class PaginationProcessor(object):

    def process_request(self, req, resp):
        start = req.params.get('start')
        if start and start.isdigit():
            start = int(start)
        count = req.params.get('count')
        if count and count.isdigit():
            count = int(count)
        req.context.setdefault('pagination', {
            'start': start,
            'count': count})
