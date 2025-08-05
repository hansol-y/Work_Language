from schemas import Tone, MessageInput

def build_prompt(text: MessageInput) -> str:
    """
    Build a prompt based on the input text and tone.
    
    Args:
        text (MessageInput): The input message.
        
    Returns:
        str: The constructed prompt.
    """
    tone_descriptions = {
        Tone.VERY_POLITE: "very polite",
        Tone.POLITE: "polite",
        Tone.NEUTRAL: "neutral",
        Tone.DIRECT: "direct",
        Tone.VERY_DIRECT: "very direct"
    }

    print(f"Building prompt with tone: {tone_descriptions[text.tone]}")
    
    return f"Convert the following text to a {tone_descriptions[text.tone]} in tone:\n{text.text}"
