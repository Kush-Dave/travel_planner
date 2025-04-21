from agent.tools.weather_tool import get_mock_weather

def handle_follow_up(question, state):
  if "weather" in question.lower():
    dest = state.selected_destinations[-1] if state.selected_destinations else "Unknown"
    forecast = get_mock_weather(dest)
    state.add_message(f"Weather info: {forecast}")
    return forecast
  