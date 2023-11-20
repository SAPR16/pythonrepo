def application(environ, start_response):
 status = '200 0K'
 output = b'Hello this is a CICD for python Power Web App!!'
 response_headers = [('Content-type', 'text/plain'),
 ('Content-Length', str(len(output)))]
 start_response(status, response_headers)
 return [output]
