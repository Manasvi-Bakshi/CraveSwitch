from app import api_key

def test_api_key_exists():
    assert api_key is not None

def test_context_options():
    contexts = [
        "Late-night craving",
        "Stress eating",
        "Gym/Fitness"
    ]
    assert len(contexts) > 0
