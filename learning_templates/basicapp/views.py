from django.shortcuts import render

# Create your views here.
def index(request):
  context_dict = {'txt1': 'This is txt1;next1;next2', 'num1':100}
  return render(request, 'basicapp/index.html', context=context_dict)

def other(request):
  return render(request, 'basicapp/other.html')

def relative(request):
  return render(request, 'basicapp/rel_url_templates.html')

def page1(request):
  return render(request, 'basicapp/page1.html')

def main1(request):
  return render(request, 'basicapp/main1.html')
