from django.shortcuts import render, redirect
import smtplib

# Create your views here.
def index(request):
    if "subform" in request.POST:
        try:
            email = request.POST['contact-email']
        except MultiValueDictKeyError:
            email = ""
        mailserver = smtplib.SMTP('smtp.office365.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login('no-reply@quanch.io', 'Jr91766jr')
        message = """From: Autoresponder <no-reply@quanch.io>
To: Juan Rodriguez  <jrodriguez@paradisum.io>
MIME-Version: 1.0
Content-type: text/html
Subject: New Signup User

A user has entered their email address to be signed up for the newsletter in the Coming Soon page:<br><br>
Email: """ + email + """<br><br>

Sincerely,<br>
Paradisum
"""
        mailserver.sendmail('no-reply@quanch.io', 'jrodriguez@paradisum.io', message)
        mailserver.quit()
        return redirect('/complete')
    if 'thememode' not in request.session:
        request.session['thememode'] = "Dark"
    if request.session['thememode'] == "Dark":
        return render(request, 'default/index.html')
    if request.session['thememode'] == "Light":
        return render(request, 'default/indexlight.html')

def light(request):
    request.session['thememode'] = "Light"
    return redirect('/')

def dark(request):
    request.session['thememode'] = "Dark"
    return redirect('/')

def complete(request):
    if request.session['thememode'] == "Dark":
        return render(request, 'default/complete.html')
    if request.session['thememode'] == "Light":
        return render(request, 'default/completelight.html')