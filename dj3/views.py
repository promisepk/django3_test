from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def auth(request):
    user = request.resource_owner
    print('user:'+user.username)
    pass
    return HttpResponse(None)


#class ApiEndpoint(ProtectedResourceView):
 #   def get(self, request, *args, **kwargs):
  #      return HttpResponse('Hello, OAuth2!')



@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!'+request.user.username, status=200)