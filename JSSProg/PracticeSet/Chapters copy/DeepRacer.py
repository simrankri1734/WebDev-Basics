# def reward_function(params):
#     # Extract parameters
#     distance_from_center = params['distance_from_center']
#     track_length = params['track_length']
#     speed = params['speed']
#     heading = params['heading']
#     waypoints = params['waypoints']
#     closest_objects = params['closest_objects']
#     closest_objects_distance = params['closest_objects_distance']

#     # Reward for staying on the track center
#     reward = 1 - (distance_from_center / (track_length / 2))
    
#     # Reward for high speed
#     reward += speed / 10
    
#     # Reward for heading towards the next waypoint
#     next_waypoint = waypoints[closest_objects[1]]
#     track_direction = math.degrees(math.atan2(next_waypoint[1] - waypoints[closest_objects[0]][1], next_waypoint[0] - waypoints[closest_objects[0]][0]))
#     direction_diff = abs(track_direction - heading)
#     reward -= direction_diff / 180
    
#     return float(reward)


def get_track_configuration():
    # Display options for track surfaces
    print("Choose your track surface from the following options:")
    print("1. Hardwood")
    print("2. Carpet")
    print("3. Concrete")
    print("4. Asphalt")
    print("5. Interlocked Foam")
    print("6. Rubber Pads")
    surface_choice = input("Enter the number corresponding to your choice: ")

    # Display options for tape types
    print("\nChoose your tape type:")
    print("1. Duct Tape (Pearl White, 1.88 inches wide)")
    print("2. Masking Tape (Less Sticky, 1.88 inches wide)")
    tape_choice = input("Enter the number corresponding to your choice: ")

    # Map surface choices to their names
    surfaces = {
        '1': 'Hardwood',
        '2': 'Carpet',
        '3': 'Concrete',
        '4': 'Asphalt',
        '5': 'Interlocked Foam',
        '6': 'Rubber Pads'
    }

    # Map tape choices to their names
    tapes = {
        '1': 'Duct Tape (Pearl White, 1.88 inches wide)',
        '2': 'Masking Tape (Less Sticky, 1.88 inches wide)'
    }

    # Retrieve the selected surface and tape
    surface = surfaces.get(surface_choice, 'Unknown Surface')
    tape = tapes.get(tape_choice, 'Unknown Tape')

    # Print the selected configuration
    print("\nTrack Configuration:")
    print(f"Track Surface: {surface}")
    print(f"Track Borders: {tape}")

# Run the configuration function
get_track_configuration()
