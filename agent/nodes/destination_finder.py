from agent.tools.destination_tool import find_destinations

def suggest_destination(state):
  trip_type = state.user_preferences.get("trip_type", "")
  region = state.user_preferences.get("region", "")
  destinations = find_destinations(trip_type, region)
  if destinations:
    state.add_selected_destination(destinations[0]['name'])
    return destinations[0]
  
  return None