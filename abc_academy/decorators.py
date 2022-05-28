from django.shortcuts import redirect


def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if request.user in request:
            
            return func(request, *args, **kwargs)
        else:
            return redirect('admins:adminlogin')
            
    return wrap