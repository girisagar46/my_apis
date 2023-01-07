import datetime

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import get_top_billionares


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


@api_view(['GET'])
def real_time(request):
    billionares = get_top_billionares()
    return Response(billionares)
