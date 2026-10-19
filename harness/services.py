import logging
from openai import OpenAI
from django.conf import settings

logger = logging.getLogger(__name__)

class DeepSeekService:
    def __init__(self):
        self.client = OpenAI(
            base_url = "http://api.deepseek.com",
            api_key = settings.DEEPSEEK_KEY
        )

    def getRisk(self, patient):
        prompt = (
           f"A prostate cancer patient has a "
           f"PSA level of {patient.psa_level} ng/ml a gleason score of "
           f"{patient.gleason_score} and a clinical stage of {patient.clinical_stage}."
           f"Using NCCN guidelines determine the risk stratification of the patient."
        )

        try:
            response = self.client.chat.completions.create(
                model="deepseek-flash", 
                messages=[
                    {"role": "system", "content": "Act as an expert oncologist."},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                reasoning_effort="high",
                extra_body={"thinking": {"type": "enabled"}},
                max_tokens=10000,
            )
            data = response.choices[0].message.content.strip()
            return data

        except Exception as e:
            logger.error(f"DeepSeek API Error: {e}")
            return "Unknown"

    def getTreatment(self, patient):
        prompt = (
           f"A prostate cancer patient has a "
           f"PSA level of {patient.psa_level} ng/ml a gleason score of "
           f"{patient.gleason_score} and a clinical stage of {patient.clinical_stage}."
           f"Using NCCN guidelines recommend a treatment path for the patient."
        )

        try:
            response = self.client.chat.completions.create(
                model="deepseek-flash", 
                messages=[
                    {"role": "system", "content": "Act as an expert oncologist."},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                reasoning_effort="high",
                extra_body={"thinking": {"type": "enabled"}},
                max_tokens=20000,
            )
            data = response.choices[0].message.content.strip()
            return data

        except Exception as e:
            logger.error(f"DeepSeek API Error: {e}")
            return "Unknown"

