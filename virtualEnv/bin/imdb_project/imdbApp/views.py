from django.shortcuts import render

from imdbpie import Imdb

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

from datetime import datetime

from imdbApp.forms import UserForm, UserProfileForm



## creating an instance of Imdb()
imdb = Imdb()



def user_login(request):

	context_dict={}

	top250=imdb.top_250()

	lst=[]

	for i in top250:
		for k, v in i.items():
			if k=="title":
				lst.append(v)

	context_dict['moviesTop250']=lst


	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username, password=password)

		if user:

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/imdbApp/dashboard")
			else:
				return HttpResponse("Your Rango account is disabled")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid Login details supplied")
	else:
		return render(request, 'imdbApp/login.html', context_dict)


@login_required
def restricted(request):
	return HttpResponse("")


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/imdbApp/login")



def dashboard(request):
	context_dict={}

	if request.method=="POST":
		username=request.POST.get('username')
		context_dict['user']=username
	else:
		print("none")

	return render(request, 'imdbApp/dashboard.html', context_dict)





def register(request):

	registered=False

	if request.method=="POST":
		 user_form=UserForm(data=request.POST)
		 profile_form=UserProfileForm(data=request.POST)


		 if user_form.is_valid() and profile_form.is_valid():
		 	user=user_form.save()
		 	user.set_password(user.password)
		 	user.save()

		 	profile=profile_form.save(commit=False)
		 	profile.user=user

		 	profile.save()
		 	registered=True
		 else:
		 	print user_form.errors, profile_form.errors
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()

	return render(request, 'imdbApp/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


      

def movie_search(request):

	context_dict={}
	if request.method=="POST":
		movie_title=request.POST.get('movie_name')
		context_dict['movie_name']=movie_title
		print(movie_title)  ## test_code to print movie_title
	
	def inner_func(**kwargs):
		dict_x={}
		for i, v in kwargs.items():
			dict_x[i]=v
		return dict_x

	list_1=[]
	list_2=[]


	movie_details = imdb.search_for_title(movie_title)

	context_dict["movie_details"]=movie_details

	return render(request, 'imdbApp/movie_info.html', context_dict)


