from dataclasses import dataclass
from typing import Tuple, Union

import colorio


def hex_to_rgb255(hex_: str) -> Tuple[int, int, int]:
    return tuple(int(hex_.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))


def rgb255_to_hex(r: Union[int, float], g: Union[int, float], b: Union[int, float]) -> str:
    return f"#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}"


@dataclass
class Paint:
    brand: str
    name: str
    hex: str = None
    rgb: Tuple[int, int, int] = None

    def __post_init__(self):
        if self.hex is None and self.rgb is None:
            raise ValueError("Need to provide RGB or HEX")

        if self.rgb is not None and self.hex is None:
            self.hex = rgb255_to_hex(*self.rgb)

        if self.hex is not None and self.rgb is None:
            self.rgb = hex_to_rgb255(self.hex)

        self.lab = colorio.cs.CIELAB().from_rgb255(self.rgb)

    def lrv(self) -> float:
        return colorio.cs.XYZ100().from_rgb255(self.rgb)[1]
