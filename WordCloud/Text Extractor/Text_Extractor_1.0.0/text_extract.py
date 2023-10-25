from select_extract_module import select_file, extract_text
from get_WordCloud import text_visualization

STOPWORD_KOREAN = "stopword_korean.txt"
FONT_PATH = "NanumGothic.ttf"

if __name__ == "__main__":
    txt_path = select_file(0)

    if txt_path:
        text = extract_text(txt_path)
        text_visualization(text, STOPWORD_KOREAN, FONT_PATH)
