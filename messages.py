def get_message(emotion: str) -> str:
    messages = {
        "Crisis": "You're not alone. Please reach out to someone you trust or a crisis helpline right now. Your life has value.",
        "Stressed": "It sounds like you're carrying a lot right now. Take a slow breath — one thing at a time. You don't have to do it all at once.",
        "Anxious": "Anxiety can feel overwhelming. Try to ground yourself — notice 5 things around you. You are safe in this moment.",
        "Sad": "It's okay to feel sad. Let yourself feel it — these moments pass, and you don't have to face them alone.",
        "Happy": "It's wonderful to hear you're feeling good. Hold onto that lightness — you deserve it.",
        "Neutral": "I hear you. This space is yours — take your time and share whatever feels right.",
    }
    return messages.get(emotion, "I hear you. Take a breath — you're not alone.")


def get_resources(emotion: str) -> dict:
    resources = {
        "Crisis": {
            "music": "https://open.spotify.com/playlist/4QJuMGCyWgLBCNWnQMXydB",
            "video": "https://www.youtube.com/watch?v=inpok4MKVLM",
            "apps": "https://www.crisistextline.org",
        },
        "Stressed": {
            "music": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
            "video": "https://www.youtube.com/watch?v=aNXKjGFUlMs",
            "apps": "https://www.headspace.com",
        },
        "Anxious": {
            "music": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
            "video": "https://www.youtube.com/watch?v=1ZYbU82GVz4",
            "apps": "https://www.calm.com",
        },
        "Sad": {
            "music": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
            "video": "https://www.youtube.com/watch?v=RVA2N6tX2cg",
            "apps": "https://www.betterhelp.com",
        },
        "Happy": {
            "music": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
            "video": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "apps": "https://www.headspace.com",
        },
        "Neutral": {
            "music": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
            "video": "https://www.youtube.com/watch?v=inpok4MKVLM",
            "apps": "https://www.calm.com",
        },
    }
    return resources.get(emotion, {})