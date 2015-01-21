from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from make_friends.register import RegistrationForm, LoginForm
from make_friends.models import User
from django.template import RequestContext
from django import forms
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fx = form.save(commit=False)
            fx.set_password(request.POST['password'])
            fx.save()
            return HttpResponseRedirect('/login/')
        else:
            return render_to_response('register.html', {'form' : form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def login_work(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/account/')
    else:    
        if request.method == 'POST':
                form = LoginForm(request.POST)
                print "hello"
                if True:
                        username = request.POST['username']
                        password = request.POST['password']
                        flag = authenticate(username=username, password=password)
                        
                        if flag is not None:
                            login(request, flag)
                            current_user = request.user
                            current_user.loggedin = True
                            return HttpResponseRedirect('account/')
                        else:
                            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))

def account(request):
    current_user = request.user
    return render(request, 'account.html', {'user_name' : current_user.username})
