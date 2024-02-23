import os

import requests
import base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
DIFFUSION_API_KEY = os.getenv("DIFFUSION_API_KEY")

def generate_image_prompt(local_file_path, prompt, negative_prompt, width, height):
  api_url = "https://stablediffusionapi.com/api/v3/img2img"
  api_key = DIFFUSION_API_KEY

  with open(local_file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

  payload = {
    "key": api_key,
    "prompt": prompt,
    "negative_prompt": negative_prompt if negative_prompt else "blurry",
    "init_image": encoded_string,
    "width": width,
    "height": height,
    "samples": 1,
    "num_inference_steps": 30,
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "guidance_scale": 7.5,
    "strength": 0.7,
    "base64": "yes",
    "seed": None,
    "webhook": None,
    "track_id": None
  }

  response = requests.post(api_url, json=payload)
  if response.status_code == 200:
    jsonResponse = response.json()
    status = jsonResponse.get("status")
    if status in ["failed", "error"]:
      print(jsonResponse.get("message"))
    else:
      image_url = jsonResponse["output"][0]
      image_response = requests.get(image_url)
      if image_response.status_code == 200:
        image_data = base64.b64decode(image_response.text)
        output_path = Path("generated-image.jpg")
        with open(output_path, "wb") as f:
          f.write(image_data)
          print(f"Downloaded and decoded image saved to: {output_path}")

      else:
        print("Unexpected response code:", response.status_code)


if __name__ == "__main__":
  company_name = "knife Inc"
  company_description = "A sharp knife for home use,A sharp knife for home use"
  target_audience = "house hold"
  prompt = "Keep the main items in the original picture, and change the background of the picture to Christmas style."

  local_file_path = r"F:\my_file\my_photo\knife\a-knife-on-desk-with-fruit.jpg"
  generate_image_prompt(local_file_path, prompt, None, 512, 512)
