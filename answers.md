## Homework-05

### Question 1

Install uv<br>
What's the version of uv you installed?<br>
Use --version to find out<br>

#### Answer : uv 0.9.5 (d5f39331a 2025-10-21)

### Question 2

Use uv to install Scikit-Learn version 1.6.1<br>
What's the first hash for Scikit-Learn you get in the lock file?<br>
Include the entire string starting with sha256:, don't include quotes<br>

#### Answer : hash = "sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e"

### Question 3

Write a script for loading the pipeline with pickle<br>
Score this record:<br>

{
    "lead_source": "paid_ads",<br>
    "number_of_courses_viewed": 2,<br>
    "annual_income": 79276.0<br>
}

#### Answer : 0.533

### Question 4

Install FastAPI<br>
Write FastAPI code for serving the model<br>
Now score this client using requests:<br>

url = "YOUR_URL"<br>
client = {<br>
    "lead_source": "organic_search",<br>
    "number_of_courses_viewed": 4,<br>
    "annual_income": 80304.0<br>
}

requests.post(url, json=client).json()

#### Answer : 0.534

### Question 5

Download the base image agrigorev/zoomcamp-model:2025. You can easily make it by using docker pull command.

So what's the size of this base image?

#### Answer : 45

### Question 6

Let's run your docker container!

After running it, score this client once again:

url = "YOUR_URL"<br>
client = {<br>
    "lead_source": "organic_search",<br>
    "number_of_courses_viewed": 4,<br>
    "annual_income": 80304.0<br>
}

requests.post(url, json=client).json()

What's the probability that this lead will convert?

#### Answer : 0.59