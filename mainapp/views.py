from .models import Pin
from django.shortcuts import redirect, render
from django.contrib.auth import base_user, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
import os,requests
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def home(request):
  all_pins = Pin.objects.all()
  locations = []
  for pin in all_pins:
    for data in pin.user.all():
      temp = [pin.lat,pin.long,data.id]
      locations.append(temp)
  return render(request, 'home.html', {'locations' : locations, 'key': os.getenv('GOOGLE_MAPS_API_KEY')})

@login_required
def pins_index(request):
  sort_by = None
  try:
    sort_by = request.POST['sortby']
  except:
    sort_by = "date"
  print("sort_by", sort_by)
  if sort_by == "name":
    all_pins = Pin.objects.filter(user=request.user).order_by('name')
  else:
    all_pins = Pin.objects.filter(user=request.user).order_by('-date')
  locations = []
  for pin in all_pins:
    for data in pin.user.all():
      temp = [pin.lat,pin.long,data.id]
      locations.append(temp)
  return render(request, 'pins/index.html', { 'pins': all_pins,'locations' : locations,'key': os.getenv('GOOGLE_MAPS_API_KEY') })

@login_required
def pins_show(request, pin_id):
    pin = Pin.objects.get(id = pin_id)
    return render(request, 'pins/show.html', { 'pin': pin, 'key': os.getenv('GOOGLE_MAPS_API_KEY') })

class PinCreate(LoginRequiredMixin, CreateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note']
  #success_url = '/pins/'

  def form_valid(self, form):
    pin = form.save()
    #geocoding
    lat,long = extract_latlong(pin.address)
    pin.lat = lat
    pin.long = long
    pin.user.add(self.request.user.id)
    return super().form_valid(form)

class PinUpdate(LoginRequiredMixin, UpdateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note']

  def form_valid(self,form):
    pin = form.save()
    #geocoding
    lat,long = extract_latlong(pin.address)
    pin.lat = lat
    pin.long = long
    return super().form_valid(form)


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

def extract_latlong(address):
  #if error return none and none
  lat,long = None, None
  api_key = os.getenv('GOOGLE_MAPS_API_KEY')
  base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
  endpoint = f"{base_url}{address}&key={api_key}"
  response = requests.get(endpoint)
  if response.status_code not in range(200,299):
    return None,None
  try:
    results = response.json()['results'][0]
    lat = results['geometry']['location']['lat']
    long = results['geometry']['location']['lng']
  except:
    pass
  return lat,long

