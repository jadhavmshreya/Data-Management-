'''import requests

def generate_sql(user_query):

    prompt = f"""
You are an SQL expert.

Database schema:
movies(id, name, year, rating, genre)

Convert this into SQL query:
{user_query}

Return ONLY SQL.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    return result.strip() '''

import requests

def generate_sql(user_query):

    prompt = f"""
You are an SQL expert.

Database schema:
movies(id, name, year, rating, genre)

Convert natural language into SQL.

Rules:
- Return ONLY SQL
- No explanation
- No markdown
- SQL must start with SELECT

User query:
{user_query}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    # Extract SQL safely
    sql_start = result.find("SELECT")

    if sql_start != -1:
        result = result[sql_start:]

    return result.strip()