import openai

openai.api_key = "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"
completion = openai.Completion()

with open("samples.txt") as file:
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
	while True:
		
		question = input("Q: ")
		answer = ask(question, default_log)
		print(answer)