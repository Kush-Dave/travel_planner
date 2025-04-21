# import state as st

def extract_preferences(user_input, state):
  preferences = {}
  
  if "beach" in user_input.lower():
    preferences["trip_type"]  = "beach"
    
  elif "adventure" in user_input.lower():
    preferences["trip_type"] = "adventure"
  
    
  if "asia" in user_input.lower():
    preferences["region"] = "asia"
  
  elif "oceania" in user_input.lower():
    preferences["region"] = "oceania"
  
  
  state.update_preferences(preferences)
  