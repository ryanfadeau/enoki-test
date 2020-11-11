from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CalendarForm
import calendar
import pandas
from django.utils.dateparse import parse_date
from .calendars import FrBusinessCalendar
from .models import User
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #log le user dans django
            login(request, user)
            return redirect('calendar')
    else:
        form = AuthenticationForm()
        
    return render(request, 'user/login.html', {'form': form})

@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return redirect('login')

def create_calendar(from_date, to_date, custom_cal):    
    fr_calendar = FrBusinessCalendar()
    # jours fériés français
    public_holidays = fr_calendar.holidays(start=from_date, end=to_date).to_list()
    date_range = pandas.date_range(start=from_date, end=to_date)
    for date in date_range:
        day_name = calendar.day_name[date.weekday()]
        if day_name in custom_cal:
            custom_cal[day_name] += 1
        
        if date in public_holidays:
            if day_name == 'Sunday':
                custom_cal['public_day_sunday'] += 1
            else:
                custom_cal['public_day'] += 1
    return custom_cal

@login_required(login_url='login/')
def calendar_view(request):
    form = CalendarForm
    custom_cal = {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0,
        'public_day': 0,
        'public_day_sunday': 0
    }
    if request.method == 'POST':
        from_date = parse_date(request.POST['from_date'])
        to_date = parse_date(request.POST['to_date'])
        custom_cal = create_calendar(from_date, to_date, custom_cal)
    return render(request, 'user/calendar.html', {'form':form, 'calendar':custom_cal})

class create_user_view(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/create_user.html'
    form_class = CustomUserCreationForm
    success_message = "%(username)s was created successfully"

    def get_success_url(self):
        return reverse('login')
