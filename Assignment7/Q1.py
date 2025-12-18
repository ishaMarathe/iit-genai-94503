import streamlit as st
from langchain.chat_models import init_chat_model
import os
import pandas as pd
from pandasql import sqldf
from dotenv import load_dotenv

load_dotenv()

st.title("SQL Assistant")

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation=[{"role":"system","content":"You are SQLite expert developer with 10 years of experience."}]

uploaded_file=st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)

    st.subheader("Schema")
    st.write(df.dtypes)

    user_input=st.text_input("Ask anything about this CSV")

    if user_input:
        llm_input=f"""
        Table Name:data
        Table Schema:{df.dtypes}
        Question:{user_input}
        Instruction:
            Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'.
        """

        result=llm.invoke(llm_input)
        query=result.content

        st.subheader("SQL Query")
        st.code(query, language="sql")

        try:
            output=sqldf(query, {"data":df})
        except Exception as e:
            st.error(f"Query execution failed: {e}")
            output=None

        if output is not None:
            if output.empty:
                st.warning("Query executed but no results.")
                explanation="The query executed successfully but returned no data."
            else:
                output_preview=output.head(10).to_string(index=False)
                llm_explain_input=f"""
                SQL Query Result:
                {output_preview}

                Instruction:
                Explain in simple English what this query result shows.
                Only explain the data returned by the query, do not repeat the query or question.
                """

                explanation_result=llm.invoke(llm_explain_input)
                explanation=explanation_result.content

            st.subheader("Explanation")
            st.write(explanation)

            if not output.empty:
                st.subheader("Query Result")
                st.dataframe(output)
