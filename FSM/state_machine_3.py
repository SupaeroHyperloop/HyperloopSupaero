# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:50:13 2023

@authors: Elena & Miguel
"""

#This is the first version of hand-written code, it has some indentation problems that were messing with Elena & I (Miguel)
'''
import queue
import sys, os
import threading

class StateMachine:
	# Implementation of the state machine StateMachine.
    class State:
		# State Enum 
        (
			main_init,
			main_launch, 
			main_estop,
			main_prearm,
			main_arm,
			main_push,
			main_coast,
			main_braking,
			main_shutdown,
			null_state
		) = range(10)
	
	
    def __init__(self):
		# Declares all necessary variables including list of states, histories etc. 
        self.brakes_closed = None
        self.pushing = None
        self.velocity = None
        self.distance = None
        self.levitation_distance = None     #added
        self.prearm = None
        self.launch = None
        self.estop_button = None

        #Breaks
        self.brakes_closed = None
		self.open_breaks_work = None
		self.close_breaks_work = None

		#GUI 
		self.GUI_prearm = False
		self.GUI_arm = False 
		self.GUI_launch = False 
		self.GUI_estop = False 
		self.GUI_shutdown = False; 

		
		self.in_event_queue = queue.Queue()
		# enumeration of all states:
		self.__State = StateMachine.State
		self.__state_conf_vector_changed = None
		self.__state_vector = self.State.null_state
		
		# for timed statechart:
		self.timer_service = None
		self.__time_events = [None] * 7
		
		# initializations:
		self.brakes_closed = True
		self.pushing = False
		self.velocity = 0
		self.distance = 0
        self.levitation_distance = 0     #added
		self.__is_executing = False
	
    def is_active(self):
		"""Checks if the state machine is active.
		"""
		return self.__state_vector is not self.__State.null_state
			
    def low_power_circuit_active (self):
		# Read heartbeats from all low power circuit compnents 
		# GPIO pins -- figure out later 
		return True
	
    def test_breaks(self):
		# Resting position is closed 

		# Open, check that it opened and then release and check that it was released 
		# - Send signal to open 
		# - Read pressure sensors 
		# - if open -> self.open_breaks_work = True 
		# - Release 
		#  - Read pressure sensors 
		# - if closed ->  self.close_breaks_work = True 

		return  self.open_breaks_work and self.close_breaks_work 

    def read_GUI(self): 
		#Read from GUI and fill all self.GUI ..... 
		# self.GUI_prearm = False
		# self.GUI_arm = False 
		# self.GUI_launch = False 
		# self.GUI_estop = False 
		# self.GUI_shutdown = False; 
		return 0 

    def electro_magnetic_relays_open(self):
        #Ensure electromagnetic relays are open, current function is a placeholder
        return True 
    
    def activate_propulsion(self):
        #Send order for motor to start working, activate motor and break control
        self.pushing = True
        return True
    
    def turnOff_propulsion(self):
        #Turn off propulsion 
        self.pushing = False
        return True
    
    def activate_state_estimator(self):
        #At minimum, activates IMU and sensor readings
        #Could also be in charge of updating sensor values after launch 
        # or another function could be written, whatever is more efficient
        return True
    
    def allow_Manual_Service_Disconnect(self):
        #This must turn off the pod yet also block the brakes open to be able to remove it
        return True
	
	def init_timer_callback(self): 
		self.transition_ESTOP()
	
	def transition_ESTOP(self): 
		self.brakes_closed = True; 
		self.__state_vector = self.State.main_estop 
		#SHUTDOWN 

	def run_cycle(self):
		"""Implementation of run_cycle function.
		"""
		self.__is_executing = True 

		while True: 

			#Potentially read GUI here to detect stop stuff 
			self.read_GUI()

			if self.__state_vector == self.State.main_init: 

				if self.breaks_work and self.powercircuit_active and self.telemetry_active : #Some things are missing

					if self.GUI_prearm : 
						self.brakes_closed = False; 
						self.__state_vector = self.State.main_prearm


				else : 
					if (init_timer_defined == False ):
						init_timer = threading.Timer(30,self.init_timer_callback()) #When the timer is over timer_callback will set init_timer_over = True
						init_timer.start() 
						init_timer.join()
						init_timer_defined = True
								#Test breaks 
					if not self.breaks_work : 
							self.breaks_work = self.test_breaks()
					if not self.powercircuit_active :
							self.powercircuit_active = self.low_power_circuit_active()
					if not self.telemetry_active:
							self.telemetry_active = self.is_telemetry_active() 
			
			if self.__state_vector == self.State.main_prearm:
				#The breaks are now open and the pod can be moved on the track, once it is placed, the operator will 
				# press the ARM button on the GUI and the transition will be made. 
				if self.GUI_arm: 
					#In the transiton we will have to activate the navigation 
					self.activate_state_estimator()
					self.__state_vector = self.State.main_arm
			
			if self.__state_vector == self.State.main_arm: 
                
                #Double-check connections to sensors, but make sure self.powercircuit_active changes with physical sys and not virtual
                if self.powercircuit_active and self.electromagnetic_relays_open:
					if self.GUI_launch: 
                        self.activate_propulsion()
						self.__state_vector = self.State.main_launch
                        
                else:
                    if (init_timer_defined == False ):
						init_timer = threading.Timer(30,self.init_timer_callback()) #When the timer is over timer_callback will set init_timer_over = True
						init_timer.start() 
						init_timer.join()
						init_timer_defined = True
                        
                    if not self.powercircuit_active:            
                        self.powercircuit_active = self.low_power_circuit_active()
                        
                    if not self.electromagnetic_relays_open:            
                        self.electromagnetic_relays_open = self.electro_magnetic_relays_open()
                        
			if self.__state_vector == self.State.main_launch:
				#self.get_IMU_readings() if activate_propulsion() doesn't finally activate AND update
                if self.velocity > 1: #1 is placeholder for minimum threshold velocity in 30 seconds
                    #make sure that control has full freedom to do its job from now on
    				self.__state_vector = self.State.main_pushing 
                        
                else:
                    if (init_timer_defined == False ):
						init_timer = threading.Timer(30,self.init_timer_callback()) #When the timer is over timer_callback will set init_timer_over = True
						init_timer.start() 
						init_timer.join()
						init_timer_defined = True
				
            if self.__state_vector == self.State.main_pushing:
                #5 m/s is current best estimation for the min. elcectrom. levitation vel.
                #0.02 m is current best estimation for min. functional vert. levit. dist.
                if (self.velocity >= 5) and (self.levitation_distance >= 0.02): 
                    self.__state_vector = self.State.main_coasting 
                    
            if self.__state_vector == self.State.main_coasting:
                #Assuming constraints cannot be reached before this point 
                # implement safety and mission limit values
                if (self.distance >= 40) or (self.velocity >= 15):
                    self.turnOff_propulsion()
                    self.brakes_closed = True
                    self.__state_vector = self.State.main_braking
                    
            if self.__state_vector == self.State.main_braking:
                if (self.velocity = 0) and (self.GUI_shutdown):
                    self.brakes_closed = True
                    self.allow_Manual_Service_Disconnect()
                    self.__state_vector = self.State.main_shutdown
                    
            if self.__state_vector == self.State.main_shutdown:
                print("mission success :) ")         
'''





#This is the new code, corrected by ChatGPT and including the following changes:
'''
	-Fixed Indentation Errors: Corrected inconsistent indentation levels throughout the code to ensure readability 
and proper execution.
	-Corrected init_timer_callback Syntax: Changed self.init_timer_callback() to self.init_timer_callback when passing 
as a callback to threading.Timer.
	-Fixed Incorrect self.State References: Changed instances of self.State to self.__State where necessary.
	-Replaced = with ==: Corrected if (self.velocity = 0) to if (self.velocity == 0) in the main_braking state check 
for velocity.
'''

import queue
import sys, os
import threading

class StateMachine:
    # Implementation of the state machine StateMachine.
    class State:
        # State Enum 
        (
            main_init,
            main_launch, 
            main_estop,
            main_prearm,
            main_arm,
            main_push,
            main_coast,
            main_braking,
            main_shutdown,
            null_state
        ) = range(10)
    
    def __init__(self):
        # Declares all necessary variables including list of states, histories etc. 
        self.brakes_closed = None
        self.pushing = None
        self.velocity = None
        self.distance = None
        self.levitation_distance = None
        self.prearm = None
        self.launch = None
        self.estop_button = None

        # Breaks
        self.brakes_closed = None
        self.open_breaks_work = None
        self.close_breaks_work = None

        # GUI 
        self.GUI_prearm = False
        self.GUI_arm = False 
        self.GUI_launch = False 
        self.GUI_estop = False 
        self.GUI_shutdown = False 

        self.in_event_queue = queue.Queue()
        # Enumeration of all states:
        self.__State = StateMachine.State
        self.__state_conf_vector_changed = None
        self.__state_vector = self.__State.null_state
        
        # For timed statechart:
        self.timer_service = None
        self.__time_events = [None] * 7
        
        # Initializations:
        self.brakes_closed = True
        self.pushing = False
        self.velocity = 0
        self.distance = 0
        self.levitation_distance = 0
        self.__is_executing = False
    
    def is_active(self):
        # Checks if the state machine is active.
        return self.__state_vector is not self.__State.null_state
            
    def low_power_circuit_active(self):
        # Read heartbeats from all low power circuit components 
        # GPIO pins -- figure out later 
        return True
    
    def test_breaks(self):
        # Resting position is closed 

        # Open, check that it opened and then release and check that it was released 
        # - Send signal to open 
        # - Read pressure sensors 
        # - if open -> self.open_breaks_work = True 
        # - Release 
        #  - Read pressure sensors 
        # - if closed ->  self.close_breaks_work = True 

        return self.open_breaks_work and self.close_breaks_work 

    def read_GUI(self): 
        # Read from GUI and fill all self.GUI ..... 
        # self.GUI_prearm = False
        # self.GUI_arm = False 
        # self.GUI_launch = False 
        # self.GUI_estop = False 
        # self.GUI_shutdown = False; 
        return 0 

    def electro_magnetic_relays_open(self):
        # Ensure electromagnetic relays are open, current function is a placeholder
        return True 
    
    def activate_propulsion(self):
        # Send order for motor to start working, activate motor and break control
        self.pushing = True
        return True
    
    def turnOff_propulsion(self):
        # Turn off propulsion 
        self.pushing = False
        return True
    
    def activate_state_estimator(self):
        # At minimum, activates IMU and sensor readings
        # Could also be in charge of updating sensor values after launch 
        # or another function could be written, whatever is more efficient
        return True
    
    def allow_Manual_Service_Disconnect(self):
        # This must turn off the pod yet also block the brakes open to be able to remove it
        return True
    
    def init_timer_callback(self): 
        self.transition_ESTOP()
    
    def transition_ESTOP(self): 
        self.brakes_closed = True 
        self.__state_vector = self.__State.main_estop 
        # SHUTDOWN 

    def run_cycle(self):
        # Implementation of run_cycle function.
        self.__is_executing = True 

        while True: 

            # Potentially read GUI here to detect stop stuff 
            self.read_GUI()

            if self.__state_vector == self.__State.main_init: 

                if self.breaks_work and self.powercircuit_active and self.telemetry_active:  # Some things are missing

                    if self.GUI_prearm: 
                        self.brakes_closed = False 
                        self.__state_vector = self.__State.main_prearm

                else: 
                    if not init_timer_defined:
                        init_timer = threading.Timer(30, self.init_timer_callback)  # Corrected callback syntax
                        init_timer.start() 
                        init_timer_defined = True
                    # Test breaks 
                    if not self.breaks_work: 
                        self.breaks_work = self.test_breaks()
                    if not self.powercircuit_active:
                        self.powercircuit_active = self.low_power_circuit_active()
                    if not self.telemetry_active:
                        self.telemetry_active = self.is_telemetry_active() 
            
            if self.__state_vector == self.__State.main_prearm:
                # The breaks are now open and the pod can be moved on the track. Once placed, the operator will 
                # press the ARM button on the GUI and the transition will be made. 
                if self.GUI_arm: 
                    # In the transition we will have to activate the navigation 
                    self.activate_state_estimator()
                    self.__state_vector = self.__State.main_arm
            
            if self.__state_vector == self.__State.main_arm: 
                
                # Double-check connections to sensors
                if self.powercircuit_active and self.electro_magnetic_relays_open():
                    if self.GUI_launch: 
                        self.activate_propulsion()
                        self.__state_vector = self.__State.main_launch
                        
                else:
                    if not init_timer_defined:
                        init_timer = threading.Timer(30, self.init_timer_callback)  # Corrected callback syntax
                        init_timer.start() 
                        init_timer_defined = True
                        
                    if not self.powercircuit_active:            
                        self.powercircuit_active = self.low_power_circuit_active()
                        
                    if not self.electro_magnetic_relays_open():            
                        self.electro_magnetic_relays_open = self.electro_magnetic_relays_open()
                        
            if self.__state_vector == self.__State.main_launch:
                #self.get_IMU_readings() if activate_propulsion() doesn't finally activate AND update
                if self.velocity > 1:  # Placeholder for minimum threshold velocity in 30 seconds
                    # Make sure that control has full freedom to do its job from now on
                    self.__state_vector = self.__State.main_push
                        
                else:
                    if not init_timer_defined:
                        init_timer = threading.Timer(30, self.init_timer_callback)  # Corrected callback syntax
                        init_timer.start()
                        init_timer_defined = True
                
            if self.__state_vector == self.__State.main_push:
                # 5 m/s is current best estimation for the min. electromagnetic levitation velocity.
                # 0.02 m is current best estimation for min. functional vertical levitation distance.
                if (self.velocity >= 5) and (self.levitation_distance >= 0.02): 
                    self.__state_vector = self.__State.main_coast 
                    
            if self.__state_vector == self.__State.main_coast:
                # Assuming constraints cannot be reached before this point 
                # Implement safety and mission limit values
                if (self.distance >= 40) or (self.velocity >= 15):
                    self.turnOff_propulsion()
                    self.brakes_closed = True
                    self.__state_vector = self.__State.main_braking
                    
            if self.__state_vector == self.__State.main_braking:
                if (self.velocity == 0) and self.GUI_shutdown:
                    self.brakes_closed = True
                    self.allow_Manual_Service_Disconnect()
                    self.__state_vector = self.__State.main_shutdown
                    
            if self.__state_vector == self.__State.main_shutdown:
                print("Mission success :)")