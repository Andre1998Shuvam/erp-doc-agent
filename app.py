import streamlit as st
from rag import ask
import os

st.set_page_config(page_title="ERP Doc Agent")
st.title("📄 ERP Doc Agent")
st.write("Upload ERP docs, ask questions, get grounded answers with citations.")

query = st.text_input("Ask about your ERP docs:", placeholder="e.g. What is the payroll cutoff process?")

if st.button("Ask") and query:
    with st.spinner("Searching docs..."):
        answer, chunks = ask(query)
    
    st.subheader("Answer")
    st.write(answer)
    
    st.subheader("Sources Used")
    for c in chunks:
        with st.expander(f"{c['source']} - Page {c['page']}"):
            st.write(c['text'][:800])

st.sidebar.info("Built with FAISS + Ollama")