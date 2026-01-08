# AI News Generator with CrewAI, Gemini, and Streamlit

This project is an AI-powered news article generator built using **CrewAI**, **Google Gemini**, **Serper**, and **Streamlit**. It demonstrates how multiple autonomous agents can collaborate to research a topic and produce a well-structured, readable article end-to-end.

The application exposes a simple web interface where users enter a topic, trigger the agents, and receive a generated article along with optional verbose agent logs.

---

## Features

* Multi-agent workflow using CrewAI
* Research agent powered by web search (Serper)
* Writing agent that converts research into a polished article
* Google Gemini LLM integration
* Streamlit-based interactive UI
* Optional verbose agent reasoning for transparency
* Markdown export of generated articles

---

## Architecture Overview

The system is composed of four main layers:

1. **UI Layer (Streamlit)**

   * Collects user input
   * Triggers the agent workflow
   * Displays the final article and logs

2. **Crew Layer**

   * Defines the agents, tasks, and execution flow
   * Runs agents sequentially using CrewAI

3. **Agent Layer**

   * `Senior Researcher`: Gathers insights using Serper search
   * `Writer`: Synthesizes research into a readable article

4. **LLM & Tools**

   * Google Gemini (`gemini-2.5-flash`)
   * Serper Dev Tool for real-time web search

---

## Project Structure

```
.
├── app.py          # Streamlit application
├── crew.py         # Crew configuration and execution
├── agents.py       # Agent definitions
├── tasks.py        # Research and writing tasks
├── tools.py        # External tools (Serper)
├── .env            # Environment variables (not committed)
└── README.md
```

---

## Requirements

* Python 3.9+
* Google Gemini API key
* Serper API key

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/ai-news-generator.git
   cd ai-news-generator
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

---

## Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

Make sure the `.env` file is not committed to version control.

---

## Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## Usage

1. Enter a topic (e.g., *AI in Healthcare*, *LLMs in Education*)
2. Click **Generate Article**
3. Wait while the agents research and write
4. View the final article
5. Optionally inspect agent logs or download the article as Markdown

---

## Screenshots

Add screenshots of the UI here to showcase the application.

Suggested sections:

* Home screen
* Article generation in progress
* Final generated article
* Agent logs view

Example:

```
![Home Screen](screenshots/home.png)
![Generated Article](screenshots/article.png)
```

---

## Notes on Model Configuration

This project uses the Gemini API via CrewAI’s LLM abstraction.
The model configuration that is known to work reliably:

```python
LLM(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.5,
)
```

Using unsupported or preview-only model identifiers may result in API errors.

---

## Future Improvements

* Parallel agent execution
* Source citation in generated articles
* Multiple writing styles or tones
* Persistent article history
* Deployment on Streamlit Cloud or Docker


* Add an architecture diagram section
* Rewrite it for open-source discoverability (badges, keywords, etc.)
