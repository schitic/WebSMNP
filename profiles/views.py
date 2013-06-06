# Create your views here.
from django.http.response import HttpResponse

def test_variable(request):
  return HttpResponse(124)