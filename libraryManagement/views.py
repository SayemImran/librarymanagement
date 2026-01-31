from django.shortcuts import redirect

def root_api(request):
    return redirect('api-root')