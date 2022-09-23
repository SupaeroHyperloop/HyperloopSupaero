# HyperloopSupaero

![HYPERLOOP](https://user-images.githubusercontent.com/97123368/157680947-9e6c7dbe-bec0-49dc-a396-6c6e3fa803e2.png)

As the first French Hyperloop technology development team based at the Institut Supérieur de l’Aéronautique et de l’Espace in Toulouse, our main goal is to design and improve the current technology and infrastructure needed to implement a Hyperloop prototype, the transport of tomorrow.

# GUI  and Control Commands

The software will be used to build a robust graphical user interface (GUI) for the purpose of visualising the critical components of the pod’s operation. This section focuses on a general software infrastructure on which to base the Hyperloop Supaero design.

The software core sets out to fulfill the following requirements:
  
**Lightweight Communications and Marshalling (LCM)**
  * Ensure to effectively read and process information from the various sensors on-board the pod.
  * Messages must be passed to Master Controller which passes commands through a CAN bus configuration.
 
 # Hardware
 **Controllers on-board the Hyperloop pod**
 * **Navigation Controller**:
    Performs the position estimation calculations and data processing. This gives the vehicle controller the information needed to perform the control actions. 
  * **Vehicle controller**:
    Main flight controller of the pod. It triggers emergency modes and constantly monitors motor performance. It commands all actuators on the pod.
  * **Power unit**:
    Keeps a check on the health of the battery packs through the Battery Management System (BMS) and sensors for temperature, current and voltage. 

 **Sensors on-board the Hyperloop pod**
 * Front Sensor Hub
    - IMU accelerometer
    - Friction brakes temperature
    - Front-wheel temperature
    - Photoelectric distance sensors
    - MEMS-based 360 tilt sensor
    - Front friction piston solenoid temperature

 * Central Sensor Hub
    - IMU accelerometer
    - Liquid cooling pressure
    - Battery current
    - Battery temperature
    - EC-brakes temperature
    - Liquid cooling temperature IN and OUT

  * Rear sensor Hub
    - IMU accelerometer
    - Rear-wheel temperature
    - Photoelectric distance sensors
    - Friction-drive motor temperature
    - Rear friction solenoid temperature

  
