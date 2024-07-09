from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from faq_chatbot.nlp import OpenAI_API
from faq_chatbot.models import FAQs


class ChatBotView(APIView):
    """
    API view for handling chatbot interactions.

    This view receives user input (a question) and returns a response based on the most similar
    pre-defined answer from a database. It uses an embedding-based search to find the closest match.

    Attributes:
        open_api (OpenAI_API): An instance of the OpenAI_API class for handling embeddings.
    """
    open_api = OpenAI_API()

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for chatbot interactions.

        Args:
            request (Request): The incoming HTTP request containing user input.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response containing the chatbot's reply.
        """
        user_question = request.data.get('user_input')

        question_embedding = self.open_api.get_embedding(user_question)
        most_similar = FAQs.search_db_by_vector(question_embedding)
        
        
        reply = most_similar.answer

        return Response({'reply': reply}, status=status.HTTP_200_OK)