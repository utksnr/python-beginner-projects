from gtts import gTTS
import PyPDF2

def pythonText():
    pyText = input("Print your Text please.")
    savename = input("Please enter save name.")


    language = "tr"
    gtts_transformer =gTTS(text=pyText, lang = language)
    gtts_transformer.save(savename+".mp3")

def pdfText():
    pdfpath = input("Please enter pdf path.")
    savename = input("Please enter save name.")

    pdf_file = open(f"{pdfpath}","rb")
    pdf_Reader = PyPDF2.PdfFileReader(pdf_file)
    total_page = pdf_Reader.numPages
    textlist = []

    for i in range(total_page):
        page = pdf_Reader.getPage(i)
        textlist.append(page.extract_text())

    string = " ".join(textlist)

    language = "tr"
    gtts_transformer =gTTS(text=string, lang = language)
    gtts_transformer.save(savename+".mp3")


def TexttoAudio():
    print("Welcome to Text to Audio. This is one of my beginner projects.")
    print("Enter Python to convert text from python.")
    print("Enter Pdf to convert text from local Pdf File.")
    decision = input("Decision  Python or Pdf ==>: ")

    if decision == "Python":
        pythonText()
    elif decision == "Pdf":
        pdfText()

TexttoAudio()