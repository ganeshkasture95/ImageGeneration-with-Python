import os
import openai

openai.api_key = 'Your Open Ai key here'

users_prompt = input("enter the promt")
responce = openai.Image.create(
    prompt = users_prompt,
    n=1,
    size="1024x1024"
)

# image_url = responce['data'][0]['url']
# print(image_url)

#     image_url = responce['data'][0]['url']
#     print(image_url)
#     responce = requests.get(image_url)
#     image = Image.open(io.BytesIO(responce.content))
#     image = ImageTk.PhotoImage(image)
    
#     canves.image = image
#     canves.create_image(0,0,anchor = 'nw',image = image)
