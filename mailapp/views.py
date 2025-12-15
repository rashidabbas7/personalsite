from django.shortcuts import render
import json
from django.core.mail import EmailMessage
from django.http import HttpResponse
def home(request):
    if request.method=="GET":
        return render(request,'mails/mailtemp.html')
    else:
        body=json.loads(request.body)
        name=body.get("name")
        message=body.get("message")
        emailaccount=body.get("email")
        subject=body.get("subject")
        email=EmailMessage(
            subject=subject+"by "+name,
            body=message,
            to=['rashidabbasalq777@gmail.com'],

            reply_to=[emailaccount]
            
            
        )
        email.send()
        return render(request,'mails/mailtemp.html')

    