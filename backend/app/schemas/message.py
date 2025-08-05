from enum import Enum
from pydantic import BaseModel

class Tone(Enum):
    """
    Enum for different tones of messages.
    """
    VERY_POLITE = 1
    POLITE = 2
    NEUTRAL = 3
    DIRECT = 4
    VERY_DIRECT = 5
    

class MessageInput(BaseModel):
    """
    Schema for input messages.
    """
    text: str
    tone: Tone
    
class ConvertedOutput(BaseModel):
    output: str