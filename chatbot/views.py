from django.shortcuts import render

# Create your views here.
from .utils.langgraph_tool import process_message

def home(request):
    return render(request, 'home.html')

def chat(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = process_message(user_input)
    return render(request, 'home.html', {'response': response})
