# Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design. You will be given a simplistic version of an FSM to code for a basic TCP session.

# The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.

# The input array of events will consist of one or more of the following strings:

# APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
# The states are as follows and should be returned in all capital letters as shown:

# CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
# The input will be an array of events. Your job is to traverse the FSM as determined by the events, and return the proper state as a string, all caps, as shown above.

# If an event is not applicable to the current state, your code will return "ERROR".

# Action of each event upon each state:
# (the format is INITIAL_STATE: EVENT -> NEW_STATE)

# CLOSED: APP_PASSIVE_OPEN -> LISTEN
# CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
# LISTEN: RCV_SYN          -> SYN_RCVD
# LISTEN: APP_SEND         -> SYN_SENT
# LISTEN: APP_CLOSE        -> CLOSED
# SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
# SYN_RCVD: RCV_ACK        -> ESTABLISHED
# SYN_SENT: RCV_SYN        -> SYN_RCVD
# SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
# SYN_SENT: APP_CLOSE      -> CLOSED
# ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
# ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
# FIN_WAIT_1: RCV_FIN      -> CLOSING
# FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
# FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
# CLOSING: RCV_ACK         -> TIME_WAIT
# FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
# TIME_WAIT: APP_TIMEOUT   -> CLOSED
# CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
# LAST_ACK: RCV_ACK        -> CLOSED
# "EFSM TCP"

# Examples
# ["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"] =>  "ESTABLISHED"

# ["APP_ACTIVE_OPEN"] =>  "SYN_SENT"

# ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"] =>  "ERROR"


class WrongType(Exception):
    pass

# Solution one
def traverse_TCP_states(events):
    state = 'CLOSED'

    for event in events:
        if state == 'CLOSED':
            if event == 'APP_PASSIVE_OPEN':
                state = 'LISTEN'
            elif event == 'APP_ACTIVE_OPEN':
                state = 'SYN_SENT'
            else:
                return 'ERROR'
        elif state == 'LISTEN':
            if event == 'RCV_SYN':
                state = 'SYN_RCVD'
            elif event == 'APP_SEND':
                state = 'SYN_SENT'
            elif event == 'APP_CLOSE':
                state = 'CLOSED'
            else:
                return 'ERROR'
        elif state == 'SYN_RCVD':
            if event == 'APP_CLOSE':
                state = 'FIN_WAIT_1'
            elif event == 'RCV_ACK':
                state = 'ESTABLISHED'
            else:
                return 'ERROR'
        elif state == 'SYN_SENT':
            if event == 'RCV_SYN':
                state = 'SYN_RCVD'
            elif event == 'RCV_SYN_ACK':
                state = 'ESTABLISHED'
            elif event == 'APP_CLOSE':
                state = 'CLOSED'
            else:
                return 'ERROR'
        elif state == 'ESTABLISHED':
            if event == 'APP_CLOSE':
                state = 'FIN_WAIT_1'
            elif event == 'RCV_FIN':
                state = 'CLOSE_WAIT'
            elif event not in ['APP_SEND', 'RCV_ACK', 'RCV_FIN_ACK']:
                return 'ERROR'
        elif state == 'FIN_WAIT_1':
            if event == 'RCV_FIN':
                state = 'CLOSING'
            elif event == 'RCV_FIN_ACK':
                state = 'TIME_WAIT'
            elif event == 'RCV_ACK':
                state = 'FIN_WAIT_2'
            else:
                return 'ERROR'
        elif state == 'CLOSING':
            if event == 'RCV_ACK':
                state = 'TIME_WAIT'
            else:
                return 'ERROR'
        elif state == 'FIN_WAIT_2':
            if event == 'RCV_FIN':
                state = 'TIME_WAIT'
            elif event == 'RCV_ACK':
                state = 'ESTABLISHED'
            else:
                return 'ERROR'
        elif state == 'TIME_WAIT':
            if event == 'APP_TIMEOUT':
                state = 'CLOSED'
            else:
                return 'ERROR'
        elif state == 'CLOSE_WAIT':
            if event == 'APP_CLOSE':
                state = 'LAST_ACK'
            else:
                return 'ERROR'
        elif state == 'LAST_ACK':
            if event == 'RCV_ACK':
                state = 'CLOSED'
            else:
                return 'ERROR'
        else:
            return 'ERROR'

    return state.upper()


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('fib(1000)')

    start_time = time.time()
    fib(1000)
    print(fib(1000))
    end_time = time.time()

    print('', end_time - start_time)
