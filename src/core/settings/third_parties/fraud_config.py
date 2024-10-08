from core.env import env

RATE_LIMIT_PERIOD = env.int("FRAUD_DETECTION_RATE_LIMIT_PERIOD", default=3600)
MAX_RATES_PER_HOUR = env.int("FRAUD_DETECTION_MAX_RATES_PER_HOUR", default=500)
SUSPICIOUS_THRESHOLD = env.int("FRAUD_DETECTION_SUSPICIOUS_THRESHOLD", default=1000)
TIME_THRESHOLD = env.int("FRAUD_DETECTION_TIME_THRESHOLD", default=10)
LAST_ACTIONS_TO_TRACK = env.int("FRAUD_DETECTION_LAST_ACTIONS_TO_TRACK", default=100)
SUSPECTED_RATES_THRESHOLD = env.float("FRAUD_DETECTION_SUSPECTED_RATES_THRESHOLD", default=0.2)

