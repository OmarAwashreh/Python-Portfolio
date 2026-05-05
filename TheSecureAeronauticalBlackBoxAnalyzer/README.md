# ✈️ The Secure Aeronautical Black Box Analyzer

A command-line Python application designed to process and analyze immutable flight telemetry data. It parses flight logs to extract critical metrics like altitude, speed, and coordinates, and calculates telemetry changes between radar pings.

## ✨ Technologies

- `Python 3`

## 🚀 Features

- Analyzes immutable flight data using Python tuples for data integrity
- Calculates altitude differentials between sequential radar pings
- Scans logs to identify and extract maximum flight speeds and their exact timestamps
- Utilizes advanced sequence operations including tuple unpacking, slicing, and concatenation
 
## 📍 The Process

I've been diving into Python data structures, specifically focusing on how to handle immutable sequences. A "Black Box" flight data analyzer was the perfect way to practice! Since actual flight logs shouldn't be altered after they're recorded, using Python `tuples` instead of lists was the safest approach. I started by structuring the data points (timestamps, coordinates, altitude, and speed), then built loops to extract high-altitude flights and pinpoint the maximum speed. Figuring out how to "correct" an immutable log using tuple slicing and concatenation was a great challenge. It's a terminal-based script, but it really solidified my understanding of data integrity and sequence unpacking!

## 🚦 Running the Project

1. Clone the repository or download `TheSecureAeronauticalBlackBoxAnalyzer.py`
2. Ensure you have Python 3 installed on your system
3. Open your terminal and navigate to the project directory
4. Run the script: `python TheSecureAeronauticalBlackBoxAnalyzer.py`

## 🎞️ Preview

```
-----The Secure Aeronautical Black Box Analyzer-----

--- Flight Telemetry ---
At 2026-04-25T10:00:00Z, the aircraft was at 12000 ft traveling 450 knots.
At 2026-04-25T10:05:00Z, the aircraft was at 14500 ft traveling 470 knots.
At 2026-04-25T10:10:00Z, the aircraft was at 30000 ft traveling 520 knots.
At 2026-04-25T10:15:00Z, the aircraft was at 34000 ft traveling 540 knots.
At 2026-04-25T10:20:00Z, the aircraft was at 36000 ft traveling 560 knots.
At 2026-04-25T10:25:00Z, the aircraft was at 35000 ft traveling 550 knots.

Max speed recorded: 560 knots at 2026-04-25T10:20:00Z.

--- Altitude Changes ---
Altitude change from ping 1 to 2: 2500 ft
Altitude change from ping 2 to 3: 15500 ft
Altitude change from ping 3 to 4: 4000 ft
Altitude change from ping 4 to 5: 2000 ft
Altitude change from ping 5 to 6: -1000 ft

Timestamp '2026-04-25T10:10:00Z' present in log? True

Master log successfully merged. Total pings: 8
```
