# Data Management Project Mod B
Voice2Query: AI-Powered Speech-to-SQL for Interactive Database Exploration
-------------

# Main Objective
----------------
Developed a system that converts spoken language into executable SQL queries.

Main Goals

Speech Recognition
Natural Language Understanding
SQL Query Generation
Database Query Execution
Interactive Dashboard

Result: Enable users to query databases using voice commands instead of SQL.



# Abstract
----------
Voice2Query is an AI-powered Speech-to-SQL system designed to simplify database interaction through natural voice commands. The system integrates Automatic Speech Recognition (ASR), Natural Language Processing (NLP), Text-to-SQL generation, and data visualization into a unified pipeline. Spoken queries are first transcribed into text using Whisper, then translated into SQL statements using Ollama with Llama 3. The generated SQL queries are executed on a SQLite database, and the results are displayed through an interactive Streamlit dashboard. By eliminating the need for manual SQL writing, the system enables intuitive and accessible database exploration for users with little or no database expertise. The project demonstrates the practical integration of speech recognition, large language models, and relational database technologies in a fully functional end-to-end application.


# Technical Architecture
------------------------

Whisper Base 
Ollama + Llama 3 
SQLite 
Streamlit 
Python 


## Core Components
------------------
VoiceInterface - Central voice interaction UI with real-time state feedback (listening, processing, answering)


## AI & Language Processing
---------------------------
LLM Engine: 
Speech Recognition: 
Voice-to-Text: 

### Data Management
-------------------
SQLite

# Conclusion
------------
Voice2Query provides an end-to-end Speech-to-SQL solution that enables intuitive voice-based interaction with databases. By combining Whisper, Ollama with Llama 3, SQLite, and Streamlit, the system successfully converts spoken language into SQL queries, executes them on a relational database, and visualizes the results through an interactive dashboard. The project demonstrates how AI and data management technologies can be integrated to create a practical and user-friendly database exploration system.
