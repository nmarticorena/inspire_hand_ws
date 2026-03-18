#!/usr/bin/env python3
from inspire_sdkpy import inspire_sdk_double, inspire_hand_defaut
import time

if __name__ == "__main__":

    ## publish All Data
    # states_structure = [
    #         ('pos_act', 1534, 6, 'short'),
    #         ('angle_act', 1546, 6, 'short'),
    #         ('force_act', 1582, 6, 'short'),
    #         ('current', 1594, 6, 'short'),
    #         ('err', 1606, 3, 'byte'),
    #         ('status', 1612, 3, 'byte'),
    #         ('temperature', 1618, 3, 'byte')
    #     ]

    ## Only publish this data to increase publishing frequency
    states_structure = [
            ('angle_act', 1546, 6, 'short'),
            # ('force_act', 1582, 6, 'short'),
            ('status', 1612, 3, 'byte'),
        ]

    handler = inspire_sdk_double.ModbusDataHandlerDouble(device_id=[2,1], use_serial=True, serial_port='/dev/ttyUSB0',states_structure=states_structure) # l r
    time.sleep(0.5)

    call_count = 0  # Record call count
    start_time = time.perf_counter()  # Record start time

    try:
        while True:
            data_dict = handler.read()  # Read data

            call_count += 1  # Increment call count
            time.sleep(0.001)  # Sleep 1 ms

            # Calculate and print call frequency periodically
            if call_count % 10 == 0:  # Calculate frequency every 10 calls
                elapsed_time = time.perf_counter() - start_time  # Calculate total elapsed time
                frequency = call_count / elapsed_time  # Calculate frequency (Hz)
                print(f"Current frequency: {frequency:.2f} Hz, Call count: {call_count}, Elapsed time: {elapsed_time:.6f} s")
    except KeyboardInterrupt:
        elapsed_time = time.perf_counter() - start_time  # Calculate total elapsed time
        frequency = call_count / elapsed_time if elapsed_time > 0 else 0  # Calculate final frequency
        print(f"Program ended. Total calls: {call_count}, Total elapsed time: {elapsed_time:.6f} s, Final frequency: {frequency:.2f} Hz")
