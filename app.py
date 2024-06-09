import streamlit as st

# Basic Information
name = "John Doe"
title = "Software Developer"
about = """
A passionate software developer with 5+ years of experience in developing scalable web applications. 
Proficient in Python, JavaScript, and various frameworks.
"""
contact_email = "john.doe@example.com"

# Experience
experience = [
    {
        'position': 'Senior Developer',
        'company': 'Tech Solutions Inc.',
        'years': '2020-Present',
        'description': 'Leading a team of developers to create cutting-edge web applications.'
    },
    {
        'position': 'Junior Developer',
        'company': 'WebWorks',
        'years': '2017-2020',
        'description': 'Developed various web applications and provided maintenance and support.'
    }
]

# Skills
skills = ['Python', 'JavaScript', 'Flask', 'Django', 'HTML', 'CSS']

# Streamlit App
st.title(name)
st.subheader(title)

st.write(about)

st.header("Experience")
for job in experience:
    st.subheader(f"{job['position']} at {job['company']}")
    st.write(f"{job['years']}")
    st.write(job['description'])

st.header("Skills")
st.write(", ".join(skills))

st.header("Contact")
st.write(f"Email: {contact_email}")
