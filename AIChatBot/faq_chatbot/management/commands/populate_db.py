from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from pathlib import Path
from faq_chatbot.models import FAQs
from faq_chatbot.nlp import OpenAI_API
import os

class Command(BaseCommand):
    help = 'Populate the FAQs table in faq_db with initial FAQ & Answers'

    def handle(self, *args, **kwargs):
        faqs_dir = os.path.join(settings.BASE_DIR, 'FAQs')
        open_api = OpenAI_API()
        data = []

        categories = {
            'general': 'General Queries',
            'challenge': 'The Challenge',
            'funded': 'The Funded Account'
        }

        # Clear the existing FAQs in the database
        FAQs.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("SELECT setval(pg_get_serial_sequence('faqs', 'id'), 1, false)")


        for category_name, category_dir in categories.items():
            category_path = os.path.join(faqs_dir, category_dir)

            if os.path.exists(category_path) and os.path.isdir(category_path):
                for filename in os.listdir(category_path):
                    if filename.endswith('.txt'):
                        file_path = os.path.join(category_path, filename)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            lines = file.readlines()
                            question = lines[0].strip()
                            answer = '\n'.join(lines[1:]).strip()
                            embedding = open_api.get_embedding(question)
                            data.append({
                                'category': category_name,
                                'question': question,
                                'answer': answer,
                                'embedding': embedding
                            })
        
        # Add the custom message for when no FAQ matches
        if os.path.exists(faqs_dir) and os.path.isdir(faqs_dir):
            filepath = os.path.join(faqs_dir, 'custom_message.txt')
            with open(filepath) as file:
                custom_message = file.readlines()[0].strip()
        FAQs.objects.create(question='No Match', answer=custom_message, embedding=[0]*1536)
        
        # Add the new FAQs to the database
        for faq_data in data:
            FAQs.objects.create(
                category=faq_data['category'],
                question=faq_data['question'],
                answer=faq_data['answer'],
                embedding=faq_data['embedding']
            )