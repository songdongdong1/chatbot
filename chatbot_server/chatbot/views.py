from django.shortcuts import render

# Create your views here.
# chatbot/views.py
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . google.init import google_api
import json

ai_client = google_api.client


@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data['message']

        messages = [
            {"role": "user", "content": user_message},
        ]
        chat_completion = google_api_client.getResponse((
            messages=messages,
            model="gpt-3.5-turbo",
        )
        bot_response = chat_completion.choices[0].message.content

        return JsonResponse({'message': bot_response})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)