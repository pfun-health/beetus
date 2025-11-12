# #
# generate.py : generate various dynamics, procedures by using the BeetusClient (pfun-cma-model)
# #

from typing import Literal
from dataclasses import dataclass

from beetus.client import BeetusClient
from pfun_cma_model.engine.cma_model_params import CMAModelParams


class PFunGenerator:
    """Generates various dynamics, procedures by using the BeetusClient (pfun-cma-model)."""

    def __init__(self, model_params: CMAModelParams = None):
        self.model_params = model_params if model_params is not None else CMAModelParams()

    async def query_pfun(self):
        with BeetusClient() as client:
            try:
                api_response = await client.run_at_time_route_model_run_at_time_post(
                    t0=0,
                    t1=24,
                    n=100,
                    params=self.model_params
                )
                return api_response
            except Exception as e:
                print(f"Error calling API: {e}")

    async def generate(self):
        # implement for subclasses
        pass


@dataclass
class PlatformParams:
    """Parameters for generating a platform."""
    signal: Literal["c", "m", "a", "G"] = "c"
    width: float = 100.0
    height: float = 100.0
    x_offset: float = 0.0
    y_offset: float = 0.0


class PFunPlatformGenerator(PFunGenerator):
    def __init__(self, model_params: CMAModelParams = None, platform_params: PlatformParams = None):
        super().__init__(model_params)
        self.platform_pieces = []
        self.platform_params = platform_params if platform_params is not None else PlatformParams()

    async def generate_platform(self):
        """Generates a platform based on the PFun API response."""
        api_response = await self.query_pfun()
        # Process the API response to generate the platform
        if hasattr(api_response, self.platform_params.signal) and hasattr(api_response, "t"):
            for i in range(len(api_response.t)):
                x = (api_response.t[i] * self.platform_params.width) + self.platform_params.x_offset
                y = self.platform_params.y_offset - (api_response.c[i] * self.platform_params.height)
                self.platform_pieces.append(MovingPlatform(x, y))

    async def generate(self):
        """Generates a platform based on the PFun API response."""
        await self.generate_platform()

    @property
    def bbox(self):
        """Returns the bounding box of the generated platform."""
        if not self.platform_pieces:
            return None
        min_x = min(piece.x for piece in self.platform_pieces)
        max_x = max(piece.x + piece.width for piece in self.platform_pieces)
        min_y = min(piece.y for piece in self.platform_pieces)
        max_y = max(piece.y + piece.height for piece in self.platform_pieces)
        return (min_x, min_y, max_x, max_y)


class PFunWaveGenerator(PFunGenerator):
    def __init__(self, model_params: CMAModelParams = None, wave_params: WaveParams = None):
        super().__init__(model_params)
        self.wave_pieces = []
        self.wave_params = wave_params if wave_params is not None else WaveParams()

    async def generate_wave(self):
        """Generates a wave based on the PFun API response."""
        api_response = await self.query_pfun()
        # Process the API response to generate the wave
        if hasattr(api_response, self.wave_params.signal) and hasattr(api_response, "t"):
            for i in range(len(api_response.t)):
                x = (api_response.t[i] * self.wave_params.width) + self.wave_params.x_offset
                y = self.wave_params.y_offset - (api_response.c[i] * self.wave_params.height)
                self.wave_pieces.append(MovingWave(x, y))

    async def generate(self):
        """Generates a wave based on the PFun API response."""
        await self.generate_wave()

    @property
    def bbox(self):
        """Returns the bounding box of the generated wave."""
        if not self.wave_pieces:
            return None
        min_x = min(piece.x for piece in self.wave_pieces)
        max_x = max(piece.x + piece.width for piece in self.wave_pieces)
        min_y = min(piece.y for piece in self.wave_pieces)
        max_y = max(piece.y + piece.height for piece in self.wave_pieces)
        return (min_x, min_y, max_x, max_y)
