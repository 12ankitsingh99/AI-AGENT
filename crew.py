import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

# Define a function to run the crew process
def run_crew_process(topic):
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )
    result = crew.kickoff(inputs={'topic': topic})
    return result

# Streamlit code for input and output
st.title("AI in Healthcare News Research and Writing")

# Input: Get the topic from the user
topic = st.text_input("Enter the topic:", "AI in healthcare")

# Button to start the task execution process
if st.button("Run Crew Process"):
    with st.spinner('Processing...'):
        result = run_crew_process(topic)
        st.success("Process completed!")

    # Output: Display the result
    st.write(result)
