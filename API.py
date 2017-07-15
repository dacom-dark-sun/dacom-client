import slumber


class _CustomResourse(slumber.Resource):
    def _request(self, *args, **kwargs):
        try:
            return super()._request(*args, **kwargs)
        except slumber.exceptions.HttpClientError as e:
            if hasattr(e, 'content'):
                # TODO Change exception message
                print(e.content.decode())

            raise


class API(slumber.API):
    resource_class = _CustomResourse

    def __init__(self, *args, **kwargs):
        api_key = kwargs.pop('api_key', None)

        super().__init__(*args, **kwargs)

        if api_key:
            self._store['session'].headers['Api-Key'] = api_key
