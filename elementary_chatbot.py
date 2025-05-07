# elementary_chatbot.py

def chatbot():
    print("Welcome to ShopBot! How can I assist you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("ShopBot: Thank you for visiting! Have a great day.")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ShopBot: Hello! How can I help you?")
        elif 'order' in user_input:
            print("ShopBot: You can check your order status by logging into your account and visiting the 'My Orders' page.")
        elif 'return' in user_input:
            print("ShopBot: Our return policy allows returns within 30 days of delivery. Would you like to start a return?")
        elif 'refund' in user_input:
            print("ShopBot: Refunds are processed within 5–7 business days after the return is received.")
        elif 'shipping' in user_input:
            print("ShopBot: Standard shipping takes 3–5 business days. Expedited options are also available.")
        elif 'payment' in user_input:
            print("ShopBot: We accept Visa, MasterCard, PayPal, and UPI.")
        else:
            print("ShopBot: I'm sorry, I didn't understand that. Could you rephrase?")

if __name__ == "__main__":
    chatbot()
