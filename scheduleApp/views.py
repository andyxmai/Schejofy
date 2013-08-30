from django.shortcuts import render, redirect
from django.http import HttpResponse
from scheduleApp.models import User, Course, Membership
from django.utils.safestring import mark_safe
import json
from scheduleApp.forms import ProfileForm

def index(request):
	#return HttpResponse(html)
	return render(request, 'index.html')

def get_user_shopping(user):
	shopping = {}
	for m in user.membership_set.all():
		if m.is_shopping:
			shopping[m.course] = True
		else:
			shopping[m.course] = False
	return shopping

def chunks(l, n):
	""" Yield successive n-sized chunks from l.
	"""
	for i in xrange(0, len(l), n):
		yield l[i:i+n]

def home(request):
	#HOME_USER = User.objects.all()[0]
	#user = HOME_USER
	user = User.objects.create(first_name="Andy", last_name="Mai")
	courses = user.course_set.all()

	# get user's shopping classes
	shopping = get_user_shopping(user)

	all_courses = []
	allCourses = Course.objects.all()
	for course in allCourses:
		all_courses.append({"id":course.id, "name":course.name})
	all_courses = mark_safe(json.dumps(all_courses))
	return render(request, 'home.html', {'user':user, 'courses':courses, 'all_courses':all_courses, 'shopping':shopping})

def course(request, id):
	course = Course.objects.get(id=id)
	members_shopping = []
	for x in course.membership_set.all():
		temp = {}
		temp['id'] = x.user.id
		temp['name'] = x.user.first_name + ' ' + x.user.last_name
		if x.is_shopping:
			temp['is_shopping'] = True
		else:
			temp['is_shopping'] = False
		members_shopping.append(temp)
	#members = course.members.all()
	members_shopping = list(chunks(members_shopping, 3))
	print members_shopping
	return render(request, 'course.html', {'course':course, 'members_shopping':members_shopping})

def user(request, id):
	user = User.objects.get(id=id)
	courses = user.course_set.all()
	shopping = get_user_shopping(user)
	return render(request, 'user.html', {'user':user, 'courses':courses, 'shopping':shopping})

def add_course(request):
	course = Course.objects.get(id=request.POST['course_id'])
	user = User.objects.get(id=request.POST['user_id'])
	m = Membership(user=user, course=course)
	m.save()
	return HttpResponse('')

def remove_course(request):
	course = Course.objects.get(id=request.POST['course_id'])
	user = User.objects.get(id=request.POST['user_id'])
	m = Membership.objects.get(user=user, course=course)
	m.delete()
	return HttpResponse('')

def change_shopping(request):
	course = Course.objects.get(id=request.POST['course_id'])
	user = User.objects.get(id=request.POST['user_id'])
	m = Membership.objects.get(user=user, course=course)
	m.is_shopping = False if request.POST['is_shopping'] == '0' else True
	m.save()
	return HttpResponse('')

def register_form(request):
	return render(request, 'register_form.html')

def register(request):
	first_name = request.POST['firstName']
	last_name = request.POST['lastName']
	new_user = User.objects.create(first_name=first_name, last_name=last_name)
	return redirect('/home')

def profile(request):
	HOME_USER = User.objects.all()[0]
	user = HOME_USER
	if request.method == 'POST': # If the form has been submitted...
		form = ProfileForm(request.POST) # A form bound to the POST data
		user.year = request.POST.get('year')
		user.save()
		return render(request, 'profile.html', {'user':user, 'form':form, 'saved':True})
	else:
		form = ProfileForm(initial={'year':user.year}) # An unbound form

	return render(request, 'profile.html', {'user':user, 'form':form, 'saved':False,})

def search(request):
	if request.is_ajax():
	    q = request.GET['query']
	    users = User.objects.filter(first_name__icontains = q )[:20]
	    results = []
	    for user in users:
	        user_json = {}
	        user_json['id'] = user.id
	        user_json['name'] = user.first_name + ' ' + user.last_name
	        user_json['is_user'] = True
	        results.append(user_json)
	    courses = Course.objects.filter(name__icontains = q )[:20]
	    for course in courses:
	        course_json = {}
	        course_json['id'] = course.id
	        course_json['name'] = course.name
	        course_json['is_user'] = False
	        results.append(course_json)
	    data = json.dumps(results)
	else:
	    data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)