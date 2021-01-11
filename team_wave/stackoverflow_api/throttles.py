from rest_framework.throttling import AnonRateThrottle,UserRateThrottle


class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'