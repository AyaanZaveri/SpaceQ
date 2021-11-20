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

  def ask(question, chat_log):
    
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
      prompt=prompt, engine="davinci-codex", stop=['\nHuman'], temperature=0.9,
      top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
      max_tokens=150)

    answer = response.choices[0].text.strip()
    return answer

  if __name__ == '__main__':   
    question = name
    answer = ask(question, default_log)

    qLog.append(question)
    aLog.append(answer)

    qLogStr = str(qLog)
    aLogStr = str(aLog)

    print(qLogStr)
    print(aLogStr)

    if answer == "'''":
      answer = "Answer:"

    print(answer)
    print(question)

  return render_template('index.html', answer=answer, name=name, qLogStr=qLogStr, aLogStr=aLogStr)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True, port=5000)