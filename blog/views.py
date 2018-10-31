from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import ContactForm

# Create your views here.

def post_list_view(request):
	list_objects = Post.published.all()
	paginator = Paginator(list_objects, 3)
	page = request.GET.get("page")
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	posts = Post.published.all()
	return render(request, "blog/post/list.html", {"posts": posts} )
	
def post_detail_view(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status="published")
	# Fungerar ej, problem med Django 1.x vs. 2.x?
	# , publish__year=year, publish__month==month, publish__day=day
	return render(request, "blog/post/detail.html", {"post": post} )

def emailView(request):
	if request.method == "GET":
		form = ContactForm()

	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			from_email = form.cleaned_data["from_email"]
			name = form.cleaned_data["name"]
			message = form.cleaned_data["message"]
			
			try:
				send_mail(name, message, from_email, ["bzan96@gmail.com"])
			except BadHeaderError:
				return HttpResponse("Invalid header found.")
			return redirect("emailsuccess")
		
	return render(request, "blog/kontakt.html", {"form":form})

def successView(request):
	return HttpResponse("Tack för ditt meddelande! Jag återkommer så snart jag kan.")

def index(request):
	return render(request, "blog/index.html")

def wedding(request):
	return render(request, "blog/bröllop.html")

def fancy(request):
	return render(request, "blog/fancy.html")

def fransar(request):
	return render(request, "blog/fransar.html")

def om_mig(request):
	return render(request, "blog/om_mig.html")

def kontakt(request):
	return render(request, "blog/kontakt.html")

def emailsuccess(request):
	return render(request, "blog/emailsuccess.html")