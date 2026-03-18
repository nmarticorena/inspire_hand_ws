
---

# Dexterous Hand SDK User Guide

## Environment Management

It is recommended to use `venv` for virtual environment management:

```bash
python -m venv venv # or extract venv_x86.tar.xz and place .venv in inspire_hand_ws/.venv

# Then run the following scripts to update the venv paths:
python update_venv_path.py .venv
python update_bin_files.py .venv 

source venv/bin/activate  # Linux/MacOS activate virtual environment
```

## Installing Dependencies

1. When setting up the environment manually, install the project dependencies; if you use Unzip venv_x86.tar.xz to set up the environment, you do not need to run the following commands:

    ```bash
    pip install -r requirements.txt
    ```

2. Update submodules:

    ```bash
    git submodule init  # Initialize submodules
    git submodule update  # Update submodules to the latest version
    ```

3. Install the two SDKs separately:

    ```bash
    cd unitree_sdk2_python
    pip install -e .

    cd ../inspire_hand_sdk
    pip install -e .
    ```
## Control Modes

The Inspire Hand SDK supports multiple control modes, defined as follows:

- **Mode 0**: `0000` (No operation)
- **Mode 1**: `0001` (Angle)
- **Mode 2**: `0010` (Position)
- **Mode 3**: `0011` (Angle + Position)
- **Mode 4**: `0100` (Force control)
- **Mode 5**: `0101` (Angle + Force control)
- **Mode 6**: `0110` (Position + Force control)
- **Mode 7**: `0111` (Angle + Position + Force control)
- **Mode 8**: `1000` (Velocity)
- **Mode 9**: `1001` (Angle + Velocity)
- **Mode 10**: `1010` (Position + Velocity)
- **Mode 11**: `1011` (Angle + Position + Velocity)
- **Mode 12**: `1100` (Force control + Velocity)
- **Mode 13**: `1101` (Angle + Force control + Velocity)
- **Mode 14**: `1110` (Position + Force control + Velocity)
- **Mode 15**: `1111` (Angle + Position + Force control + Velocity)
## Usage Examples

The following are descriptions of several common usage examples:

1. **DDS publish control commands**:

    Run the following script to publish control commands:
    ```bash
    python inspire_hand_sdk/example/dds_publish.py
    ```

2. **DDS subscribe to dexterous hand state and tactile sensor data, and visualize**:

    Run the following script to subscribe to the dexterous hand state and sensor data, and visualize the data:
    ```bash
    python inspire_hand_sdk/example/dds_subscribe.py
    ```

3. **Dexterous Hand DDS driver (headless mode)**:

    Use the following script for headless mode operation:
    ```bash
    python inspire_hand_sdk/example/Headless_driver.py
    ```

4. **Dexterous Hand configuration panel**:

    Run the following script to use the dexterous hand configuration panel:
    ```bash
    python inspire_hand_sdk/example/init_set_inspire_hand.py
    ```

5. **Dexterous Hand DDS driver (panel mode)**:

    Use the following script to enter panel mode and control the dexterous hand DDS driver:
    ```bash
    python inspire_hand_sdk/example/Vision_driver.py
    ```

---
