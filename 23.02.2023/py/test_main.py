import main


# First approach
def test_traverse_TCP_states():
    test_cases = (
        (['APP_ACTIVE_OPEN','RCV_SYN_ACK','RCV_FIN'], 'CLOSE_WAIT'),
        (['APP_PASSIVE_OPEN',  'RCV_SYN','RCV_ACK'], 'ESTABLISHED'),
        (['APP_ACTIVE_OPEN','RCV_SYN_ACK','RCV_FIN','APP_CLOSE'], 'LAST_ACK'),
        (['APP_ACTIVE_OPEN'], 'SYN_SENT'),
        (['APP_PASSIVE_OPEN','RCV_SYN','RCV_ACK','APP_CLOSE','APP_SEND']), 'ERROR')
    )

    for x, y in test_cases:
        # First approach
        assert main.traverse_TCP_states(x) == y
