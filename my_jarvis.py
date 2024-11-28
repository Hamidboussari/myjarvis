import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
# import itertools


ctk.set_appearance_mode("dark") #Initialisation du mode d'affichage de la fenetre
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("My JARVIS")
app.geometry("800x600")

video_path = "medias/background JARVIS.mp4"
cap = cv2.VideoCapture(video_path)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
        
        background_label.configure(image=frame_image)
        background_label.image = frame_image  
        
    
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    app.after(30, update_frame)

background_label = ctk.CTkLabel(app, text="Test", font=("Helvitica", 16))
background_label.pack(pady=100)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

update_frame()

app.mainloop()

