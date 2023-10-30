import openai
import os
import customtkinter as ctk
import tkinter
from PIL import Image,ImageTk
import requests,io

# system settings---------- 

def generate():
    openai.api_key = 'your open ai key'
    users_prompt = prompt_entry.get('0.0',tkinter.END)
    users_prompt += "in style"+style_dropdowm.get()
    
    
    response = openai.Image.create(
        prompt = users_prompt,
        n=int(number_slider.get()),
        size="512x512"
    )
    
    image_urls=[]
    for i in range (len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    
    print(image_urls)
    
    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)
    
    def update_image(index = 0 ):
        canves.image = images[index]
        canves.create_image(0,0,anchor = 'nw',image = images[index])
        index = (index + 1) % len(images)
        canves.after(3000,update_image,index)
    
    update_image()
        


#  app frame -----------------

root = ctk.CTk()
root.title("GenImg")


input_frame = ctk.CTkFrame(root)
input_frame.pack(side ='left',expand = True,padx = 20 , pady = 20)

promt_lable = ctk.CTkLabel(input_frame,text="Prompt")
promt_lable.grid(
    row = 0,
    column = 0,
    padx = 10,
    pady = 10
)

prompt_entry = ctk.CTkTextbox(input_frame,height=10)
prompt_entry.grid(
    row = 0,
    column = 1,
    padx = 10,
    pady = 10
)

style_lable = ctk.CTkLabel(input_frame ,text='style')
style_lable.grid(row = 1,column = 0,padx=10,pady=10)

style_dropdowm = ctk.CTkComboBox(input_frame,values=['realistic','cartoon','3d illustration'])
style_dropdowm.grid(row = 1 ,column = 1 , padx = 10,pady = 10)

number_lable= ctk.CTkLabel(input_frame,text = 'images')
number_lable.grid(row = 2,column = 0,padx =10,pady =10)

number_slider = ctk.CTkSlider(input_frame,from_=1,to=10,number_of_steps=9)
number_slider.grid(row = 2,column = 1,padx = 10 , pady =10)

grnerate_button = ctk.CTkButton(input_frame,text='Generate',command=generate)
grnerate_button.grid(row=3,column =0,columnspan = 2,sticky = 'news',padx= 10,pady = 10)


canves = tkinter.Canvas(root,width=512,height=512)
canves.pack(side ='right',expand = True,padx = 20 , pady = 20)


# app loop --------------

root.mainloop()