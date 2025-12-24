markdown_text = """
# Introduction
This is the introduction section.
It explains what the document is about.

## Background
This section provides background information.
It gives context to the topic.

### History
This subsection talks about the history.
Details about past events are included here.

## Objectives
The objectives of this document are:
- Explain markdown splitting
- Show header-based chunking

# Conclusion
This is the conclusion section.
It summarizes the document.
"""

print("4. Markdown-Aware Chunking")
from langchain_text_splitters import MarkdownHeaderTextSplitter
headers_to_split_on = [ ("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3") ]
text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
docs = text_splitter.split_text(markdown_text)
doc = docs[0]
print("docs content:",doc.page_content)