

def create_itinerary(dates, destination, state):
  itinerary = {
    "destination" : destination,
    "dates" : dates,
    "plan" : f"Enjoy your trip to {destination} from {dates}. Have fun!"
  }
  
  state.update_itinerary(itinerary)