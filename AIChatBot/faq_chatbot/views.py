from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from faq_chatbot.nlp import OpenAI_API
from faq_chatbot.models import FAQs


class ChatBotView(APIView):
    open_api = OpenAI_API()

    def post(self, request, *args, **kwargs):
        user_question = request.data.get('user_input')

        question_embedding = self.open_api.get_embedding(user_question)
        most_similar = FAQs.search_db_by_vector(question_embedding)
        
        
        reply = most_similar.answer

        return Response({'reply': reply}, status=status.HTTP_200_OK)