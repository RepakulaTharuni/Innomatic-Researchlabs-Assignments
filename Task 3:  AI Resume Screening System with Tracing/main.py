
# IMPORTS
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
# 
# LANGSMITH TRACING (MANDATORY)
import os
from getpass import getpass

os.environ["LANGCHAIN_API_KEY"] = getpass("Enter LangSmith API Key: ")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI Resume Screening"

# MODEL (OPTIONAL - NOT CRITICAL)
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=pipe)

# HELPER FUNCTIONS 
def extract_skills(text):
    return [skill.strip().lower() for skill in text.replace("\n", ",").split(",") if skill.strip()]


def match_skills(resume_skills, jd_skills):
    matching = [s for s in resume_skills if s in jd_skills]
    missing = [s for s in jd_skills if s not in resume_skills]
    return matching, missing


def calculate_score(matching, total):
    if total == 0:
        return 0
    return int((len(matching) / total) * 100)


# FINAL EXPLANATION FUNCTION
def generate_explanation(score, matching, missing):

    if score == 100:
        return f"The candidate is an excellent fit with all required skills such as {', '.join(matching)}. No important skills are missing, making them highly suitable for the role."

    elif score >= 50:
        return f"The candidate has a moderate fit with skills like {', '.join(matching)}. However, missing skills such as {', '.join(missing)} reduce their overall suitability."

    else:
        return f"The candidate is not a good fit as they lack key required skills. Missing critical skills like {', '.join(missing)} results in a low score."


# PIPELINE FUNCTION
def run_pipeline(resume, jd):

    print("\n==============================")
    print("🚀 AI RESUME SCREENING")
    print("==============================")

    # STEP 1: EXTRACT
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    print("\nSTEP 1 - EXTRACT:")
    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)

    # STEP 2: MATCH
    matching, missing = match_skills(resume_skills, jd_skills)

    print("\nSTEP 2 - MATCH:")
    print("Matching Skills:", matching)
    print("Missing Skills:", missing)

    # STEP 3: SCORE
    score = calculate_score(matching, len(jd_skills))

    print("\nSTEP 3 - SCORE:")
    print(score)

    # STEP 4: EXPLANATION
    explanation = generate_explanation(score, matching, missing)

    print("\nSTEP 4 - EXPLANATION:")
    print(explanation)


# JOB DESCRIPTION
jd = """
python, machine learning, deep learning, nlp, sql,
pandas, numpy, tensorflow
"""


# RESUMES
strong_resume = """
python, machine learning, deep learning, nlp, sql,
pandas, numpy, tensorflow
"""

average_resume = """
python, machine learning, sql, pandas
"""

weak_resume = """
excel, communication
"""


# RUN PIPELINE
print("🔥 STRONG CANDIDATE")
run_pipeline(strong_resume, jd)

print("\n⚖️ AVERAGE CANDIDATE")
run_pipeline(average_resume, jd)

print("\n❌ WEAK CANDIDATE")
run_pipeline(weak_resume, jd)
