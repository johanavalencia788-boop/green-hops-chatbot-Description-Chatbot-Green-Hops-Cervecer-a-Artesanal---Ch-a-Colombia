#!/usr/bin/env python3
"""
Demo script for Green Hops Chatbot
Shows example interactions with the chatbot
"""

from chatbot import GreenHopsChatbot


def run_demo():
    """Run a demonstration of the chatbot's capabilities"""
    bot = GreenHopsChatbot()
    
    print("=" * 60)
    print("DEMO: Green Hops Chatbot - Cervecería Artesanal")
    print("=" * 60)
    
    # List of demo interactions
    demo_interactions = [
        ("hola", "Greeting the chatbot"),
        ("productos", "Viewing product catalog"),
        ("cuanto cuesta la IPA?", "Asking about prices"),
        ("horario", "Checking business hours"),
        ("hacen delivery?", "Asking about delivery service"),
        ("donde estan ubicados?", "Asking for location"),
        ("info", "Getting brewery information"),
        ("eventos", "Asking about events"),
    ]
    
    for user_input, description in demo_interactions:
        print(f"\n{'─' * 60}")
        print(f"Demo: {description}")
        print(f"{'─' * 60}")
        print(f"💬 Usuario: {user_input}")
        response = bot.process_input(user_input)
        print(f"🤖 Bot: {response}")
        print()
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print("\nTo run the chatbot interactively, execute: python chatbot.py")


if __name__ == "__main__":
    run_demo()
