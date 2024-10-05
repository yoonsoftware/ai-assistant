import streamlit as st

def chat_ui(qa_system):
    """Streamlit을 이용한 AI 상담사 UI"""
    st.title("AI 상담사")

    if 'conversation_history' not in st.session_state:
        st.session_state['conversation_history'] = []

    user_input = st.text_input("상담사에게 물어보세요:")

    if user_input:
        answer = qa_system({"query": user_input})['result']
        st.session_state['conversation_history'].append((user_input, answer))

    if st.session_state['conversation_history']:
        for user_msg, ai_msg in st.session_state['conversation_history']:
            st.write(f"사용자: {user_msg}")
            st.write(f"상담사: {ai_msg}")
