from agent.graph import run_travel_planner

def test_graph_execution():
  planner = run_travel_planner()
  
  assert "Santorini" in planner.messages[-2] or "Barcelona" in planner.messages[-2]
  assert isinstance(planner.itinerary, dict)
  
  print("Test Passed!")