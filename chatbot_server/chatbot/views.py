from django.shortcuts import render

# Create your views here.
# chatbot/views.py
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . google.init import google_api
import json

ai_client = google_api()



@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data['message']

        messages = [
            {"role": "user", "content": user_message},
        ]
        chat_completion = ai_client.getResponse(
            queryText= user_message,
        )
        #bot_response = chat_completion.choices[0].message.content
        bot_response = chat_completion

        return JsonResponse({'message': bot_response})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)