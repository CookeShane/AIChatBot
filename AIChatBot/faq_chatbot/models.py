from django.db import models
from pgvector.django import VectorField, L2Distance, IvfflatIndex

# Create your models here.
class FAQs(models.Model):
    """
    FAQs model to store frequently asked questions and their answers.

    Attributes:
        category (CharField): The category of the FAQ, with choices including 'General Queries', 'The Challenge', and 'The Funded Account'.
        question (TextField): The text of the question.
        answer (TextField): The text of the answer.
        embedding (VectorField): A vector representation of the question for similarity search.

    Methods:
        search_db_by_vector(query_vector):
            Searches the database for the closest matching FAQ based on the provided query vector.
            Args:
                query_vector (list): The vector representation of the query.
            Returns:
                FAQs: The closest matching FAQ if the distance is less than or equal to 0.55.
                str: A message indicating no match was found if the distance is greater than 0.55.

        __str__():
            Returns the question text as the string representation of the FAQ.
    """
    class Meta:
        db_table = 'faqs'
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

        indexes = [
            IvfflatIndex(fields=['embedding'])
        ]

    categories = [('general', 'General Queries'), ('challenge', 'The Challenge'), ('funded', 'The Funded Account')]

    category = models.CharField(max_length=100, choices=categories, null=True)
    question = models.TextField()
    answer = models.TextField()
    embedding = VectorField(dimensions=1536)

    @classmethod
    def search_db_by_vector(cls, query_vector):
        """
        Searches the database for the closest matching FAQ based on the provided query vector.

        Args:
            query_vector (list): The vector representation of the query.

        Returns:
            FAQs: The closest matching FAQ if the distance is less than or equal to 0.55.
            str: A message indicating no match was found if the distance is greater than 0.55.
        """
        closest_match = cls.objects.annotate(distance=L2Distance('embedding', query_vector)).order_by('distance').first()

        if closest_match.distance <= 0.55:
            return closest_match
        else:
            return cls.objects.get(id='1')


    def __str__(self):
        return self.question