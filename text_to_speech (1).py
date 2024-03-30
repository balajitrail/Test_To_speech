import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import pygame

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")

        self.label = ttk.Label(root, text="Enter Text:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.text_entry = ttk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_text)
        self.convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.play_button = ttk.Button(root, text="Play", command=self.play_audio, state=tk.DISABLED)
        self.play_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def convert_text(self):
        text = self.text_entry.get()
        if text:
            language = "en"
            speech = gTTS(text=text, lang=language, slow=False, tld="com")
            speech.save("sample.mp3")
            print("Text converted and saved as sample.mp3")
            self.play_button.config(state=tk.NORMAL)

    def play_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sample.mp3")
        pygame.mixer.music.play()
        # Wait until the music is playing
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
