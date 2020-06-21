"""
Sample use simulating real-world processes with simpy
"""

import simpy
import random
import statistics

wait_times = []


class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1,3))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3/10)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1,5))