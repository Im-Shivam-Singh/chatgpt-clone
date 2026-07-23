from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

def read_files():
    from app.document.factory import DocumentFactory
    files = ["sample/test.pdf"]
    for file in files:
        full = f'{PROJECT_ROOT}/app/document/tests/{file}'
        reader_cls = DocumentFactory.get_reader(full)
        print(reader_cls.read(full))

if __name__ == "__main__":
    read_files()