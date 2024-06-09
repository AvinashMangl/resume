from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John Doe"
    title = "Software Developer"
    about = "A passionate software developer with 5+ years of experience in developing scalable web applications."
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
    skills = ['Python', 'JavaScript', 'Flask', 'Django', 'HTML', 'CSS']

    return render_template('index.html', name=name, title=title, about=about, experience=experience, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
