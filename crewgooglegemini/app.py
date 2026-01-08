import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
import streamlit as st
import os
from crew import run_crew
import logging
logging.getLogger("root").setLevel(logging.WARNING)


# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="AI News Crew",
    page_icon="🧠",
    layout="centered",
)

st.title("AI News Generator")
st.caption("CrewAI + Gemini-powered research & writing agents")

# -----------------------------
# User Input
# -----------------------------
topic = st.text_input(
    "Enter a topic",
    value="AI in Healthcare",
    help="Example: AI in Finance, LLMs in Education, Robotics in Medicine",
)

# -----------------------------
# Run Crew
# -----------------------------
if st.button("🚀 Generate Article"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("🤖 Agents are researching, debating, and writing..."):
            try:
                # Run CrewAI
                result = run_crew(topic)

                st.success("✅ Article generated successfully!")

                # -----------------------------
                # Final Output
                # -----------------------------
                st.markdown("## 📰 Final Output")
                st.markdown(result)

                # -----------------------------
                # Agent Logs / Reasoning
                # -----------------------------
                with st.expander("🔍 Agent Logs (Verbose Output)"):
                    st.text(result)

                # -----------------------------
                # Download Markdown File
                # -----------------------------
                if os.path.exists("new-blog-post.md"):
                    with open("new-blog-post.md", "r", encoding="utf-8") as f:
                        st.download_button(
                            label="💾 Download Article (Markdown)",
                            data=f.read(),
                            file_name="ai_news.md",
                            mime="text/markdown",
                        )
                else:
                    st.info("Markdown file not found. Writer may not have produced a file.")

            except Exception as e:
                st.error("Something went wrong while running the agents.")
                st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with CrewAI, Gemini, Serper & Streamlit")
