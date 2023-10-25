def install():
    import subprocess
    subprocess.run(["pip", "install", "wordcloud"]) # pip install wordcloud
    subprocess.run(["pip", "install", "matplotlib"]) # pip install matplotlib
    subprocess.run(["pip", "install", "PyPDF2"]) # pip install PyPDF2

install()
