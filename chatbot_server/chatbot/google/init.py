
from google import genai

class google_api:
    def __init__(self):

        self.client = genai.Client(api_key="AIzaSyCrfqJ1IMy39KIz-1pAxem4r8CRdsCdz_Q")


    def getResponse(self, queryText):

        print(queryText)

        response = self.client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = queryText)
        return response.text





