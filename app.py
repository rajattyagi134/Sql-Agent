from agent import SQLAgent

agent = SQLAgent()

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":

        break

    response = agent.answer_question(question)

    if response["success"]:

        print("\nAnswer:\n")

        print(response["answer"])

    else:

        print(response["error"])

agent.close()