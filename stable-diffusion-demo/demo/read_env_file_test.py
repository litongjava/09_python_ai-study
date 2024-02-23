import os

from dotenv import load_dotenv

load_dotenv()
DIFFUSION_API_KEY = os.getenv("DIFFUSION_API_KEY")
print(DIFFUSION_API_KEY)
