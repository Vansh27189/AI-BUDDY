from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_huggingface import HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser
from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

# class Output(BaseModel):
#     points: list[str]


gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    temperature=0.5,
    model_kwargs={"response_mime_type": "text/plain"}
)

gemini_template = PromptTemplate(
    template='''Write a detailed, well-structured report on the topic: "{topic}".
Requirements:
- Start with a concise executive summary (5–6 lines)
- Use clear section headings
- Explain key concepts in simple but precise language
- Include real-world examples where relevant
- Discuss advantages, limitations, and future outlook
- Keep the tone professional and informative
- Avoid bullet points unless absolutely necessary
- Length: 300-400 words

IMPORTANT: Return the report as plain conversational text. Do not use JSON formatting.
''',
input_variables=['topic']
)

report_chain = gemini_template | gemini_llm

#Hugging face

hf_pipeline = pipeline(
    task="summarization",
    model="google/flan-t5-base",  # good for summarization
    max_new_tokens=200
)

hf_llm = HuggingFacePipeline(pipeline=hf_pipeline)

points_prompt = PromptTemplate(
    template='''
Summarize the report below into exactly 5 key points.

Format exactly like this:
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5
IMPORTANT: Return the report as plain conversational text. Do not use JSON formatting.
REPORT:
{report}
''',
input_variables=['report']

)
points_chain = points_prompt | hf_llm | StrOutputParser()

def generate_report_and_points(topic: str):
   
    report_result = report_chain.invoke({"topic": topic})
    report_text = report_result.content # extract text

    final_points= points_chain.invoke({"report": report_text})
    return report_text, final_points
   

def main():
    topic = input("enter the topics name")
    report, points = generate_report_and_points(topic)
    print("\n===== REPORT =====\n")
    print(report)

    print("\n===== 5 KEY POINTS =====\n")
    print(points)

if __name__ == "__main__":
    main()


