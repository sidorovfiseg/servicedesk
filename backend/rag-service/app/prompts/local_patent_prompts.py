from langchain.prompts import PromptTemplate

# Prompt for translating text from Russian to English
ru_en_translation_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Translate this text into English. The answer should contain only a translation of the text without additional explanations. There is no need to explain that this is a translated text.
text: `{text}`
""",
)

# Prompt for translating text from English to Russian
en_ru_translation_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Translate this text into Russian. The answer should contain only a translation of the text without additional explanations. There is no need to explain that this is a translated text.
text: `{text}`
""",
)

# Prompt to generate questions based on a given Russian text
questions_to_text_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Придумай несколько вопросов, на которые отвечает данный текст. Ответ должен содержать только придуманные тобой вопросы, через запятую.
текст: `{text}`
""",
)

# Prompt for generating questions and answers based on a given Russian text
context_compression_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Придумай несколько вопросов к тексту и напиши ответы на них. Перечисли вопросы и ответы через запятую.
текст: `{text}`
""",
)

# Prompt to assist in identifying information in a patent report based on Russian text
get_id_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Ты — русскоязычный автоматический ассистент патентного отдела. Ты помогаешь людям находить точную информацию в тексте отчета.
Отвечай на вопрос пользователя только на основе информации из отчета. Если фрагмент отчета не содержит
релевантной информации, отвечай: не достаточно информации для ответа.
текст: `{text}`
""",
)
