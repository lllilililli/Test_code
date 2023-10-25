from select_extract_module import select_file, extract_text, get_save_file_path

if __name__ == "__main__":
    pdf_path = select_file(1)

    if pdf_path:
        text = extract_text(pdf_path)
        save_path = get_save_file_path()

        if save_path:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(text)
