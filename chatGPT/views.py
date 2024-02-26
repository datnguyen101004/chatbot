from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

genai_api_key = "AIzaSyByzOKaQBWNuhGGzz29lsfcE5x0SQuOYcM"

genai.configure(api_key=genai_api_key)
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

model = genai.GenerativeModel("gemini-pro",
                              generation_config = generation_config)


def ask_openai(message):
    response = model.generate_content([message])
    print(response.text)
    return response.text

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({
            'message': message,
            'response': response
        })
    return render(request, 'chatbot.html')
