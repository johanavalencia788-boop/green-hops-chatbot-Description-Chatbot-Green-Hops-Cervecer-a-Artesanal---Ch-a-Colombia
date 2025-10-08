#!/usr/bin/env python3
"""
Green Hops Chatbot - Cervecería Artesanal de Chía, Colombia
Interactive chatbot to assist customers with product information, brewery details, and FAQs.
"""

import re
from datetime import datetime


class GreenHopsChatbot:
    """Chatbot for Green Hops Craft Brewery"""
    
    def __init__(self):
        self.brewery_info = {
            'name': 'Green Hops Cervecería Artesanal',
            'location': 'Chía, Colombia',
            'description': 'Cervecería artesanal colombiana dedicada a producir cervezas de alta calidad con ingredientes naturales.',
            'specialty': 'Cervezas artesanales con lúpulo fresco y ingredientes locales',
            'hours': 'Lunes a Sábado: 12:00 PM - 10:00 PM, Domingo: 12:00 PM - 8:00 PM'
        }
        
        self.products = {
            'IPA': {
                'name': 'Green Hops IPA',
                'type': 'India Pale Ale',
                'abv': '6.5%',
                'description': 'IPA con aroma cítrico y floral, amargor equilibrado',
                'price': '$8.000 COP'
            },
            'Pale Ale': {
                'name': 'Pale Ale Artesanal',
                'type': 'American Pale Ale',
                'abv': '5.2%',
                'description': 'Cerveza clara con notas maltosas y lúpulo americano',
                'price': '$7.000 COP'
            },
            'Stout': {
                'name': 'Stout Colombiana',
                'type': 'Coffee Stout',
                'abv': '7.0%',
                'description': 'Cerveza oscura con notas de café y chocolate',
                'price': '$9.000 COP'
            },
            'Lager': {
                'name': 'Lager Fresca',
                'type': 'Premium Lager',
                'abv': '4.8%',
                'description': 'Cerveza ligera y refrescante, perfecta para el clima',
                'price': '$6.500 COP'
            }
        }
        
        self.faqs = {
            'horario': 'Nuestro horario es de Lunes a Sábado de 12:00 PM a 10:00 PM, y Domingos de 12:00 PM a 8:00 PM.',
            'ubicacion': 'Estamos ubicados en Chía, Colombia. ¡Visítanos!',
            'delivery': 'Sí, hacemos entregas a domicilio en Chía y alrededores. Pedido mínimo de $20.000 COP.',
            'eventos': 'Organizamos eventos de cata y tours de la cervecería. Consulta disponibilidad.',
            'reservas': 'Puedes hacer reservas llamando o escribiendo a nuestras redes sociales.',
            'proceso': 'Elaboramos nuestras cervezas artesanalmente usando malta de calidad, lúpulo fresco y agua pura.',
            'ingredientes': 'Utilizamos solo ingredientes naturales: malta, lúpulo, levadura y agua. Sin conservantes.'
        }
        
    def greet(self):
        """Return greeting message"""
        return f"""
¡Bienvenido a {self.brewery_info['name']}! 🍺
{self.brewery_info['description']}

¿En qué puedo ayudarte hoy?
Puedes preguntarme sobre:
- Productos (escribe 'productos' o 'cervezas')
- Información del establecimiento (escribe 'info' o 'sobre nosotros')
- Preguntas frecuentes (escribe 'faq' o 'ayuda')
- Horarios (escribe 'horario')
- Ubicación (escribe 'ubicacion')

Escribe 'salir' para terminar la conversación.
"""
    
    def show_products(self):
        """Display all available products"""
        response = "\n🍺 Nuestras Cervezas Artesanales:\n"
        response += "=" * 50 + "\n"
        for key, product in self.products.items():
            response += f"\n📌 {product['name']} ({product['type']})\n"
            response += f"   ABV: {product['abv']}\n"
            response += f"   {product['description']}\n"
            response += f"   Precio: {product['price']}\n"
        return response
    
    def show_brewery_info(self):
        """Display brewery information"""
        response = f"\n🏭 {self.brewery_info['name']}\n"
        response += "=" * 50 + "\n"
        response += f"📍 Ubicación: {self.brewery_info['location']}\n"
        response += f"✨ Especialidad: {self.brewery_info['specialty']}\n"
        response += f"🕐 Horario: {self.brewery_info['hours']}\n"
        response += f"\n{self.brewery_info['description']}\n"
        return response
    
    def show_faqs(self):
        """Display frequently asked questions"""
        response = "\n❓ Preguntas Frecuentes:\n"
        response += "=" * 50 + "\n"
        for topic, answer in self.faqs.items():
            response += f"\n• {topic.capitalize()}: {answer}\n"
        return response
    
    def process_input(self, user_input):
        """Process user input and return appropriate response"""
        user_input = user_input.lower().strip()
        
        # Exit commands
        if user_input in ['salir', 'exit', 'quit', 'adios', 'chao']:
            return "¡Gracias por visitar Green Hops! 🍺 ¡Hasta pronto!"
        
        # Greetings
        if any(word in user_input for word in ['hola', 'hello', 'hi', 'buenos dias', 'buenas tardes', 'buenas noches']):
            return "¡Hola! Bienvenido a Green Hops. ¿En qué puedo ayudarte?"
        
        # Products
        if any(word in user_input for word in ['producto', 'cerveza', 'beer', 'catalogo', 'menu', 'que tienen']):
            return self.show_products()
        
        # Brewery info
        if any(word in user_input for word in ['info', 'sobre', 'acerca', 'nosotros', 'quienes']):
            return self.show_brewery_info()
        
        # FAQs
        if any(word in user_input for word in ['faq', 'ayuda', 'help', 'pregunta']):
            return self.show_faqs()
        
        # Hours
        if any(word in user_input for word in ['horario', 'hora', 'abierto', 'cerrado', 'cuando']):
            return f"🕐 {self.faqs['horario']}"
        
        # Location
        if any(word in user_input for word in ['ubicacion', 'donde', 'direccion', 'location']):
            return f"📍 {self.faqs['ubicacion']}"
        
        # Delivery
        if any(word in user_input for word in ['delivery', 'domicilio', 'envio', 'entregar', 'entrega']):
            return f"🚚 {self.faqs['delivery']}"
        
        # Events
        if any(word in user_input for word in ['evento', 'cata', 'tour', 'visita']):
            return f"🎉 {self.faqs['eventos']}"
        
        # Reservations
        if any(word in user_input for word in ['reserva', 'reservar', 'booking']):
            return f"📞 {self.faqs['reservas']}"
        
        # Process
        if any(word in user_input for word in ['proceso', 'como hacen', 'elaboracion', 'fabrican']):
            return f"⚙️ {self.faqs['proceso']}"
        
        # Ingredients
        if any(word in user_input for word in ['ingrediente', 'natural', 'organico']):
            return f"🌿 {self.faqs['ingredientes']}"
        
        # Price queries
        if any(word in user_input for word in ['precio', 'costo', 'cuanto', 'vale']):
            return "Nuestros precios varían entre $6.500 y $9.000 COP. Escribe 'productos' para ver el catálogo completo con precios."
        
        # Default response
        return """
Lo siento, no entendí tu pregunta. Puedo ayudarte con:
- Productos/Cervezas
- Información del establecimiento
- Horarios y ubicación
- Preguntas frecuentes (FAQ)

¿Sobre qué te gustaría saber?
"""
    
    def run(self):
        """Run the chatbot in interactive mode"""
        print(self.greet())
        
        while True:
            try:
                user_input = input("\n💬 Tú: ").strip()
                
                if not user_input:
                    continue
                
                response = self.process_input(user_input)
                print(f"\n🤖 Green Hops Bot: {response}")
                
                if "¡Gracias por visitar" in response:
                    break
                    
            except KeyboardInterrupt:
                print("\n\n¡Gracias por visitar Green Hops! 🍺 ¡Hasta pronto!")
                break
            except EOFError:
                print("\n\n¡Gracias por visitar Green Hops! 🍺 ¡Hasta pronto!")
                break


def main():
    """Main entry point"""
    chatbot = GreenHopsChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
