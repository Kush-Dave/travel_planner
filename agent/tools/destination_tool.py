import json
import os

def load_destinations():
  path = os.path.join(os.path.dirname(__file__), "C:\\Users\\Kush\\Desktop\\travel_planner\\agent\\data\\destination.json")
  with open(path, 'r') as file:
    return json.load(file)
  
def find_destinations(trip_type, region):
  data = load_destinations()
  matches = data.get(trip_type.lower(), [])
  if region:
    matches = [dest for dest in matches if dest['region'].lower() == region.lower()]
  
  return matches