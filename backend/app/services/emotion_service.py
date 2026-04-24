def detect_emotion(text: str) -> str:
    """
    Detect emotion from text using improved keyword matching.

    Returns:
        sad | angry | happy | anxious | neutral
    """

    text = text.lower()

    sad_words = ["sad", "tired", "exhausted", "down", "depressed", "low"]
    angry_words = ["angry", "mad", "frustrated", "annoyed"]
    happy_words = ["happy", "great", "good", "excited", "joy"]
    anxious_words = ["anxious", "worried", "stress", "nervous", "overwhelmed"]

    if any(word in text for word in sad_words):
        return "sad"

    elif any(word in text for word in angry_words):
        return "angry"

    elif any(word in text for word in happy_words):
        return "happy"

    elif any(word in text for word in anxious_words):
        return "anxious"

    else:
        return "neutral"