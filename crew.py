import gradio as gr
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

# Forming the tech-focused crew with some enhanced configuration
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Function to execute the crew process
def generate_article(topic):
    result = crew.kickoff(inputs={'topic': topic})
    print(result)
    return result

# Creating the Gradio interface
examples = [["AI in healthcare"], ["Quantum Computing advances"], ["The future of blockchain technology"]]

iface = gr.Interface(
    fn=generate_article,
    inputs=gr.Textbox(lines=1, placeholder="Enter a technology topic..."),
    outputs="text",
    title="Tech News Generator",
    description="Generate a news article on any tech topic using CrewAI.",
    examples=examples,
)


iface.launch(share=True, inbrowser=True)
