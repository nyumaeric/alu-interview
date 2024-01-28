def rain(walls):
  """
  Calculates the total amount of rainwater retained in a cross-section of walls.

  Args:
    walls: A list of non-negative integers representing the heights of walls with unit width 1.

  Returns:
    An integer indicating the total amount of rainwater retained in square units.
  """
  # Check for empty list
  if not walls:
    return 0

  # Initialize variables
  total_water = 0
  current_max = 0

  # Iterate through the wall heights
  for height in walls:
    # Calculate potential water accumulation based on current height and previous max
    water_accumulation = min(height, current_max) - height

    # Add accumulated water to total
    total_water += water_accumulation

    # Update current max height
    current_max = max(current_max, height)

  return total_water
