import streamlit as st

st.set_page_config(page_title="Bruce-Arhin Shadrach | GenAI Engineer", layout="centered")

st.title("👨🏽‍💻 Bruce-Arhin Shadrach")
st.subheader("Generative AI Engineer | LLM Developer | RAG Specialist")
st.write("📍 Edmonton, AB | 📧 brucearhin098@gmail.com | ☎️ +1 (647) 834-7396")

st.markdown("---")

st.markdown("### 🧠 About Me")
st.write("""
Generative AI Engineer with 5+ years of experience building LLM-based systems, multi-agent frameworks, and RAG pipelines using tools like LangChain, Vertex AI, and Azure OpenAI. I’ve built custom LLM agents, deployed enterprise-ready chatbots, and fine-tuned GPT models for specialized business use cases.
""")

st.markdown("### 💼 Projects")
st.markdown("- 🔁 **RAG AI Assistant** (LangChain, Azure): Deployed RAG pipeline with vector search (98% retrieval accuracy)")
st.markdown("- 🤖 **LLM Agent Framework**: Custom agent orchestration inspired by LangGraph with OpenAI function calling")
st.markdown("- 🧪 **Prompt Evaluation Pipeline**: Built CI/CD-compatible testing for prompt templates and LLM flows")

st.markdown("### 🔗 GitHub Projects")
st.write("[🔗 View My Repositories](https://github.com/your-github-name)")

st.markdown("### 📥 Download Resume")
with open("Bruce_Resume.pdf", "rb") as file:
    btn = st.download_button(label="📄 Download My Resume", data=file, file_name="Bruce_Resume.pdf", mime="application/pdf")

st.markdown("### 📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/your-email@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
