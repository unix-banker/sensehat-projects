            
from sense_hat import SenseHat
import csv
from time import sleep

sense = SenseHat()

header = ["ax", "ay", "az", "gx", "gy", "gz", "mx", "my", "mz", "gesture"]

def processingLoop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)

    while True:
        gesture = input("Enter the gesture (up/down/left/right) or type 'stop' to finish: ").lower()

        if gesture == 'stop':
            print("Stopping data collection.")
            break

        print(f"Perform {gesture} gesture. Get ready...")
        input("Press Enter when ready.")
        print(f"Collecting data for {gesture}...")

        count = 0
        while count < 30:
            a = sense.get_accelerometer_raw()
            g = sense.get_gyroscope_raw()
            m = sense.get_compass_raw()

            csv_writer.writerow([
                a['x'], a['y'], a['z'],
                g['x'], g['y'], g['z'],
                m['x'], m['y'], m['z'],
                gesture
            ])
            
            csvfile.flush()
            sleep(0.1)
            count += 1

        print(f"Data for {gesture} collected.")

with open("results.csv", "w", newline='') as csvfile:
    processingLoop(csvfile)