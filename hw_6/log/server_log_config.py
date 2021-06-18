import logging
import logging.handlers

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger('server')

formatter = logging.Formatter('%(asctime)-30s %(levelname)-10s %(name)s  %(message)s')

time_hand = logging.handlers.TimedRotatingFileHandler('server.log', when='midnight')
time_hand.setLevel(logging.INFO)
time_hand.setFormatter(formatter)

logger.addHandler(time_hand)

logger.propagate = False
