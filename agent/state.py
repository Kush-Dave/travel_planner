class TravelState:
  def __init__(self):
    self.user_preferences = {}
    self.selected_destinations = []
    self.current_itinerary = {}
    self.conversation_history = []
    
  def update_preferences(self, preferences):
    self.user_preferences.update(preferences)
    self.conversation_history.append(f"Preferences Updated: {preferences}")
    
  def add_selected_destination(self, destination):
    self.selected_destinations.append(destination)
    self.conversation_history.append(f"Destination selected: {destination}")
    
  def update_itinerary(self, itinerary):
    self.current_itinerary.update(itinerary)
    self.conversation_history.append(f"Itinerary updated: {itinerary}")
    
  def add_message(self, message):
    self.conversation_history.append(message)