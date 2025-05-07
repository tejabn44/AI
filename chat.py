def chatbot():
    print("TechBot: Hello! I’m TechBot. How can I help you today?")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "internet" in user_input:
            print("TechBot: Please check your router or modem. Try restarting it.")
        elif "slow" in user_input:
            print("TechBot: You may have background downloads or too many devices connected.")
        elif "wifi" in user_input:
            print("TechBot: Try reconnecting to the Wi-Fi or resetting your network settings.")
        elif "plan" in user_input:
            print("TechBot: You can check your data plan in your customer dashboard online.")
        elif "help" in user_input:
            print("TechBot: I can help you with internet, speed issues, or account info.")
        elif "bye" in user_input:
            print("TechBot: Goodbye! Have a great day.")
            break
        else:
            print("TechBot: I'm sorry, I didn’t understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
