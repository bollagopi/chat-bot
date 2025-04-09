Api_key="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"
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=Ask-or-v1-13bb240c25ba847d753d42aedcb3975737a5c9f63efe2a65dac95546a2b73261,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  model="google/gemini-2.0-flash-lite-preview-02-05:free",
  messages=[
    {
      "role": "user",
      "content": "who is good chat gpt or gemini"
    }
  ]
)

print(completion.choices[0].message.content)