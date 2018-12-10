class XooaPendingException(Exception):
    def __init__(self, result_id, result_url):

        # Call the base class constructor with the parameters it needs
        super(XooaPendingException, self).__init__({'result_url': result_url, 'result_id': result_id})

        # self.errors = errors


class XooaRequestTimeoutException(Exception):
    def __init__(self, result_id, result_url):

            super(XooaRequestTimeoutException, self).__init__({'result_url': result_url, 'result_id': result_id})

        # self.errors = errors


class XooaApiException(Exception):
    def __init__(self, message, errors):

        super(XooaApiException, self).__init__({'error_code': errors, 'error_message': message})

        # self.errors = errors


class InvalidParameterException(Exception):
    def __init__(self):

        super(InvalidParameterException, self).__init__({'error_message': 'Invalid Parameter'})

        # self.errors = errors
