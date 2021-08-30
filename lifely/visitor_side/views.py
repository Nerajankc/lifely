from django.shortcuts import render
from .models import Gallery
from .forms import FeedbackForm, NewsLetterForm


def index(request):
    photos = Gallery.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        form = FeedbackForm
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/index.html", {
        'form': form,
        'photos': photos,
        'newsletter_form': newsletter_form
    })


def about_us(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/about_us.html", {
        'newsletter_form': newsletter_form,
    })


def blog(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/blog.html", {
        'newsletter_form': newsletter_form,
    })


def privacy_policy(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/privacy_policy.html", {
        'newsletter_form': newsletter_form,
    })


def user_policy(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/user_policy.html", {
        'newsletter_form': newsletter_form,
    })


def terms_and_condition(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/terms_and_condition.html", {
        'newsletter_form': newsletter_form,
    })


def career(request):
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm
    return render(request, "visitor_side/career.html", {
        'newsletter_form': newsletter_form,
    })
