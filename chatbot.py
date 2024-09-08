def movies_chatbot():
    print("Hello! I'm your Movies Chatbot. How can I assist you with movie information today?")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! What movie information are you looking for?")
        elif "popular movies" in user_input:
            print("Chatbot: Some popular movies right now are 'Oppenheimer', 'Barbie', and 'Mission: Impossible – Dead Reckoning'.")
        elif "upcoming movies" in user_input:
            print("Chatbot: Upcoming movies include 'Dune: Part Two', 'The Marvels', and 'Killers of the Flower Moon'.")
        elif "best movies of all time" in user_input:
            print("Chatbot: Some of the best movies of all time include 'The Godfather', 'The Shawshank Redemption', and 'The Dark Knight'.")
        elif "who directed" in user_input:
            if "inception" in user_input:
                print("Chatbot: 'Inception' was directed by Christopher Nolan.")
            elif "pulp fiction" in user_input:
                print("Chatbot: 'Pulp Fiction' was directed by Quentin Tarantino.")
            elif "the godfather" in user_input:
                print("Chatbot: 'The Godfather' was directed by Francis Ford Coppola.")
            else:
                print("Chatbot: I can help with the director if you provide a specific movie title.")
        elif "movie recommendations" in user_input:
            print("Chatbot: Based on your interests, you might enjoy 'The Grand Budapest Hotel', 'Mad Max: Fury Road', or 'Parasite'.")
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Enjoy your movie time!")
            break
        else:
            print("Chatbot: I'm not sure about that. Can you ask something else related to movies?")

# Run the chatbot
movies_chatbot()