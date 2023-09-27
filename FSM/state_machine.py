import queue
import sys, os

class StateMachine:
	"""Implementation of the state machine StateMachine.
	"""

	class State:
		""" State Enum
		"""
		(
			main_estop,
			main_prearm,
			main_arm,
			main_push,
			main_coast,
			main_braking,
			main_shutdown,
			main_stopping,
			null_state
		) = range(9)
	
	
	def __init__(self):
		""" Declares all necessary variables including list of states, histories etc. 
		"""
		
		self.brakes_closed = None
		self.pushing = None
		self.velocity = None
		self.distance = None
		self.prearm = None
		self.launch = None
		self.estop_button = None
		
		self.in_event_queue = queue.Queue()
		# enumeration of all states:
		self.__State = StateMachine.State
		self.__state_conf_vector_changed = None
		self.__state_vector = [None] * 1
		for __state_index in range(1):
			self.__state_vector[__state_index] = self.State.null_state
		
		# for timed statechart:
		self.timer_service = None
		self.__time_events = [None] * 7
		
		# initializations:
		self.brakes_closed = 1
		self.pushing = 0
		self.velocity = 0
		self.distance = 0
		self.__is_executing = False
	
	def is_active(self):
		"""Checks if the state machine is active.
		"""
		return self.__state_vector[0] is not self.__State.null_state
	
	def is_final(self):
		"""Checks if the statemachine is final.
		Always returns 'false' since this state machine can never become final.
		"""
		return False
			
	def is_state_active(self, state):
		"""Checks if the state is currently active.
		"""
		s = state
		if s == self.__State.main_estop:
			return self.__state_vector[0] == self.__State.main_estop
		if s == self.__State.main_prearm:
			return self.__state_vector[0] == self.__State.main_prearm
		if s == self.__State.main_arm:
			return self.__state_vector[0] == self.__State.main_arm
		if s == self.__State.main_push:
			return self.__state_vector[0] == self.__State.main_push
		if s == self.__State.main_coast:
			return self.__state_vector[0] == self.__State.main_coast
		if s == self.__State.main_braking:
			return self.__state_vector[0] == self.__State.main_braking
		if s == self.__State.main_shutdown:
			return self.__state_vector[0] == self.__State.main_shutdown
		if s == self.__State.main_stopping:
			return self.__state_vector[0] == self.__State.main_stopping
		return False
		
	def time_elapsed(self, event_id):
		"""Add time events to in event queue
		"""
		if event_id in range(7):
			self.in_event_queue.put(lambda: self.raise_time_event(event_id))
			self.run_cycle()
	
	def raise_time_event(self, event_id):
		"""Raise timed events using the event_id.
		"""
		self.__time_events[event_id] = True
	
	def __execute_queued_event(self, func):
		func()
	
	def __get_next_event(self):
		if not self.in_event_queue.empty():
			return self.in_event_queue.get()
		return None
	
	def raise_prearm(self):
		"""Raise method for event prearm.
		"""
		self.in_event_queue.put(self.__raise_prearm_call)
		self.run_cycle()
	
	def __raise_prearm_call(self):
		"""Raise callback for event prearm.
		"""
		self.prearm = True
	
	def raise_launch(self):
		"""Raise method for event launch.
		"""
		self.in_event_queue.put(self.__raise_launch_call)
		self.run_cycle()
	
	def __raise_launch_call(self):
		"""Raise callback for event launch.
		"""
		self.launch = True
	
	def raise_estop_button(self):
		"""Raise method for event estop_button.
		"""
		self.in_event_queue.put(self.__raise_estop_button_call)
		self.run_cycle()
	
	def __raise_estop_button_call(self):
		"""Raise callback for event estop_button.
		"""
		self.estop_button = True
	
	def __entry_action_main_estop(self):
		"""Entry action for state 'ESTOP'..
		"""
		self.brakes_closed = 1
		
	def __entry_action_main_prearm(self):
		"""Entry action for state 'PREARM'..
		"""
		self.timer_service.set_timer(self, 0, (3 * 1000), False)
		self.brakes_closed = 0
		
	def __entry_action_main_push(self):
		"""Entry action for state 'PUSH'..
		"""
		self.timer_service.set_timer(self, 1, 1000, True)
		self.pushing = 1
		
	def __entry_action_main_coast(self):
		"""Entry action for state 'COAST'..
		"""
		self.timer_service.set_timer(self, 2, (4 * 1000), False)
		self.timer_service.set_timer(self, 3, 1000, True)
		self.pushing = 0
		
	def __entry_action_main_braking(self):
		"""Entry action for state 'BRAKING'..
		"""
		self.timer_service.set_timer(self, 4, 1000, True)
		self.brakes_closed = 1
		
	def __entry_action_main_shutdown(self):
		"""Entry action for state 'SHUTDOWN'..
		"""
		self.timer_service.set_timer(self, 5, (3 * 1000), False)
		
	def __entry_action_main_stopping(self):
		"""Entry action for state 'STOPPING'..
		"""
		self.timer_service.set_timer(self, 6, 1000, True)
		self.brakes_closed = 1
		
	def __exit_action_main_prearm(self):
		"""Exit action for state 'PREARM'..
		"""
		self.timer_service.unset_timer(self, 0)
		
	def __exit_action_main_push(self):
		"""Exit action for state 'PUSH'..
		"""
		self.timer_service.unset_timer(self, 1)
		
	def __exit_action_main_coast(self):
		"""Exit action for state 'COAST'..
		"""
		self.timer_service.unset_timer(self, 2)
		self.timer_service.unset_timer(self, 3)
		
	def __exit_action_main_braking(self):
		"""Exit action for state 'BRAKING'..
		"""
		self.timer_service.unset_timer(self, 4)
		
	def __exit_action_main_shutdown(self):
		"""Exit action for state 'SHUTDOWN'..
		"""
		self.timer_service.unset_timer(self, 5)
		
	def __exit_action_main_stopping(self):
		"""Exit action for state 'STOPPING'..
		"""
		self.timer_service.unset_timer(self, 6)
		
	def __enter_sequence_main_estop_default(self):
		"""'default' enter sequence for state ESTOP.
		"""
		self.__entry_action_main_estop()
		self.__state_vector[0] = self.State.main_estop
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_prearm_default(self):
		"""'default' enter sequence for state PREARM.
		"""
		self.__entry_action_main_prearm()
		self.__state_vector[0] = self.State.main_prearm
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_arm_default(self):
		"""'default' enter sequence for state ARM.
		"""
		self.__state_vector[0] = self.State.main_arm
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_push_default(self):
		"""'default' enter sequence for state PUSH.
		"""
		self.__entry_action_main_push()
		self.__state_vector[0] = self.State.main_push
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_coast_default(self):
		"""'default' enter sequence for state COAST.
		"""
		self.__entry_action_main_coast()
		self.__state_vector[0] = self.State.main_coast
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_braking_default(self):
		"""'default' enter sequence for state BRAKING.
		"""
		self.__entry_action_main_braking()
		self.__state_vector[0] = self.State.main_braking
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_shutdown_default(self):
		"""'default' enter sequence for state SHUTDOWN.
		"""
		self.__entry_action_main_shutdown()
		self.__state_vector[0] = self.State.main_shutdown
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_stopping_default(self):
		"""'default' enter sequence for state STOPPING.
		"""
		self.__entry_action_main_stopping()
		self.__state_vector[0] = self.State.main_stopping
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_default(self):
		"""'default' enter sequence for region main.
		"""
		self.__react_main__entry_default()
		
	def __exit_sequence_main_estop(self):
		"""Default exit sequence for state ESTOP.
		"""
		self.__state_vector[0] = self.State.null_state
		
	def __exit_sequence_main_prearm(self):
		"""Default exit sequence for state PREARM.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_prearm()
		
	def __exit_sequence_main_arm(self):
		"""Default exit sequence for state ARM.
		"""
		self.__state_vector[0] = self.State.null_state
		
	def __exit_sequence_main_push(self):
		"""Default exit sequence for state PUSH.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_push()
		
	def __exit_sequence_main_coast(self):
		"""Default exit sequence for state COAST.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_coast()
		
	def __exit_sequence_main_braking(self):
		"""Default exit sequence for state BRAKING.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_braking()
		
	def __exit_sequence_main_shutdown(self):
		"""Default exit sequence for state SHUTDOWN.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_shutdown()
		
	def __exit_sequence_main_stopping(self):
		"""Default exit sequence for state STOPPING.
		"""
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_stopping()
		
	def __exit_sequence_main(self):
		"""Default exit sequence for region main.
		"""
		state = self.__state_vector[0]
		if state == self.State.main_estop:
			self.__exit_sequence_main_estop()
		elif state == self.State.main_prearm:
			self.__exit_sequence_main_prearm()
		elif state == self.State.main_arm:
			self.__exit_sequence_main_arm()
		elif state == self.State.main_push:
			self.__exit_sequence_main_push()
		elif state == self.State.main_coast:
			self.__exit_sequence_main_coast()
		elif state == self.State.main_braking:
			self.__exit_sequence_main_braking()
		elif state == self.State.main_shutdown:
			self.__exit_sequence_main_shutdown()
		elif state == self.State.main_stopping:
			self.__exit_sequence_main_stopping()
		
	def __react_main__entry_default(self):
		"""Default react sequence for initial entry .
		"""
		self.__enter_sequence_main_estop_default()
		
	def __react(self, transitioned_before):
		"""Implementation of __react function.
		"""
		return transitioned_before
	
	
	def __main_estop_react(self, transitioned_before):
		"""Implementation of __main_estop_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.prearm:
				self.__exit_sequence_main_estop()
				self.__enter_sequence_main_prearm_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_prearm_react(self, transitioned_before):
		"""Implementation of __main_prearm_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.__time_events[0]:
				self.__exit_sequence_main_prearm()
				self.__time_events[0] = False
				self.__enter_sequence_main_arm_default()
				self.__react(0)
				transitioned_after = 0
			elif self.estop_button:
				self.__exit_sequence_main_prearm()
				self.__enter_sequence_main_stopping_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_arm_react(self, transitioned_before):
		"""Implementation of __main_arm_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.launch:
				self.__exit_sequence_main_arm()
				self.__enter_sequence_main_push_default()
				self.__react(0)
				transitioned_after = 0
			elif self.estop_button:
				self.__exit_sequence_main_arm()
				self.__enter_sequence_main_stopping_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_push_react(self, transitioned_before):
		"""Implementation of __main_push_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.velocity >= 22:
				self.__exit_sequence_main_push()
				self.__enter_sequence_main_coast_default()
				self.__react(0)
				transitioned_after = 0
			elif self.estop_button:
				self.__exit_sequence_main_push()
				self.__enter_sequence_main_stopping_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			if self.__time_events[1]:
				self.velocity = self.velocity + 4.2
				self.distance = self.distance + self.velocity
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_coast_react(self, transitioned_before):
		"""Implementation of __main_coast_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.__time_events[2]:
				self.__exit_sequence_main_coast()
				self.__time_events[2] = False
				self.__enter_sequence_main_braking_default()
				self.__react(0)
				transitioned_after = 0
			elif self.estop_button:
				self.__exit_sequence_main_coast()
				self.__enter_sequence_main_stopping_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			if self.__time_events[3]:
				self.velocity = self.velocity - 6.9
				self.distance = self.distance + self.velocity
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_braking_react(self, transitioned_before):
		"""Implementation of __main_braking_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.velocity <= 0:
				self.__exit_sequence_main_braking()
				self.__enter_sequence_main_shutdown_default()
				self.__react(0)
				transitioned_after = 0
			elif self.estop_button:
				self.__exit_sequence_main_braking()
				self.__enter_sequence_main_stopping_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			if self.__time_events[4]:
				self.velocity = self.velocity - 1
				self.distance = self.distance + self.velocity
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_shutdown_react(self, transitioned_before):
		"""Implementation of __main_shutdown_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.__time_events[5]:
				self.__exit_sequence_main_shutdown()
				self.__time_events[5] = False
				self.__enter_sequence_main_estop_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_stopping_react(self, transitioned_before):
		"""Implementation of __main_stopping_react function.
		"""
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.velocity <= 0:
				self.__exit_sequence_main_stopping()
				self.__enter_sequence_main_estop_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken then execute local reactions
		if transitioned_after == transitioned_before:
			if self.__time_events[6]:
				self.velocity = self.velocity - 2
				self.distance = self.distance + self.velocity
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __clear_in_events(self):
		"""Implementation of __clear_in_events function.
		"""
		self.prearm = False
		self.launch = False
		self.estop_button = False
		self.__time_events[0] = False
		self.__time_events[1] = False
		self.__time_events[2] = False
		self.__time_events[3] = False
		self.__time_events[4] = False
		self.__time_events[5] = False
		self.__time_events[6] = False
	
	
	def __micro_step(self):
		"""Implementation of __micro_step function.
		"""
		state = self.__state_vector[0]
		if state == self.State.main_estop:
			self.__main_estop_react(-1)
		elif state == self.State.main_prearm:
			self.__main_prearm_react(-1)
		elif state == self.State.main_arm:
			self.__main_arm_react(-1)
		elif state == self.State.main_push:
			self.__main_push_react(-1)
		elif state == self.State.main_coast:
			self.__main_coast_react(-1)
		elif state == self.State.main_braking:
			self.__main_braking_react(-1)
		elif state == self.State.main_shutdown:
			self.__main_shutdown_react(-1)
		elif state == self.State.main_stopping:
			self.__main_stopping_react(-1)
	
	
	def run_cycle(self):
		"""Implementation of run_cycle function.
		"""
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		next_event = self.__get_next_event()
		if next_event is not None:
			self.__execute_queued_event(next_event)
		condition_0 = True
		while condition_0:
			self.__micro_step()
			self.__clear_in_events()
			next_event = self.__get_next_event()
			if next_event is not None:
				self.__execute_queued_event(next_event)
			condition_0 = self.prearm or self.launch or self.estop_button or self.__time_events[0] or self.__time_events[1] or self.__time_events[2] or self.__time_events[3] or self.__time_events[4] or self.__time_events[5] or self.__time_events[6]
		self.__is_executing = False
	
	
	def enter(self):
		"""Implementation of enter function.
		"""
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		self.__enter_sequence_main_default()
		self.__is_executing = False
	
	
	def exit(self):
		"""Implementation of exit function.
		"""
		if self.__is_executing:
			return
		self.__is_executing = True
		self.__exit_sequence_main()
		self.__is_executing = False
	
	
	def trigger_without_event(self):
		"""Implementation of triggerWithoutEvent function.
		"""
		self.run_cycle()
	
