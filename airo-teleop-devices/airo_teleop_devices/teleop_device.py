import numpy as np
import numpy.typing as npt
from abc import ABC, abstractmethod


class TeleopDevice(ABC):
    @abstractmethod
    def get_raw_state(self) -> npt.NDArray[np.float64]:
        pass
