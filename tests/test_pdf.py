from pypdf import PdfReader
import os.path

from conftest import resources_path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf():
    reader = PdfReader(os.path.join(resources_path, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert 'consultant' in text
    assert number_of_pages == 412
