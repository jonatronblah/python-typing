from attrs import define


@define
class Coordinates:
    x: int
    y: int

co = Coordinates(x="five", y=6)