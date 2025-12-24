text =[
    """
       A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs, which enable computers to perform a wide range of tasks. 
    """ 
]

print("3. Token-Based Chunking")
from langchain_text_splitters import TokenTextSplitter
text_splitter = TokenTextSplitter(chunk_size=200,chunk_overlap=20)
docs = text_splitter.create_documents(text)
doc = docs[0]
print("docs content:",doc.page_content)