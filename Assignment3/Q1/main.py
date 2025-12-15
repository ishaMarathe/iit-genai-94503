import pandas as pd
import pandasql as ps

data = pd.read_csv("books_hdr.csv")

query = "SELECT subject,sum(price) as total_price FROM books GROUP BY subject"

result = ps.sqldf(query,{"books":data})

print(result)

