# pieces.py : contains classes for different types of platform and wave pieces
from dataclasses import dataclass
from typing import List, Mapping

@dataclass
class Piece:
    """Represents a generic piece."""
    x: float
    y: float
    width: float = 10.0
    height: float = 10.0


@dataclass
class MovingPlatform(Piece):
    """Represents a moving platform piece."""
    dx: float = 0.0
    dy: float = 0.0


@dataclass
class MovingWave(MovingPlatform):
    """Represents a moving wave piece."""
    #: time vector
    tvec: List[float] = None
    #: signal vector
    svec: List[float] = None
    #: parameter vector
    pvec: Mapping[str, float] = None
