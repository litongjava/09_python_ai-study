import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()
DIFFUSION_API_KEY = os.getenv("DIFFUSION_API_KEY")

url = "https://stablediffusionapi.com/api/v5/removebg_mask"

src_image = "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_inpaint/boy.png"
payload = json.dumps({
  "key": DIFFUSION_API_KEY,
  "seed": 12345,
  "image": src_image,
  "post_process_mask": False,
  "only_mask": False,
  "alpha_matting": False,
  "seed": None,
  "webhook": None,
  "track_id": None
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
