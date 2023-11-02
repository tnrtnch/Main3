import tkinter
import customtkinter
import feedparser
import webview

CNN_link = "http://rss.cnn.com/rss/cnn_latest.rss"
FOX_link = "https://moxie.foxnews.com/google-publisher/latest.xml"
news_cnn = feedparser.parse(CNN_link)
news_fox = feedparser.parse(FOX_link)

window = customtkinter.CTk()
window.geometry("800x670")
window.title("Latest News")
window.resizable(width=False,height=False)

def open_window(event):
    webview.create_window('Current news', event.widget.cget('text')) 
    webview.start() 

def clear_frame():
   for widgets in bottom_frame.winfo_children():
      widgets.destroy()

def latest_CNN():
    count = 1
    clear_frame()
    button_CNN.configure(fg_color="green")
    button_FOX.configure(fg_color="#00688B")

    for a in news_cnn.entries:
        customtkinter.CTkLabel(master=bottom_frame, text=str(count) + "." + str(a.title), anchor=tkinter.W, font=('Helveticabold', 14))\
            .pack(side="top", fill="x")
        link_a = customtkinter.CTkLabel(master=bottom_frame, text=a.link, anchor=tkinter.W, font=('Helveticabold', 14), text_color="blue",\
             cursor="hand2")
        link_a.pack(side="top", fill="x")
        link_a.bind("<Button-1>", open_window)
        count += 1

def latest_FOX():
    count = 1
    clear_frame() 
    button_FOX.configure(fg_color="green")
    button_CNN.configure(fg_color="#00688B")

    for b in news_fox.entries:
        customtkinter.CTkLabel(master=bottom_frame, text=str(count) + "." + str(b.title), anchor=tkinter.W, font=('Helveticabold', 14))\
            .pack(side="top", fill="x")
        link_b = customtkinter.CTkLabel(master=bottom_frame, text=b.link, anchor=tkinter.W, font=('Helveticabold', 14), text_color="blue",\
             cursor="hand2")
        link_b.pack(side="top", fill="x")
        link_b.bind("<Button-1>", open_window)
        count += 1

top_frame = customtkinter.CTkFrame(master=window,fg_color="light gray",height=70)
top_frame.pack(side="top",fill="both")

bottom_frame = customtkinter.CTkFrame(master=window,fg_color="dark gray")
bottom_frame.pack(side="top",fill="both",expand=True)

frame_1 = customtkinter.CTkFrame(master=top_frame, fg_color="light gray",height=70)
frame_1.pack(side="left",fill="both",expand=True)

frame_2 = customtkinter.CTkFrame(master=top_frame, fg_color="light gray",height=70)
frame_2.pack(side="right",fill="both",expand=True)

button_CNN = customtkinter.CTkButton(master=frame_1, text="CNN - Latest news",font=('Helveticabold', 20), command=latest_CNN)
button_CNN.pack(side="right",padx=20, pady=20)

button_FOX = customtkinter.CTkButton(master=frame_2, text="FOX - Latest news",font=('Helveticabold', 20), command=latest_FOX)
button_FOX.pack(side="left",padx=20, pady=20)


window.mainloop()