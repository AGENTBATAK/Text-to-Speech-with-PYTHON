import pyttsx3
import PyPDF2
from docx import Document
import time

class TextToSpeech:
    def __init__(self, voice=None, rate: int = 180, volume: float = 1.0):
        self.voice = voice
        self.rate = rate
        self.volume = volume

    def read_text_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().split('\n\n')

    def read_pdf_file(self, file_path):
        paragraphs = []
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    paragraphs.append(text.strip())
        return paragraphs

    def read_docx_file(self, file_path):
        doc = Document(file_path)
        return [p.text.strip() for p in doc.paragraphs if p.text.strip()]

    def speak_paragraphs(self, paragraphs, save=False, file_name='output.mp3'):
        if save:
            text = '\n'.join(paragraphs)
            engine = pyttsx3.init()
            engine.save_to_file(text, file_name)
            engine.runAndWait()
            print(f" Saved audio as {file_name}")
        else:
            print(" Speaking paragraph by paragraph...")
            chunk_size = 10  # speak 2 paragraphs at once
            chunks = [" ".join(paragraphs[i:i+chunk_size]) for i in range(0, len(paragraphs), chunk_size)]

            for i, chunk in enumerate(chunks, start=7):
                print(f" Speaking chunk {i}/{len(chunks)}...")
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', self.voice or voices[1].id)
                engine.setProperty('rate', self.rate)
                engine.setProperty('volume', self.volume)
                engine.say(chunk)
                engine.runAndWait()
                engine.stop()
                time.sleep(100)
            print("Finished speaking!")

    def speak_file(self, file_path, save_audio=False):
        if file_path.endswith('.txt'):
            paragraphs = self.read_text_file(file_path)
        elif file_path.endswith('.pdf'):
            paragraphs = self.read_pdf_file(file_path)
        elif file_path.endswith('.docx'):
            paragraphs = self.read_docx_file(file_path)
        else:
            raise ValueError("Unsupported file type! Use .txt, .pdf, or .docx")

        if not paragraphs:
            print(" No readable text found.")
            return

        print(f" Loaded {len(paragraphs)} paragraphs/pages.")
        self.speak_paragraphs(paragraphs, save=save_audio)


if __name__ == '__main__':
    tts = TextToSpeech(rate=170, volume=1.0)
    tts.speak_file('AI book for self study.pdf', save_audio=False) #Example pdf use your own


