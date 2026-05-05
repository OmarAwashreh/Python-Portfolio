print("-----The Secure Aeronautical Black Box Analyzer-----\n")

# 1. The Core Ledger (Immutable Tuple of Tuples)
flight_log = (
    ("2026-04-25T10:00:00Z", 51.4700, -0.4543, 12000, 450),
    ("2026-04-25T10:05:00Z", 52.2053, -0.1195, 14500, 470),
    ("2026-04-25T10:10:00Z", 53.3498, -2.2724, 30000, 520), 
    ("2026-04-25T10:15:00Z", 54.5973, -5.9301, 34000, 540),
    ("2026-04-25T10:20:00Z", 55.9533, -3.1883, 36000, 560),
    ("2026-04-25T10:25:00Z", 57.1497, -2.0943, 35000, 550)
)

# 2. The Formatted Readout (Tuple Unpacking)
print("--- Flight Telemetry ---")
for log in flight_log:
    timestamp, lat, lon, alt, speed = log 
    print(f"At {timestamp}, the aircraft was at {alt} ft traveling {speed} knots.")

# 3. The Audit Slice (Starts at second record, ends at second-to-last)
middle_log = flight_log[1:-1] 

# 4. Advanced Unpacking (The Terminal Extract)
# The * operator automatically scoops up all middle elements into a list
takeoff, *cruising, landing = flight_log

# 5. The Altitude Filter
high_flight = ()
for log in flight_log:
    if log[3] > 10000:
        high_flight += (log,)

# 6. Multi-Value Return
def get_highest_speed(log_data):
    max_speed = 0
    max_timestamp = ""
    for ping in log_data:
        if ping[4] > max_speed:
            max_speed = ping[4]
            max_timestamp = ping[0]
    # Returning a tuple automatically
    return max_speed, max_timestamp

# Unpacking the returned tuple
highest_speed, speed_time = get_highest_speed(flight_log)
print(f"\nMax speed recorded: {highest_speed} knots at {speed_time}.")

# 7. The Immutability Workaround (The Sensor Correction)
# We discover ping #4 (index 3) needs an altitude correction to 35000
corrupted_ping = flight_log[3]
# Rebuild the single ping:
corrected_ping = corrupted_ping[:3] + (35000,) + corrupted_ping[4:]
# Rebuild the entire flight log by sandwiching the corrected ping in the middle:
corrected_flight_log = flight_log[:3] + (corrected_ping,) + flight_log[4:]

# 8. Delta Calculation
print("\n--- Altitude Changes ---")
for i in range(1, len(flight_log)):
    change = flight_log[i][3] - flight_log[i - 1][3]
    print(f"Altitude change from ping {i} to {i+1}: {change} ft")

# 9. Membership Testing
def check_timestamp(timestamp, log_data):
    for ping in log_data:
        if ping[0] == timestamp:
            return True
    return False

is_present = check_timestamp("2026-04-25T10:10:00Z", flight_log)
print(f"\nTimestamp '2026-04-25T10:10:00Z' present in log? {is_present}")

# 10. The Merger
connecting_flight = (
    ("2026-04-25T10:30:00Z", 58.3019, -0.7567, 33000, 540),
    ("2026-04-25T10:35:00Z", 59.9139, 10.7522, 31000, 520)
)
# Merging outer tuples directly joins the contents
master_log = flight_log + connecting_flight
print(f"\nMaster log successfully merged. Total pings: {len(master_log)}")