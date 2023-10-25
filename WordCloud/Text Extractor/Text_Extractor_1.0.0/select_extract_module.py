from tkinter import Tk, filedialog

def select_file(type):
    root = Tk()
    root.withdraw()
    if type == 0:
        file_path = filedialog.askopenfilename(filetypes=[("TXT Files", "*.txt"), ("PDF Files", "*.pdf")])
    else:
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

def extract_text(path):
    if path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()
    elif path.endswith('.pdf'):
        import PyPDF2
        with open(path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
    else:
        raise ValueError("Unsupported file format. Only .txt and .pdf files are supported.")
    return text

def get_save_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT Files", "*.txt")])
    return file_path
