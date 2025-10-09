import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="🍺 Green Hops ChatBot", 
    page_icon="🍺",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
.main-header { font-size: 3em; text-align: center; color: #2E8B57; }
.chat-bubble { background: #2E8B57; color: white; padding: 15px; 
               border-radius: 15px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown('<h1 class="main-header">🍺 Green Hops ChatBot</h1>', unsafe_allow_html=True)
st.markdown("### Cervecería Artesanal - Chía, Cundinamarca, Colombia")

# Base de conocimientos
knowledge_base = {
    'cervezas': {
        'sue': 'SUE es nuestra American Pale Ale con sabor refrescante y notas cítricas.',
        'chia': 'CHÍA es una Porter Oscura con sabores a café tostado y chocolate amargo.',
        'nencatacoa': 'NENCATACOA es una Irish Red con delicioso sabor a caramelo.',
        'ipa': 'IPA LIMÓN Y COCO es una India Pale Ale con cítricos refrescantes.',
        'doce': 'DOCE UVAS es una Grape Ale Dorada con sabores frutales únicos.'
    },
    'ubicacion': 'Estamos ubicados en Chía, Cundinamarca, Colombia. Maps: https://maps.app.goo.gl/CbuBREg6N5ghWwuL9',
    'horarios': 'Abrimos fines de semana de 3:00 PM a 12:00 AM',
    'contacto': 'WhatsApp: 3012802229 | Instagram: @greenhopsbeer',
    'mascotas': '¡Somos Pet Friendly! Las mascotas son bienvenidas.'
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for cerveza, info in knowledge_base['cervezas'].items():
        if cerveza in user_input:
            return f"🍺 {info}"
    
    if any(word in user_input for word in ['ubicacion', 'donde', 'direccion']):
        return f"📍 {knowledge_base['ubicacion']}"
    elif any(word in user_input for word in ['horario', 'abierto', 'cuando']):
        return f"🕒 {knowledge_base['horarios']}"
    elif any(word in user_input for word in ['contacto', 'telefono', 'whatsapp']):
        return f"📞 {knowledge_base['contacto']}"
    elif any(word in user_input for word in ['mascota', 'perro', 'gato', 'pet']):
        return f"🐕 {knowledge_base['mascotas']}"
    elif any(word in user_input for word in ['hola', 'buenas', 'saludos']):
        return "¡Hola! 🍺 Bienvenido a Green Hops. ¿Te gustaría conocer nuestras cervezas artesanales?"
    else:
        return "🤔 Puedo ayudarte con: cervezas, ubicación, horarios, contacto, mascotas. ¿Qué te interesa?"

# Interfaz principal
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 💬 Chat con Green Hops")
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    user_input = st.text_input("Escribe tu pregunta:", placeholder="Ej: ¿Qué cervezas tienen?")
    
    if user_input:
        st.session_state.messages.append(("Usuario", user_input))
        response = get_response(user_input)
        st.session_state.messages.append(("Bot", response))
    
    for sender, message in st.session_state.messages[-6:]:
        if sender == "Usuario":
            st.markdown(f"**Tú:** {message}")
        else:
            st.markdown(f'<div class="chat-bubble">{message}</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🍻 Nuestras Cervezas")
    
    cervezas_info = [
        "🍺 **SUE** - American Pale Ale",
        "🍺 **CHÍA** - Porter Oscura", 
        "🍺 **NENCATACOA** - Irish Red",
        "🍺 **IPA LIMÓN Y COCO** - IPA",
        "🍺 **DOCE UVAS** - Grape Ale"
    ]
    
    for cerveza in cervezas_info:
        st.markdown(cerveza)
    
    st.markdown("---")
    st.markdown("### 📞 Contacto")
    st.markdown("📱 WhatsApp: 3012802229")
    st.markdown("📸 [@greenhopsbeer](https://www.instagram.com/greenhopsbeer)")
    st.markdown("📍 Chía, Cundinamarca")
    st.markdown("🕒 Fines de semana 3PM-12AM")
    
    if st.button("🗑️ Limpiar Chat"):
        st.session_state.messages = []
        st.rerun()

st.markdown("---")
st.markdown("*Desarrollado por Mery Anne Escobar Hitscherich - Maestra Cervecera*")
st.markdown("*Green Hops © 2025 - Cervecería Artesanal*")
