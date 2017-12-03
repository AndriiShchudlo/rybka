from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from rest_framework import serializers

from app.models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class User_reg_log(object):
    def registry_user(self, request):
        fname = request.POST.get('first_name_reg', '')
        lname = request.POST.get('last_name_reg', '')
        email = request.POST.get('email_reg', '')
        pass1 = request.POST.get('pass1_reg', '')
        res = UserSerializer(data={'username': email, "password": pass1})
        if res.is_valid():
            user = User.objects.create(
                username=email
            )
            user.set_password(pass1)
            user.save()
            UserData.objects.create(
                user=user,
                first_name=fname,
                last_name=lname
            )
            return True, None
        return False, res.errors




    def login_in_system(self, request):
        args = {}
        args.update(csrf(request))
        if request.POST:
            email = request.POST.get('user_login', '')
            password = request.POST.get('pass_login', '')
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')  # TODO Вивести кабінет
            else:
                args['login_error'] = "Користувача з такими даними не існує"
                redirect('/')
                return render_to_response('index.html', args)
        else:
            return redirect('/')
