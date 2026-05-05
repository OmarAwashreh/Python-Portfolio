print("-----The Secure Aeronautical Black Box Analyzer-----")

flight_log = (("2026-04-25T10:00:00Z", 51.4700, -0.4543, 12000, 450),
              ("2026-04-25T10:05:00Z", 52.2053, -0.1195, 14500, 470),
              ("2026-04-25T10:10:00Z", 53.3498, -2.2724, 30000, 520), 
              ("2026-04-25T10:15:00Z", 54.5973, -5.9301, 34000, 540),
              ("2026-04-25T10:20:00Z", 55.9533, -3.1883, 36000, 560),
              ("2026-04-25T10:25:00Z", 57.1497, -2.0943, 35000, 550))

for log in flight_log:
    print(f"At {log[0]}, the aircraft was " \
            f"at {log[3]} ft traveling {log[4]} knots.")

middle_log = flight_log[1:5]
    
(takeoff, *cruising, landing) = (flight_log[0], flight_log[1:5], flight_log[5])

high_flight = ()
for log in flight_log:
    if log[3] > 10000:
        high_flight += (log, )

def highest_flight(flight_log):
    max_speed = 0
    timestamp = "null"

    for log in flight_log:
        if log[4] > max_speed:
            max_speed = log[4]
            timestamp = log[0]
            highest_plane = log
    
    highest_plane = (max_speed, timestamp)
    
    return highest_plane

(max_speed, timestamp) = highest_flight(flight_log)

corrected_flight_log = flight_log[4][0:3] + (35000,) + flight_log[4][4:]

for i in range(len(flight_log), 0, -1):
    if i < len(flight_log):
        change = flight_log[i][3] - flight_log[i - 1][3]
        print(f"Change between ping {i} and ping {i-1} is {change}")
    else:
        continue