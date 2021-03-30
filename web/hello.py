def wsgi_application(environ, start_response):
    status = "200 OK"
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8')
    ]
    body = [bytes(i+'\n', 'ascii') for i in  environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body
