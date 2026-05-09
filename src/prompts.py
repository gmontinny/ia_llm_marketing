from dataclasses import dataclass


@dataclass
class ContentRequest:
    topic: str
    platform: str
    tone: str
    length: str
    audience: str
    include_cta: bool = False
    include_hashtags: bool = False
    keywords: str = ""


SYSTEM_PROMPT = "Você é um especialista em marketing digital com foco em SEO e escrita persuasiva."


def build_user_prompt(request: ContentRequest) -> str:
    prompt = f"""Gere um conteúdo de marketing com as seguintes especificações:

- Tema: {request.topic}
- Plataforma: {request.platform}
- Tom: {request.tone}
- Tamanho: {request.length}
- Público-alvo: {request.audience}"""

    if request.keywords:
        prompt += f"\n- Palavras-chave para incluir naturalmente no texto: {request.keywords}"

    if request.include_cta:
        prompt += "\n- Inclua uma chamada para ação (CTA) ao final do texto."

    if request.include_hashtags:
        prompt += "\n- Inclua hashtags relevantes ao final."

    prompt += "\n\nRetorne apenas o conteúdo gerado, sem explicações adicionais."
    return prompt
