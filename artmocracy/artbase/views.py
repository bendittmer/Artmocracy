from django.http import HttpResponse
from django.template import RequestContext, loader

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import UserProfile, Art, WinningArt, Picture, User
from forms import PhotoUploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import logging
import random

from django.views import generic

def home(request):
        return render(
		request, 'artbase/home.html')

def upload_picture(request, uid=None):
    """
    Photo upload / dropzone handler
    :param request:
    :param uid: Optional picture UID when re-uploading a file.
    :return:
    """
    form = PhotoUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        pic = request.FILES['file']
        # [...] Process whatever you do with that file there. I resize it, create thumbnails, etc.
        # Get an instance of picture model (defined below) 
        picture = Picture()      
        picture.file = pic
        picture.pic_id = Picture.objects.all().count()
        picture.save()
        return HttpResponse('Image upload succeeded.')
    return HttpResponseBadRequest("Image upload form not valid.")

def writings(request):
        if (request.POST.get('action') == 'Option A') or (request.POST.get('action') == 'Option B'):
                if request.POST.get('action') == 'Option A':
                        random_writing_number = request.POST['optionA']
                else:
                        random_writing_number = request.POST['optionB']
                what_was_voted_on = get_object_or_404(Art, art_id=random_writing_number)
	        what_was_voted_on.art_votes=what_was_voted_on.art_votes+1
	        what_was_voted_on.save()

        writings = Art.objects.filter(category="writings")
	number_of_writings=writings.count()
	random_writing_number= random.randint(1,number_of_writings-1)
	random_writing_number_two= random.randint(1,number_of_writings-1)
        while random_writing_number_two==random_writing_number:
                random_writing_number_two= random.randint(1, number_of_writings-1)
	option_a=writings[random_writing_number]	
	option_b=writings[random_writing_number_two]
	return render(request, 'artbase/writings.html', {'option_a':option_a, 
		'option_b':option_b,'random_writing_number':random_writing_number,
                'random_writing_number_two':random_writing_number_two})
def photography(request):
        photos = Art.objects.filter(category="photography")
	number_of_photos=photos.count() 
	random_photo_number= random.randint(1,number_of_photos-1)
	random_photo_number_two= random.randint(1,number_of_photos-1)
        while random_photo_number_two==random_photo_number:
                random_photo_number_two= random.randint(1, number_of_photos-1)
	option_a=photos[random_photo_number]	
	option_b=photos[random_photo_number_two]
	return render(request, 'artbase/photography.html', {'option_a':option_a, 
		'option_b':option_b,'random_photo_number':random_photo_number,
                'random_photo_number_two':random_photo_number_two})	
def submit(request):
	return render(
		request, 'artbase/submit.html')	
def pastwinners(request):
	return render(
		request, 'artbase/pastwinners.html')	
def submitwritings(request):
	return render(
		request, 'artbase/submitwritings.html')
def submitdrawings(request):
        return render(
		request, 'artbase/submitdrawings.html')
def submitphotography(request):
    form = PhotoUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
            pic = request.FILES['file']
            # [...] Process whatever you do with that file there. I resize it, create thumbnails, etc.
            # Get an instance of picture model (defined below) 
            picture = Picture()      
            picture.file = pic
            picture.pic_id = Picture.objects.all().count()
            picture.save()
            new_id=Art.objects.count()+1
	    phototext = picture.file
	    newphoto= Art(text=phototext, category="photography", art_id=new_id)
	    newphoto.save()
            return HttpResponse('Image upload succeeded.')
    return render(
	    request, 'artbase/submitphotography.html')

def submitstuff(request):
	new_writing_id=Art.objects.count()+1
	writingtext = request.POST.get('writings_submission') 
	newwriting= Art(text=writingtext, category="writings", art_id=new_writing_id)
	newwriting.save()
	return render(
		request, 'artbase/submitwritings.html')

def loginpage(request):
	return render(
		request, 'artbase/loginpage.html')	
def userlogin(request):

	username=request.POST.get('user_name')
	password=request.POST.get('password')
        logging.error(username)
        logging.error(password)
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request, user)
                return render(
		        request, 'artbase/home.html')
        else:
                return render(
		        request, 'artbase/home.html')     


def new_user_page(request):
	return render(
		request, 'artbase/new_user_page.html')	
def newuser(request):
	new_user_name = request.POST.get('new_user_name') 
	new_user_password = request.POST.get('new_user_password') 
        if User.objects.filter(username=new_user_name).exists():
                return HttpResponseRedirect("/")
        else:
	        user=User.objects.create_user(new_user_name, password=new_user_password)
	        login(request, user)
	        return render(
		        request, 'artbase/submit.html')	

def log_out(request):
        logout(request)
        return HttpResponseRedirect("/")
