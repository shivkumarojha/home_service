from django.shortcuts import render
from . forms import EnquiryForm
from django.http import HttpResponse
from .models import ContactInfo, ServiceTypes, Newsletter, Team, ClientQuotes, Project, Tag, Message

# Home page of website
def index(request):
    contact_info = ContactInfo.objects.get(id=1)
    services = ServiceTypes.objects.all()
    
    form = EnquiryForm
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/thank_you.html')
    context = {
        'form': form,
        'contact_info': contact_info,
        'services': services,
    }
    return render(request, 'services/index.html', context)

# About view
def about(request):
    contact_info = ContactInfo.objects.get(id=1)
    services = ServiceTypes.objects.all()
    teams = Team.objects.all()
    client_quotes = ClientQuotes.objects.all()
    
    context = {
        'services': services,
        'teams': teams,
        'client_quotes': client_quotes,
        'contact_info': contact_info,
    }
    return render(request, 'services/about.html', context)

# Services view
def services(request):
    services = ServiceTypes.objects.all()
    contact_info = ContactInfo.objects.get(id=1)
    context = {
        'contact_info': contact_info,
        'services': services
    }
    return render(request, 'services/services.html', context)

#Projects view
def projects(request):
    services = ServiceTypes.objects.all()
    contact_info = ContactInfo.objects.get(id=1)
    project = Project.objects.all()
    tag = Tag.objects.all()
    
    context = {
        'contact_info': contact_info,
        'services': services,
        'tag':tag,
        'project': project,
    }
    return render(request, 'services/projects.html', context)

# Plans View
def plans(request):
    services = ServiceTypes.objects.all()
    contact_info = ContactInfo.objects.get(id=1)
    context = {
        'contact_info': contact_info,
        'services': services
    }
    return render(request, 'services/plan.html', context)

# Contact Us view
def contact_us(request):
    services = ServiceTypes.objects.all()
    contact_info = ContactInfo.objects.get(id=1)
    context = {
        'contact_info': contact_info,
        'services': services
    }
    return render(request, 'services/contact.html', context)


# View for Privacy
def privacy(request):
    return render(request, 'services/privacy.html')

# View for terms
def terms(request):
    return render(request, 'services/terms.html')
    

# View for Newsletter subscription
def newsletter(request):
    email = request.POST['newsletter']
    try:
        email = Newsletter.objects.get(email=email)
        if email:
            message = 'You are already in our subsription list.'
        
    except:
        newsletter = Newsletter()
        print(email)
        newsletter.email = email
        newsletter.save()
        message = 'Thank you for signing up for our newsletter'
    context = {
    'message': message
        
    }
    return render(request, 'services/thank_you.html', context)
    
def send_message(request):
    message = Message()
    message.name = request.POST['name']
    message.email = request.POST['email']
    message.subject = request.POST['subject']
    message.save()
    return render(request, 'services/thank_you.html')
    
    