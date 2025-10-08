#!/usr/bin/env python3
"""
Test suite for Green Hops Chatbot
Basic tests to verify chatbot functionality
"""

import unittest
from chatbot import GreenHopsChatbot


class TestGreenHopsChatbot(unittest.TestCase):
    """Test cases for Green Hops Chatbot"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bot = GreenHopsChatbot()
    
    def test_greeting(self):
        """Test that greeting is generated correctly"""
        greeting = self.bot.greet()
        self.assertIn("Green Hops", greeting)
        self.assertIn("Bienvenido", greeting)
    
    def test_show_products(self):
        """Test product catalog display"""
        products = self.bot.show_products()
        self.assertIn("IPA", products)
        self.assertIn("Pale Ale", products)
        self.assertIn("Stout", products)
        self.assertIn("Lager", products)
    
    def test_show_brewery_info(self):
        """Test brewery information display"""
        info = self.bot.show_brewery_info()
        self.assertIn("Chía, Colombia", info)
        self.assertIn("Green Hops", info)
    
    def test_show_faqs(self):
        """Test FAQ display"""
        faqs = self.bot.show_faqs()
        self.assertIn("horario", faqs.lower())
        self.assertIn("delivery", faqs.lower())
    
    def test_process_products_query(self):
        """Test product query processing"""
        response = self.bot.process_input("productos")
        self.assertIn("Cervezas Artesanales", response)
        
        response = self.bot.process_input("cervezas")
        self.assertIn("IPA", response)
    
    def test_process_hours_query(self):
        """Test hours query processing"""
        response = self.bot.process_input("horario")
        self.assertIn("Lunes a Sábado", response)
    
    def test_process_location_query(self):
        """Test location query processing"""
        response = self.bot.process_input("ubicacion")
        self.assertIn("Chía", response)
    
    def test_process_delivery_query(self):
        """Test delivery query processing"""
        response = self.bot.process_input("delivery")
        self.assertIn("domicilio", response)
        
        response = self.bot.process_input("hacen entregas?")
        self.assertIn("domicilio", response)
    
    def test_process_price_query(self):
        """Test price query processing"""
        response = self.bot.process_input("cuanto cuesta")
        self.assertIn("precio", response.lower())
    
    def test_process_greeting(self):
        """Test greeting processing"""
        response = self.bot.process_input("hola")
        self.assertIn("Hola", response)
        
        response = self.bot.process_input("buenos dias")
        self.assertIn("Bienvenido", response)
    
    def test_process_exit(self):
        """Test exit command processing"""
        response = self.bot.process_input("salir")
        self.assertIn("Gracias", response)
        
        response = self.bot.process_input("adios")
        self.assertIn("Gracias", response)
    
    def test_process_info_query(self):
        """Test info query processing"""
        response = self.bot.process_input("info")
        self.assertIn("Green Hops", response)
        
        response = self.bot.process_input("sobre nosotros")
        self.assertIn("Cervecería", response)
    
    def test_process_events_query(self):
        """Test events query processing"""
        response = self.bot.process_input("eventos")
        self.assertIn("cata", response.lower())
    
    def test_process_reservations_query(self):
        """Test reservations query processing"""
        response = self.bot.process_input("reservas")
        self.assertIn("reservas", response.lower())
    
    def test_process_unknown_query(self):
        """Test unknown query processing"""
        response = self.bot.process_input("xyz123")
        self.assertIn("Lo siento", response)
    
    def test_brewery_info_structure(self):
        """Test brewery info data structure"""
        self.assertEqual(self.bot.brewery_info['name'], 'Green Hops Cervecería Artesanal')
        self.assertEqual(self.bot.brewery_info['location'], 'Chía, Colombia')
    
    def test_products_structure(self):
        """Test products data structure"""
        self.assertIn('IPA', self.bot.products)
        self.assertIn('Pale Ale', self.bot.products)
        self.assertIn('Stout', self.bot.products)
        self.assertIn('Lager', self.bot.products)
        
        # Check product structure
        ipa = self.bot.products['IPA']
        self.assertIn('name', ipa)
        self.assertIn('type', ipa)
        self.assertIn('abv', ipa)
        self.assertIn('description', ipa)
        self.assertIn('price', ipa)


class TestChatbotResponses(unittest.TestCase):
    """Test chatbot response quality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bot = GreenHopsChatbot()
    
    def test_responses_are_non_empty(self):
        """Test that responses are not empty"""
        test_inputs = ['productos', 'info', 'horario', 'ubicacion', 'faq']
        for input_text in test_inputs:
            response = self.bot.process_input(input_text)
            self.assertTrue(len(response) > 0, f"Empty response for: {input_text}")
    
    def test_responses_are_in_spanish(self):
        """Test that responses are in Spanish"""
        response = self.bot.process_input("productos")
        # Check for Spanish words
        spanish_indicators = ['Cerveza', 'Precio', 'Artesanal', 'Nuestras']
        self.assertTrue(any(word in response for word in spanish_indicators))


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == "__main__":
    run_tests()
