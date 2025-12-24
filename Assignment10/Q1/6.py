raw_text = """
Artificial Intelligence is the simulation of human intelligence in machines.
It enables computers to learn from data and make decisions.
Machine learning is a subset of artificial intelligence.
Deep learning is a specialized form of machine learning.

AI is widely used in healthcare for disease prediction and diagnosis.
It is also used in finance for fraud detection.
Education systems use AI for personalized learning experiences.
"""

print("6. Sentence-Based Chunking (NLP-Style)")
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
text_splitter = SentenceTransformersTokenTextSplitter(chunk_size=256,chunk_overlap=20)
docs = text_splitter.create_documents([raw_text])
doc = docs[0]
print("docs content:\n",doc.page_content)