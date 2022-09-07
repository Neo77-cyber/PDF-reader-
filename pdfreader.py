import PyPDF2, pikepdf, pyttsx3
pdf = pikepdf.open("Analysis_of_Colonialism_and_Its_Impact_in_Africa_Ocheni_and_Nwankwo_CSCanada_2012.pdf")
pdf.save("decrypted pdf file.pdf")

pdf_reader = PyPDF2.PdfFileReader("decrypted pdf file.pdf")

speaker = pyttsx3.init()

for num in range(2,4):
    page = pdf_reader.getPage(num)
    text = page.extract_text(num)
    speaker.say(text)
    speaker.runAndWait

speaker.save_to_file(text, "audiobook.mp3")
speaker.runAndWait()
