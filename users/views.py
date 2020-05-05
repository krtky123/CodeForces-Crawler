from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import models


from bs4 import BeautifulSoup
import requests
from lxml import html

import pandas as pd
import matplotlib.pyplot as plt, mpld3


from collections import OrderedDict



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    # template_name = 'users/signup.html'

