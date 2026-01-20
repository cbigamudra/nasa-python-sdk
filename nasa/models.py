from dataclasses import dataclass

@dataclass
class ApodImage:
    """Astronomy Picture of the Day Model"""
    date: str
    title: str
    url: str
    explanation: str

@dataclass
class Asteroid:
    """Near Earth Object Model"""
    id: str
    name: str
    diameter_km_max: float
    is_hazardous: bool