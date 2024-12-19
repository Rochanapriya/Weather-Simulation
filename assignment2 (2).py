import numpy as np 

class WeatherSimulation:
    def __init__ (self, transition_struct, holding_days):
        self.status = list(transition_struct.keys())
        self.current = 'sunny'
        self.transition_struct = transition_struct
        self.holding_days = holding_days
        self.days_left = holding_days['sunny']
        for state, struct in transition_struct.items():
            if not np.isclose(sum(struct.values()), 1.0):
                raise RuntimeError("The sum of transition_struct for state {state} is not equal to 1.")
    def get_states(self):
        return self.status
    def current_state(self):
        return self.current
    def next_state(self):
        if self.days_left > 0:
            self.days_left -= 1
        else:
            struct = self.transition_struct[self.current]
            self.current = np.random.choice(self.status, p = list(struct.values()))
            self.days_left = self.holding_days[self.current]
            self.days_left -= 1
    def set_state(self,new_state):
        if new_state not in self.status:
            raise ValueError("Invalid state name:{new_state}.")
        self.current = new_state
        self.days_left = self.holding_days[new_state]
    def current_state_remaining_hours(self):
        return self.days_left
    def iterable(self):
        while True:
            yield self.current
            self.next_state()
    def simulate(self, days):
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Days should be a positive non-zero integer.")
        state_ram = {state: 0 for state in self.status}
        for _ in range(days):
            self.next_state()
            state_ram[self.current] += 1
        state_per = [state_ram[state] * 100 / days for state in self.status]
        return state_per