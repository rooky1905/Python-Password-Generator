from django.shortcuts import render
import random
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def password(request):
    letter = list('abcdefghijklmnopqrstuvwxyz')
    upper_letter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_char = list('!@#$%^&*()<>?":_~')
    len = int(request.GET.get('length'))
    u = request.GET.get('upper')
    s = request.GET.get('special')
    
    passw =''

    if u == 'on' and s == 'on':
        for i in range (len):
            passw += random.choice(letter+upper_letter+special_char)

    else:
        if u == 'on':
            for i in range (len):
                passw += random.choice(letter+upper_letter)
        
        elif s == 'on':
            for i in range (len):
                passw += random.choice(letter+special_char)

        else:
            for i in range (len):
                passw += random.choice(letter)
            


    messages.success(request, ('Password has been created successfully'))
    return render(request, 'password.html', {'password' : passw})
