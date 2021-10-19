def response_handler(response):
    return {
        'status': {
            'code': response.message.code,
            'message': response.message.message,
        },
        'result': response.body
    }
