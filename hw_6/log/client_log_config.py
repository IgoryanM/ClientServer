import logging


logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger('client')

formatter = logging.Formatter('%(asctime)-10s %(levelname)-10s %(name)s  %(message)s')

file_hand = logging.FileHandler('client.log')
file_hand.setLevel(logging.INFO)
file_hand.setFormatter(formatter)

logger.addHandler(file_hand)

logger.propagate = False
