# import state as st

def extract_preferences(user_input, state):
  preferences = {}
  
  if "beach" in user_input.lower():
    preferences["trip_type"]  = "beach"
    
  elif "adventure" in user_input.lower():
    preferences["trip_type"] = "adventure"
  
  elif "romantic" in user_input.lower():
    preferences["trip_type"] = "romantic"
    
  elif "cultural" in user_input.lower():
    preferences["trip_type"] = "cultural"
  
  elif "wildlife" in user_input.lower():
    preferences["trip_type"] = "wildlife"
    
  elif "ecotourism" in user_input.lower():
    preferences["trip_type"] = "ecotourism"
    
    
  if "asia" in user_input.lower():
    preferences["region"] = "asia"
  
  elif "oceania" in user_input.lower():
    preferences["region"] = "oceania"
  
  elif "africa" in user_input.lower():
    preferences["region"] = "africa"
  
  elif "australia" in user_input.lower():
    preferences["region"] = "australia"  
    
  elif "Europe" in user_input.lower():
    preferences["region"] = "Europe"
    
  elif "southkorea" in user_input.lower():
    preferences["region"] = "southkorea"
  
  state.update_preferences(preferences)
  