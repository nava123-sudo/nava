import openai
import random


openai.api_key ="AIzaSyAS3xt-C3n_vS_ayvpUBvoLfyfA5K-zCcQ"



joke_list = [
    "Why did the chicken join a band? Because it had the drumsticks!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I used to play piano by ear, but now I use my hands.",
    "Parallel lines have so much in common... it’s a shame they’ll never meet.",
]

def get_comedic_response(prompt):
    """
    Generates a humorous response to the user input.
    """


    intros = [
        "Alright, let’s get real here...",
        "Oh, that reminds me...",
        "Speaking of which, did you know...",
        "Now, I know what you're thinking...",
        "Classic! This is just like that time when...",
    ]
    intro = random.choice(intros)


    if random.random() < 0.3:
        response = f"{intro} {random.choice(joke_list)}"
        return response


    try:
        response = openai.Completion.create(
            model="text-davinci-004",
            prompt=f"You’re a stand-up comedian responding to the following: '{prompt}'. Keep it funny, light, and a bit sarcastic.",
            max_tokens=100,
            temperature=0.8,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0.3
        )


        return f"{intro} {response.choices[0].text.strip()}"

    except Exception as e:
        return f"Oh no, looks like the tech gods aren't on our side today! Here's a joke instead: {random.choice(joke_list)}"


def start_comedy_chatbot():
    print("Welcome to the Comedy Club Bot! Let's get funny.\n")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "stop"]:
            print("Comedy Bot: Alright, I'm out! Catch you next time!")
            break

        response = get_comedic_response(user_input)
        print(f"Comedy Bot: {response}\n")


if __name__ == "__main__":
    start_comedy_chatbot()
