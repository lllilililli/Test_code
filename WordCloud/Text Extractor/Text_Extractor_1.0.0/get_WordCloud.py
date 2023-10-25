from wordcloud import WordCloud
import matplotlib.pyplot as plt

def text_visualization(text, STOPWORD_KOREAN, FONT_PATH):
    with open(STOPWORD_KOREAN, "rt", encoding="utf-8") as f:
            stop_words = [line.strip() for line in f.readlines()]
            
    wordcloud = WordCloud(font_path=FONT_PATH, background_color='white', colormap='winter', stopwords=stop_words).generate(text)
    
    plt.figure("Result", figsize=(10, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
