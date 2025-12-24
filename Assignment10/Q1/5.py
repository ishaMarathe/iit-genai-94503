code_text = """
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def main():
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.subtract(10, 5))


if __name__ == "__main__":
    main()
"""


print("5. Code-Aware Chunking")
from langchain_text_splitters import RecursiveCharacterTextSplitter
code_splitter = RecursiveCharacterTextSplitter.from_language(language="python",chunk_size=200,chunk_overlap=50)
docs = code_splitter.create_documents([code_text])
doc = docs[0]
print("docs content:\n",doc.page_content)