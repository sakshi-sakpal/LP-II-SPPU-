def chatbot():
    print("🤖 Hello! I'm SakshiBot. How can I help you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("🤖 Thank you for visiting! Have a great day.")
            break
        elif 'book' in user_input or 'buy' in user_input:
            print("🤖 You can browse our collection at sakshi-elibrary.com/books.")
        elif 'read' in user_input:
            print("🤖 You can read free e-books once you sign in to your account.")
        elif 'account' in user_input or 'login' in user_input:
            print("🤖 Visit sakshi-elibrary.com/login to access your account.")
        elif 'help' in user_input or 'support' in user_input:
            print("🤖 You can contact support at support@sakshi-elibrary.com.")
        else:
            print("🤖 Sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
