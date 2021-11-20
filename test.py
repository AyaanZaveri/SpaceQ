import openai

openai.api_key = "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"
completion = openai.Completion()

default_log = '''Human: How big is the sun?
AI: The sun is about 1.39 million kilometers (864,000 miles) in diameter. (The diameter we see is from Earth's perspective, but the sun is much bigger from the sun's perspective.)
Human: How hot is the sun?
AI: The temperature inside the sun is about 15 million degrees Celsius. (It is much hotter than that, but we cannot see the temperature from here because of the size of the sun.)
Human: How many planets are there?
AI: There are eight planets in our solar system.
Human: Can we see the other planets?
AI: Yes, we can see them with a telescope.
Human: How far away is the sun?
AI: The sun is 93 million miles away from Earth. (It is much farther away than that, but we cannot see the distance from here.)
Human: What is the sun made of?
AI: The sun is made mostly of hydrogen and a little bit of helium.
Human: How long does it take for the sun to circle Earth?
AI: It takes the sun about a month to circle the Earth.
Human: How far away is the moon?
AI: The moon is about 230,000 miles away from Earth.
Human: What is the moon made of?
AI: The moon is made mostly of rock and dust.
Human: How big is the moon?
AI: The moon is about 2,000 miles across.
Human: How many moons does Earth have?
AI: Earth has one moon.
'''

def ask(question, chat_log=None):

	if chat_log is None:
		chat_log = default_log
	
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
		answer = ask(question)
		print(answer)
