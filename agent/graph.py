from agent.state import TravelState
from agent.nodes.preference_extractor import extract_preferences
from agent.nodes.destination_finder import suggest_destination
from agent.nodes.itinerary_creator import create_itinerary
from agent.nodes.follow_up_handler import handle_follow_up

def run_travel_planner():
  state = TravelState()