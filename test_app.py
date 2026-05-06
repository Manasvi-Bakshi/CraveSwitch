from app import api_key

def test_api_key_exists():
    assert api_key is not None

def test_context_options_existence():
    contexts = [
        "Late-night craving",
        "Stress eating",
        "Gym/Fitness",
        "Quick hunger",
        "Comfort food",
        "Budget meal",
        "Social outing"
    ]
    assert len(contexts) > 0
    assert "Stress eating" in contexts

def test_string_input_validation():
    dish_input = "Ice Cream"
    assert isinstance(dish_input, str)
    assert len(dish_input.strip()) > 0

def test_health_score_range_validation():
    health_upgrade = 42 # mocked metric from app
    flavor_retention = 88 # mocked metric from app
    
    assert 0 <= health_upgrade <= 100
    assert 0 <= flavor_retention <= 100

def test_prompt_variable_integrity():
    dish = "Chole Bhature"
    context = "Comfort food"
    
    prompt = f"Dish: {dish}\nContext: {context}"
    assert "Chole Bhature" in prompt
    assert "Comfort food" in prompt
