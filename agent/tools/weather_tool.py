import random

def get_mock_weather(destination):
  conditions = ["sunny", "cloudy", "rainy", "stormy"]
  temp = random.randint(15, 35)
  return f"Weather in {destination}: {temp}°C, {random.choice(conditions)}"
