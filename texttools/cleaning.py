import string

def clean_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    return " ".join(text.split())\n