import sys 
 
class CoffeeBot: 
    def __init__(self): 
        # Define intents and their corresponding responses 
        self.responses = { 
            "greeting": ["hello", "hi", "hey", "good morning"], 
            "menu": ["menu", "order", "drink", "coffee", "tea"], 
            "hours": ["hours", "open", "time", "closing"], 
            "location": ["where", "address", "location", "place"], 
            "thanks": ["thanks", "thank you", "bye", "goodbye"] 
        } 
         
        self.answers = { 
            "greeting": "Hello! Welcome to Brew & Byte. How can I help you today?", 
            "menu": "We offer Espresso, Latte, Cappuccino, and Green Tea. Would you like to see prices?", 
            "hours": "We are open from 7:00 AM to 8:00 PM every day.", 
            "location": "You can find us at 123 Java Lane, Silicon Valley.", 
            "thanks": "You're welcome! Have a great day!", 
            "fallback": "I'm sorry, I didn't quite catch that. Could you try rephrasing? (Try: 'menu' or 'hours')" 
        } 
 
    def get_intent(self, user_input): 
        user_input = user_input.lower() 
        for intent, keywords in self.responses.items(): 
            for word in keywords: 
                if word in user_input: 
                    return intent 
        return "fallback" 
 
    def chat(self): 
        print("--- Brew & Byte Support Bot ---") 
        print("Type 'quit' to exit.") 
         
        while True: 
            user_text = input("You: ") 
            if user_text.lower() in ['quit', 'exit']: 
                print("Bot: Goodbye!") 
                break 
             
            intent = self.get_intent(user_text) 
            print(f"Bot: {self.answers[intent]}") 
 
# --- Built-in Execution --- 
if __name__ == "__main__": 
    # In a real environment, this would wait for user input. 
    # Here is a simulation of a customer interaction: 
    bot = CoffeeBot() 
     
    # Simulating a turn-based conversation logic 
    simulation_steps = [ 
        "Hi there!", 
        "What is on the menu?", 
        "Where are you located?", 
        "What is your opening time?", 
        "Thank you, bye!" 
    ] 
     
    for text in simulation_steps: 
        print(f"User: {text}") 
        intent = bot.get_intent(text) 
        print(f"Bot: {bot.answers[intent]}\n") 