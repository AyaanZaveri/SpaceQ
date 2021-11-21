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

  openai.api_key = os.getenv("OPEN_AI_KEY")

  completion = openai.Completion()

  with open("CLI/samples.txt") as file:
    default_log = "\n".join(file.readlines())

  def ask(question, chat_log):
    
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
      prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
      top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
      max_tokens=150)

    answer = response.choices[0].text.strip()
    return answer

  if __name__ == "__main__":
      
    question = name
    answer = ask(question, default_log)

    print(answer)

#  if answer == "'''":
 #   answer = "Answer:"

  print(answer)

  return render_template('index.html', answer=answer, name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True, port=8181)
