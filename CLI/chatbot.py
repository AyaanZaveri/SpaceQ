import openai
import os

#To set API_KEY, type "export OPENAI_API_KEY=YOUR_KEY" in terminal
openai.api_key = os.getenv("OPENAI_API_KEY")

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
	qLog = []
	aLog = []
	while True:
		
		question = input("Q: ")
		answer = ask(question, default_log)

		qLog.append(question)
		aLog.append(answer)

		print(str(qLog))
		print(str(aLog))
		print(answer)