# from django.shortcuts import render

# # Create your views here.
# from chatbot.utils.langgraph_tool import process_message

# def home(request):
#     return render(request, 'home.html')

# def chat(request):
#     response = None
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         response = process_message(user_input)
#     return render(request, 'home.html', {'response': response})

# from django.shortcuts import render
# from .utils.langgraph_tool import process_message  # Groq integration

# def home(request):
#     response = None
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         chatbot = Chatbot()  # Initialize the chatbot
#         response = chatbot.chat(user_input)  # Get chatbot response

#     return render(request, 'home.html', {'response': response})



# -------------------------------------------------------------------------------->

# from django.shortcuts import render
# from chatbot.utils.langgraph_tool import process_message, get_memory
# import openai


# # Set your OpenAI API key
# openai.api_key = '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'

# def get_bot_response(user_input):
#     # Call the OpenAI API to generate a response
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Choose the engine you want (can be GPT-4, etc.)
#         prompt=user_input,
#         max_tokens=150,
#         n=1,
#         stop=None,
#         temperature=0.7
#     )
    
#     # Extract the response from the API and return it
#     bot_response = response.choices[0].text.strip()
#     return bot_response

# def home(request):
#     return render(request, 'home.html')

# def chat(request):
#     response = None
#     memory = None
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         response = process_message(user_input)
#         memory = get_memory()
#     return render(request, 'home.html', {'response': response, 'memory': memory})


# ---------------------------------------------------------------------------------------------


# def get_bot_response(user_input):
#     # Simple rule-based responses
#     responses = {
#         "hello": "Hi there! How can I help you?",
#         "how are you": "I'm just a bot, but I'm doing great! How can I assist you?",
#         "bye": "Goodbye! Have a great day!"
#     }

#     # Return a response based on user input
#     user_input = user_input.lower().strip()  # Normalize the input
#     return responses.get(user_input, "Hi there! How can I help you??")



# ?////////////////////////
# import os
# from django.shortcuts import render
# from chatbot.utils.langgraph_tool import process_message, get_memory, call_model, router_function


# def get_bot_response(user_input):

#     if user_input == ['Hello', 'Hi', 'Hey']:
#         return user_input

#     return process_message(user_input)  # Ensure `process_message` handles the input properly


# def home(request):
#     """
#     Render the home page.
#     """
#     # return render(request, 'home.html')
#     return render(request, 'home.html')

# def chat(request):
#     """
#     Handle chat interactions. Process user input and generate bot responses.
#     """
#     response = None
#     memory = None

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '').strip()
        
#         if user_input:  # Process only if input is not empty
#             response = get_bot_response(user_input)
#             memory = get_memory()  # Optional: Fetch memory if required
#         else:
#             response = "Please provide some input to start the chat."  # Friendly error message

#     return render(request, 'home.html', {'response': response, 'memory': memory})




# Ye sahi hay sab say 

# import os
# from django.shortcuts import render
# from chatbot.utils.langgraph_tool import process_message, get_memory, call_model, router_function

# def get_bot_response(user_input):
#     """Get bot response based on user input."""
#     if user_input == ['Hello', 'Hi', 'Hey']:
#         return user_input
#     return process_message(user_input)

# def home(request):
#     """Render the home page."""
#     return render(request, 'home.html')

# def chat(request):
#     """Handle chat interactions."""

#     response = None
#     memory = None

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '').strip()
        
#         if user_input:
#             response = get_bot_response(user_input)
#             # print(f"Chatbot response: {response}")  # Debugging 
#             memory = get_memory()
#         else:
#             response = "Please provide some input to start the chat."
            
#         return render(request, 'home.html', {'response': response, 'memory': memory})

#     return render(request, 'home.html')
   





# With html working ------------------->

import os
from django.shortcuts import render
from chatbot.utils.langgraph_tool import process_message, get_memory, call_model, router_function, call_tool
from django.http import JsonResponse

# In-memory chat history storage (replace with a database for production)
CHAT_HISTORY = []

def get_bot_response(user_input):
    """Get bot response based on user input."""
    # if user_input in ['Hello', 'Hi', 'Hey']:
    #     return user_input
    if user_input in ['Hello', 'Hi', 'Hey']:
        return process_message(user_input)
    return process_message(user_input)

def home(request):
    """Render the home page."""
    global CHAT_HISTORY
    return render(request, 'home.html')

def chat(request):
    """Handle chat interactions."""
    global CHAT_HISTORY
    response = None
    user_input = None
    memory = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()
        
        if user_input:
             # Append user message to chat history
            CHAT_HISTORY.append({'type': 'user', 'content': user_input})

            response = get_bot_response(user_input)
            memory = get_memory()

            # Append bot message to chat history
            CHAT_HISTORY.append({'type': 'bot', 'content': response})
        else:
            response = "Please provide some input to start the chat."
            
        return render(request, 'home.html', {'response': response, 'user_input': user_input, 'memory': memory, 'chat_history': CHAT_HISTORY})

    return render(request, 'home.html')


# With html working ------------------->










# from django.shortcuts import render
# from chatbot.utils.langgraph_tool import process_message, get_memory
# from django.http import JsonResponse

# CHAT_HISTORY = []

# def get_bot_response(user_input):
#     """Get bot response based on user input."""
#     if user_input in ['Hello', 'Hi', 'Hey']:
#         return user_input
#     return process_message(user_input)

# def home(request):
#     """Render the home page."""
#     global CHAT_HISTORY
#     return render(request, 'home.html')

# def chat(request):
#     """Handle chat interactions."""
#     global CHAT_HISTORY
#     response = None
#     user_input = None
#     memory = None

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '').strip()
        
#         if user_input:
#             # Append user message to chat history
#             CHAT_HISTORY.append({'type': 'user', 'content': user_input})

#             response = get_bot_response(user_input)
#             memory = get_memory()

#             # Append bot message to chat history
#             CHAT_HISTORY.append({'type': 'bot', 'content': response})
#         else:
#             response = "Please provide some input to start the chat."
            
#         return render(request, 'home.html', {'response': response, 'user_input': user_input, 'memory': memory, 'chat_history': CHAT_HISTORY})

#     return render(request, 'home.html')















# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from chatbot.utils.langgraph_tool import process_message, get_memory
# from django.views.decorators.csrf import csrf_protect  # CSRF protection instead of exempt

# def get_bot_response(user_input):
#     """Get bot response based on user input."""
#     try:
#         # Ensure that the response is properly fetched and is valid
#         return process_message(user_input)
#     except Exception as e:
#         # Log the error and return a generic error response
#         print(f"Error in processing message: {e}")
#         return "Error processing your request. Please try again later."

# def home(request):
#     """Render the home page."""
#     return render(request, 'home.html')

# @csrf_protect  # CSRF protection enabled for this view
# def chat(request):
#     """Handle chat interactions asynchronously."""
#     if request.method == 'POST':
#         try:
#             # Try to load the JSON data
#             data = json.loads(request.body)
#             user_input = data.get('user_input', '').strip()

#             if user_input:
#                 # Get response from bot and memory
#                 response = get_bot_response(user_input)
#                 memory = get_memory()
#                 return JsonResponse({'response': response, 'memory': memory})
#             else:
#                 return JsonResponse({'response': "Please provide some input to start the chat."}, status=400)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data in the request body.'}, status=400)
#         except Exception as e:
#             # Catch any other exceptions and log the error
#             print(f"Error in chat view: {e}")
#             return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)
    
#     # Return error if method is not POST
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)
















# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json
# from chatbot.utils.langgraph_tool import graph, State, MemorySaver

# memory = MemorySaver()

# # @csrf_exempt
# def home(request):
#     chat_history = request.session.get('chat_history', [])
#     return render(request, 'home.html', {'chat_history': chat_history})
#     # return render(request, 'home.html', {'chat_history': chat_history})

# @csrf_exempt
# def chat(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '')
#         chat_history = request.session.get('chat_history', [])
        
#         # Prepare initial state
#         state = {"messages": [{"type": "user", "content": user_input}], "ask_human": False}
        
#         # Process the state with the LangGraph
#         events = graph.stream(state, {}, stream_mode="values")
#         response = []
#         for event in events:
#             if "messages" in event:
#                 response = event["messages"]
        
#         # Update chat history
#         if response:
#             chat_history.append({"type": "user", "content": user_input})
#             chat_history.append({"type": "bot", "content": response[-1].content})
        
#         request.session['chat_history'] = chat_history
#         return render(request, 'home.html', {'chat_history': chat_history})



# def chat(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '')
#         chat_history = request.session.get('chat_history', [])
        
#         # Prepare initial state
#         import uuid
#         config = {
#             "configurable": {
#                 "thread_id": "1",
#                 "checkpoint_ns": " ",
#                 "checkpoint_id": str(uuid.uuid4())
#                 # "checkpoint_id": "0c62ca34-ac19-445d-bbb0-5b4984975b2a"
#             }
#         }
#         state = {"messages": [{"type": "user", "content": user_input}], "ask_human": False}
        
#         # Process the state with the LangGraph
#         events = graph.stream(state, config, stream_mode="values")
#         response = []
#         for event in events:
#             if "messages" in event:
#                 response = event["messages"]
        
#         # Update chat history
#         if response:
#             chat_history.append({"type": "user", "content": user_input})
#             chat_history.append({"type": "bot", "content": response[-1].content})
        
#         request.session['chat_history'] = chat_history
#         return render(request, 'home.html', {'chat_history': chat_history})
