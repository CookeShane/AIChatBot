from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from faq_chatbot.forms import UserQuestionForm
from faq_chatbot.nlp import OpenAI_API
from faq_chatbot.models import FAQs

class HomeView(FormView):
    """
    View to handle the home page with a form for user questions.

    Attributes:
        template_name (str): The path to the template used for rendering the view.
        form_class (Form): The form class used for handling user questions.
        open_api (OpenAI_API): An instance of the OpenAI_API class for generating embeddings.
        success_url (str): The URL to redirect to upon successful form submission.

    Methods:
        form_valid(form):
            Processes the form when it is valid.
            Args:
                form (UserQuestionForm): The validated form instance.
            Returns:
                HttpResponse: The rendered response with the context including the user's question and the most similar FAQ or a custom message.
    """
    template_name = 'faq_chatbot/home.html'
    form_class = UserQuestionForm
    open_api = OpenAI_API()
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user_question = form.cleaned_data['question']
        question_embedding = self.open_api.get_embedding(user_question)
        most_similar = FAQs.search_db_by_vector(question_embedding)

        context = {
            'form': form,
            'user_question': user_question,
            'most_similar': most_similar if isinstance(most_similar, FAQs) else None,
            'custom_message': most_similar if isinstance(most_similar, str) else None
        }

        return self.render_to_response(context)
