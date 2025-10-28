CAUTION
The audio save option (save_audio=True) is currently not working. The program can read text out loud but will not save it as an audio file.

TEXT TO AUDIO READER
Hi my name is "Swastik Katyayan" i am in 3rd Sem currently pursuing my b.tech degree , as a projectr i created this with help of all the resources
and python libraries , there are a lot of thing that need to be changed so stay tune and enjoy.

ABOUT THE PROJECT
This Python project reads text from files like PDF, TXT, or DOCX and converts them into speech. It works like a personal audiobook reader. You can listen to your study materials or books being read out loud by your computer.

😕HOW IT WORKS
1. The program uses a class called TextToSpeech.
2. It takes your file (PDF, TXT, or DOCX) and reads the content.
3. It then breaks the text into small chunks and uses the pyttsx3 library to speak each part.
4. You can control how fast the voice speaks (rate) and how loud it is (volume).
5. The save option is present but currently not functional.

🕶️REQUIRED LIBRARIES
Make sure you install these Python libraries before running the program:
1.pip install pyttsx3.
2.pip install PyPDF2.
3.pip install python-docx.

😡SETTING UP YOUR FILE
1. Place your file (PDF, TXT, or DOCX) in the same folder as this Python code.
   Example:
   D:\text to audio reader\
   ├── text_to_audio.py
   ├── AI book for self study.pdf

2. In the last line of the code, you will see:
   tts.speak_file('AI book for self study.pdf', save_audio=False)

   Replace 'AI book for self study.pdf' with the name of your file, including the extension.
   Example:
   tts.speak_file('MyNotes.pdf', save_audio=False)

😅HOW TO RUN
1. Open your terminal or command prompt in the folder containing the code.
2. Run the following command:
   python text_to_audio.py

The program will begin reading your file paragraph by paragraph.

NOTE
The save_audio feature (to save the output as an mp3 file) is not functional at the moment. It only reads the text aloud in real-time.

CREDITS:-Coz why not :3
Created by: Swastik Katyayan
3rd Semester Student
