from agent.state import TravelState
from agent.nodes.preference_extractor import extract_preferences
from agent.nodes.destination_finder import suggest_destination
from agent.nodes.itinerary_creator import create_itinerary
from agent.nodes.follow_up_handler import handle_follow_up

def run_travel_planner():
  state = TravelState()
  
  
  user_input = input("Tell me your preferences for trip (e.g. 'I want beach vacation in Asia'): ")
  extract_preferences(user_input, state)
  
  destination = suggest_destination(state)
  if destination:
    print(f"Recommended destination: {destination['name']}")
  else:
    print("Opps! Matching  destination not found")
    

  dates = input("What is your travel date?")
  create_itinerary(dates, destination["name"] if destination else "Unknown", state)
  
  question = input("Ask about anything else? i.e. weather")
  response = handle_follow_up(question, state)
  print(f"{response}")
  
  
  print("\n Final Travel plan:")
  print(state.current_itinerary)
  print("\n Conversation History")
  
  for msg in state.conversation_history:
    print("-", msg)