import time
import random
from prometheus_client import Summary , Counter, start_http_server


# define the metrics
REQUESTS_COUNTER = Counter(name="prediction_requests_total",
                  documentation="Total number of prediction requests")

RESPONSE_TIME_SUMMARY = Summary(name="prediction_request_duration_seconds",
                  documentation="Duration of prediction requests in seconds")


# start the prometheus server
start_http_server(8000)

@RESPONSE_TIME_SUMMARY.time()
def predict(delay):
    """Mock Prediction Function"""
    # increment the counter
    REQUESTS_COUNTER.inc()
    # give a random sentiment of text
    result_choice = random.choice(["positive", "negative", "neutral"])
    # simulate some prediction time
    time.sleep(delay)
    
    return {
        "sentiment": result_choice
    }
    