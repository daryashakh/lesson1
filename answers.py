def get_answers(question,answers):
	return answers.get(question)

question=input("Введи вопрос")
answers={" привет": " И тебе привет!", " как дела": " Лучше всех", " пока": "Увидимся"}	
get_answers(question, answers);
print (get_answers(question, answers))