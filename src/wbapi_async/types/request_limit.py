from .base import BaseType


class RequestLimit(BaseType):
    period: int
    """The time interval during which the maximum number of requests
    according to the limit can be sent."""

    limit: int
    """The maximum number of requests per period."""

    interval: int
    """The time gap for pauses between requests. """

    burst: int
    """The maximum number of requests that can be sent simultaneously, without interval pauses."""
