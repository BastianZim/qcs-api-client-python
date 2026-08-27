from enum import Enum


class QuantumProcessorAccessorType(str, Enum):
    DIRECT_V1 = "direct.v1"
    GATEWAY_V1 = "gateway.v1"

    def __str__(self) -> str:
        return str(self.value)
