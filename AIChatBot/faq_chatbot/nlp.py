from openai import OpenAI
from django.conf import settings


class OpenAI_API():
    """
    A class to interact with the OpenAI API.

    Attributes
    ----------
    embedding_model : str
        The model used for generating embeddings.
    client : OpenAI
        The OpenAI client initialized with the API key from Django settings.

    Methods
    -------
    get_embedding(prompt: str) -> list:
        Generates an embedding for the given prompt using the specified model.
    """
    embedding_model = 'text-embedding-ada-002'
    client = OpenAI(
        api_key = settings.OPENAI_API_KEY
    )

    def get_embedding(self, prompt):
        """
        Generates an embedding for the given prompt.

        Parameters
        ----------
        prompt : str
            The input text for which the embedding is to be generated.

        Returns
        -------
        list
            A list representing the embedding of the input text.
        """
        prompt = prompt.replace("\n", " ")

        response = self.client.embeddings.create(
            model = self.embedding_model,
            input = prompt, 
            encoding_format = 'float'
        )

        return response.data[0].embedding