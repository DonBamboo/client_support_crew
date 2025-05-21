#!/usr/bin/env python
import sys
import warnings
import re

from datetime import datetime

from client_support_crew.crew import ClientSupportCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    inputs = {
        "client_name": "Jane Smith",
        "client_email": "janesmith@testing.com",
        "website_url": "http://testingme.com",
        "title": "Slow loading website",
        "content": "The website is loading so slow.",
        "platform": "WordPress"
    }
    
    try:
        ClientSupportCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    inputs = {
        "client_name": "Jane Smith",
        "client_email": "janesmith@testing.com",
        "website_url": "http://testingme.com",
        "title": "Slow loading website",
        "content": "The website is loading so slow.",
    }
    try:
        ClientSupportCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        ClientSupportCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "client_name": "Jane Smith",
        "client_email": "janesmith@testing.com",
        "website_url": "http://testingme.com",
        "title": "Slow loading website",
        "content": "The website is loading so slow.",
    }
    
    try:
        ClientSupportCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def strip_html(html: str) -> str:
    text = re.sub(r'</?[^>]+>', '', html).strip()
    text = re.sub(r'\n{4,}', '\n\n', text)
    return text