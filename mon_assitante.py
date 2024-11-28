import customtkinter as ctk
# import cv2
# from PIL import Image, ImageTk
# import itertools


ctk.set_appearance_mode("system") #Initialisation du mode d'affichage de la fenetre
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Mon mini_JARVIS")
app.geometry("500x400")

# # Charger le GIF animé et préparer les frames
# video_path = "python_programming/assistante_virtuel/background JARVIS.mp4"
# cap = cv2.VideoCapture(video_path)

# # Fonction pour lire et afficher chaque frame de la vidéo
# def update_frame():
#     ret, frame = cap.read()
#     if ret:
#         # Convertir l'image en format compatible avec Tkinter
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
        
#         # Afficher l'image sur le label de fond
#         background_label.configure(image=frame_image)
#         background_label.image = frame_image  # Pour éviter la suppression par le garbage collector
        
#     # Recommencer la lecture si on atteint la fin de la vidéo
#     else:
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
#     app.after(30, update_frame)  # Ajuster la fréquence d'actualisation

# # Label pour afficher le fond animé
# background_label = ctk.CTkLabel(app)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# update_frame()

app.mainloop()
