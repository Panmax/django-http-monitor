import json

from django.http import HttpResponse

from http_monitor.models import Request


def request_raw(request, request_id):
    content = Request(request_id=request_id).get_conent()
    return HttpResponse(content, content_type='text/html')


def request(request, request_id):
    result = Request(request_id=request_id).get_request()
    return HttpResponse(json.dumps(result), content_type='application/json')


def requests(request):
    size = int(request.GET.get('size', 20))
    page = int(request.GET.get('page', 1))

    http_requests = Request().get_requests(size=size, page=page)
    return HttpResponse(json.dumps(http_requests), content_type='application/json')
