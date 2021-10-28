from django.http.response import HttpResponse
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
  user = request.user
  all_pins = Pin.objects.all()
  locations = []
  for pin in all_pins:
    for data in pin.user.all():
      temp = [pin.lat,pin.long,data.id,pin.id,data.username,pin.name]
      locations.append(temp)
  return render(request, 'home.html', {'locations' : locations, 'userid':user.id, 'key': os.getenv('GOOGLE_MAPS_API_KEY')})

@login_required
def pins_index(request):
  user = request.user
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
      temp = [pin.lat,pin.long,data.id,pin.id,data.username,pin.name]
      locations.append(temp)
  return render(request, 'pins/index.html', { 'pins': all_pins,'userid':user.id,'locations' : locations,'key': os.getenv('GOOGLE_MAPS_API_KEY') })

@login_required
def pins_show(request, pin_id):
    pin = Pin.objects.get(id = pin_id)
    userid = request.user.id
    for data in pin.user.all():
      pinid = data.id
    # address validation
    if pin.lat == 0 and pin.long == 0:
      # invalid address
      return render(request, 'pins/address_validation.html', {'pin': pin, 'pin_id': pin_id})
    else:
      # valid address
      return render(request, 'pins/show.html', { 'pin': pin,'userid': userid,'pinid':pinid, 'key': os.getenv('GOOGLE_MAPS_API_KEY') })

class PinCreate(LoginRequiredMixin, CreateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note']
  #success_url = '/pins/'

  def form_valid(self, form):
    pin = form.save()
    #geocoding
    lat, long, address = extract_latlong(pin.address)
    print('lat', lat, 'long', long)
    pin.lat = lat
    pin.long = long
    pin.address = address
    pin.user.add(self.request.user.id)
    return super().form_valid(form)

class PinUpdate(LoginRequiredMixin, UpdateView):
  model = Pin
  fields = ['name', 'address', 'date', 'purpose', 'rating', 'note']

  def form_valid(self,form):
    pin = form.save()
    #geocoding
    lat,long,address = extract_latlong(pin.address)
    pin.lat = lat
    pin.long = long
    pin.address = address
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
  lat,long = 0, 0
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
    address = results['formatted_address']
  except:
    pass
  return lat,long,address

def hidden(request):
  return render(request, 'hidden.html', {'key': os.getenv('GOOGLE_MAPS_API_KEY')})
