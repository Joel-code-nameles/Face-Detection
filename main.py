import customtkinter
from PIL import Image
import logic

window = customtkinter.CTk()
window.geometry("700x650")
window.title("Face Detection")

frame = customtkinter.CTkFrame(window,width=700,height=650,bg_color="#B3C3C9",border_color="#FF063F",border_width=1)
frame.place(relx = 0,rely = 0)

capture = customtkinter.CTkButton(frame,width= 50,height=40,corner_radius= 30,fg_color="#063fff",border_color="black",border_width=2,text="Capture",hover_color="#0971A8")
capture.place(relx = 0.4,rely = 0.45)
capture.configure(command= logic.Camera)

imageLabel1 = customtkinter.CTkLabel(window, text="")
imageLabel1.place(relx=0.30, rely=0.1)

img_url1 = r"images/recording-icon-outline-set-sign_1223784-39609.webp"
image_copy1 = Image.open(img_url1)
fix_image1 = customtkinter.CTkImage(image_copy1, size=(250, 200))
imageLabel1.configure(image=fix_image1)


window.mainloop()