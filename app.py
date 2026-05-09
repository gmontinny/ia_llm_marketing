import streamlit as st

from src.config import PROVIDERS, PLATFORMS, TONES, LENGTHS, AUDIENCES
from src.prompts import ContentRequest
from src.chain import generate_content

st.set_page_config(page_title="Gerador de Conteúdo - Marketing", page_icon="📝")
st.title("📝 Gerador de Conteúdo para Marketing")
st.markdown("Gere conteúdos adaptados ao seu público e canal de divulgação usando IA.")

with st.form("content_form"):
    topic = st.text_input("Tema", placeholder="Ex: saúde mental, alimentação saudável, prevenção...")

    col1, col2 = st.columns(2)
    with col1:
        provider = st.selectbox("Provedor de IA", PROVIDERS)
        platform = st.selectbox("Plataforma", PLATFORMS)
        tone = st.selectbox("Tom", TONES)
    with col2:
        length = st.selectbox("Tamanho", LENGTHS)
        audience = st.selectbox("Público-alvo", AUDIENCES)

    col3, col4 = st.columns(2)
    with col3:
        include_cta = st.checkbox("Incluir CTA (chamada para ação)")
    with col4:
        include_hashtags = st.checkbox("Retornar Hashtags")

    keywords = st.text_area(
        "Palavras-chave (SEO)",
        placeholder="Ex: bem-estar, medicina preventiva...",
        height=68,
    )

    submitted = st.form_submit_button("🚀 Gerar conteúdo")

if submitted:
    if not topic.strip():
        st.warning("Por favor, informe o tema do conteúdo.")
    else:
        request = ContentRequest(
            topic=topic,
            platform=platform,
            tone=tone,
            length=length,
            audience=audience,
            include_cta=include_cta,
            include_hashtags=include_hashtags,
            keywords=keywords,
        )

        with st.spinner("Gerando conteúdo..."):
            try:
                result = generate_content(request, provider)
                st.markdown("---")
                st.subheader("Resultado")
                st.markdown(result)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
