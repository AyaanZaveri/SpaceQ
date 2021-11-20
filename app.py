from flask import Flask, render_template, session
from flask import request
import openai
import json
import requests 
import os
app = Flask(__name__)
app.secret_key = "abc"

qLog = []
aLog = []

if __name__ == "__main__":
    app.run()

@app.route('/', methods=['GET','POST'])

def process():
  name = request.form.get('name','')
  session['name'] = name.title()
  name = name.title()
  print(name)

  #To set API_KEY, type "export OPENAI_API_KEY=YOUR_KEY" in terminal
  openai.api_key = os.getenv("OPENAI_API_KEY")
  completion = openai.Completion()

  with open("CLI/samples.txt") as file:
    default_log = "\n".join(file.readlines())

    prompt = f'{default_log}Human: {name}\nAI:'

    response = completion.create(
    prompt=prompt, engine="davinci-codex", stop=['\nHuman'], temperature=0.9,
    top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
    max_tokens=150)

    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=prompt,
      temperature=0,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )

    #print(response)

    res = json.loads(response.last_response.body)
    answer = res['choices'][0]['text']

    print(answer)

    qLog.append(name)
    aLog.append(answer)

    qLogStr = str(qLog)
    aLogStr = str(aLog)

    print(qLogStr)
    print(aLogStr)

    if answer == "'''":
      answer = "Answer:"

    print(answer)

  return render_template('index.html', answer=answer, name=name, qLogStr=qLogStr, aLogStr=aLogStr)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True, port=5000)