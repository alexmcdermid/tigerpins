from .models import Pin
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def home(request):
  return render(request, 'home.html', {'key': os.getenv('GOOGLE_MAPS_API_KEY')})

@login_required
def pins_index(request):
  all_pins = Pin.objects.filter(user=request.user)
  return render(request, 'pins/index.html', { 'pins': all_pins })

@login_required
def pins_show(request, pin_id):
    pin = Pin.objects.get(id = pin_id)
    return render(request, 'pins/show.html', { 'pin': pin, 'key': os.getenv('GOOGLE_MAPS_API_KEY') })

class PinCreate(LoginRequiredMixin, CreateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note', 'lat', 'long']
  success_url = '/pins/'

  def form_valid(self, form):
    pin = form.save()
    pin.user.add(self.request.user.id)
    return super().form_valid(form)

class PinUpdate(LoginRequiredMixin, UpdateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note']

class PinDelete(LoginRequiredMixin, DeleteView):
  model = Pin
  success_url = '/pins/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)