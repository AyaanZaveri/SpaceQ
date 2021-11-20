from flask import Flask, render_template, session
from flask import request
import openai
import json
import requests 
import os
app = Flask(__name__)
app.secret_key = "abc"

#if __name__ == "__main__":
#    app.run()

@app.route('/', methods=['GET','POST'])

def process():
  name = request.form.get('name','')
  session['name'] = name.title()
  name = name.title()
  print(name)

  openai.api_key = "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"
  response = openai.Completion.create(
  engine="davinci-codex",
  prompt="Question: How big is the sun?\nAnswer: The sun is about 1.39 million kilometers (864,000 miles) in diameter. (The diameter we see is from Earth's perspective, but the sun is much bigger from the sun's perspective.)\n\nQuestion: How hot is the sun?\nAnswer: The temperature inside the sun is about 15 million degrees Celsius. (It is much hotter than that, but we cannot see the temperature from here because of the size of the sun.)\n\nQuestion: How many planets are there?\nAnswer: There are eight planets in our solar system.\n\nQuestion: Can we see the other planets?\nAnswer: Yes, we can see them with a telescope.\n\nQuestion: How far away is the sun?\nAnswer: The sun is 93 million miles away from Earth. (It is much farther away than that, but we cannot see the distance from here.)\n\nQuestion: What is the sun made of?\nAnswer: The sun is made mostly of hydrogen and a little bit of helium.\n\nQuestion: Why is the sky blue?\nAnswer: Blue is the color of the sky because of Earth's atmosphere.\n\nQuestion: Why are the sunrises and sunsets red?\nAnswer: When the sun goes down, it leaves behind red, orange, yellow, and purple color.\n\nQuestion: Why do we need the sun?\nAnswer: We need the sun for warmth and light.\n\nQuestion: How long does it take for the sun to circle Earth?\nAnswer: It takes the sun about a month to circle the Earth.\n\nQuestion: How far away is the moon?\nAnswer: The moon is about 230,000 miles away from Earth.\n\nQuestion: What is the moon made of?\nAnswer: The moon is made mostly of rock and dust.\n\nQuestion: How big is the moon?\nAnswer: The moon is about 2,000 miles across.\n\nQuestion: How many moons does Earth have?\nAnswer: Earth has one moon.\n\nQuestion: Why is the sky blue during the day?\nAnswer: The sky is blue during the day because of particles in the air.\n\nQuestion: " + name + "\n",
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)


  #print(response)

  res = json.loads(response.last_response.body)
  print(res)
  answer = res['choices'][0]['text']
  print(answer)

  if answer == "'''":
    answer = "Answer:"

  print(answer)

  return render_template('index.html', answer=answer, name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True, port=8181)