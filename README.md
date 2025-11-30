# Smart-Resume-Analyzer-Job-Recommendation-System
The Smart Resume Analyzer &amp; Job Recommendation System is an interactive application that allows users to upload their resumes and receive personalized career insights.
The system extracts key information such as skills, education, and experience from the resume and evaluates how well the candidate matches various job roles. Users can also select a desired job title, and the system provides recommendations on missing skills and predicts future confidence levels if those skills are acquired.

This project combines resume parsing, skill extraction, job matching, and career recommendation into a single, user-friendly dashboard. It is ideal for job seekers looking to improve their employability or transition to a new role.

# Key Features

Resume Upload & Parsing

Supports PDF and DOCX resumes

Extracts skills, education, and experience

## Job Matching & Confidence Score

Compares extracted skills with predefined job profiles

Provides confidence percentages for current skills per job role

## Desired Job Recommendation

Allows user to select a target job

Identifies missing skills required for that role

Predicts confidence score after acquiring recommended skills

## Interactive Dashboard (Streamlit)

Highlights key points from the resume

Shows match scores and missing skills

Visualizes skills comparison with progress bars or radar charts

## Optional Backend & API

Store resumes and analysis results in SQL

Flask API endpoint for external integration

# Technologies Used

Python: Resume processing, skill extraction, job matching

Pandas / NumPy: Data manipulation and calculations

Regex / TF-IDF (sklearn): Extracting and ranking skills

Streamlit: Interactive dashboard for user input and visualization

SQLAlchemy: Optional resume storage in database

Flask: Optional API for external access

Joblib: Save reusable models or skill extraction mappings

# Workflow

User uploads resume → system extracts skills, education, experience

Extracted skills are compared against predefined job profiles

System calculates confidence % for each job role

User selects desired role → system highlights missing skills

Predicted confidence % for desired role is displayed after acquiring missing skills

Dashboard shows resume highlights, current vs target skills, and visualizations

# Expected Outcome

Resume Highlights: Skills, Education, Experience

Job Matches: List of jobs with confidence scores

Desired Job Recommendations: Missing skills and predicted confidence

Visualizations: Progress bars, radar charts, skill comparison

# Use Case

Job seekers wanting a clear understanding of their skill fit for different roles

Candidates planning to upskill for desired positions

Recruiters looking for a fast way to screen resumes and assess skill gaps
