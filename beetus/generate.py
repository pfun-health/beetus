# #
# generate.py : generate various dynamics, procedures by using the BeetusClient (pfun-cma-model)
# #

import asyncio
import logging
from typing import Dict, List, Optional
import json
from openapi_client.models.cma_model_params import CMAModelParams
from beetus.client import BeetusClient
from beetus.params import PlatformParams, WaveParams
from beetus.pieces import Piece, MovingPlatform, MovingWave

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PFunGenerator:
    """Generates various dynamics, procedures by using the BeetusClient (pfun-cma-model)."""

    def __init__(self, ndays: int = 1, model_params: Optional[CMAModelParams] = None):
        self._ndays = ndays
        self._day = 0
        self.model_params = model_params if model_params is not None else CMAModelParams()
        self._pieces: List[Piece] = []
        self._client: Optional[BeetusClient] = None

    @property
    def day(self) -> int:
        """Returns the current day."""
        return self._day

    @property
    def current_day(self) -> int:
        """Returns the current day."""
        return self._day

    def __iter__(self):
        return self

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current_day > self._ndays:
            raise StopAsyncIteration
        return await self.generate()

    @property
    def ndays(self) -> int:
        """Returns the number of days to generate."""
        return self._ndays

    @property
    def pieces(self) -> List[Piece]:
        """Returns the list of generated pieces."""
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        """Sets the list of generated pieces."""
        self._pieces = value

    @property
    def client(self) -> BeetusClient:
        """Returns the BeetusClient instance."""
        if self._client is None:
            self._client = BeetusClient()
        return self._client

    async def query_pfun(self) -> object:  # type: ignore
        """Queries the PFun API and returns the response."""
        with self.client as client:
            try:
                # Run the synchronous API call in a separate thread to avoid blocking the event loop
                api_response = await asyncio.to_thread(
                    client.run_model_model_run_post,
                    config=self.model_params  # type: ignore
                )
                return api_response
            except Exception as e:
                print(f"Error calling API: {e}")

    async def generate(self):
        """Generates dynamics/procedures based on the PFun API response."""
        api_response = await self.query_pfun()
        piece = Piece(x=self.current_day * 10, y=0, width=10, height=10)
        self.pieces.append(piece)
        self._day += 1
        return piece


class PFunPlatformGenerator(PFunGenerator):
    """Generates a platform based on the PFun API response."""

    def __init__(self, ndays: int = 1, model_params: Optional[CMAModelParams] = None, platform_params: Optional[PlatformParams] = None):
        super().__init__(ndays, model_params)
        self.platform_params = platform_params if platform_params is not None else PlatformParams()

    async def generate_platform(self):
        """Generates a platform based on the PFun API response."""
        api_response = await self.query_pfun()
        # Process the API response to generate the platform
        self._day += 1
        return self.pieces[-1]

    async def generate(self):
        """Generates a platform based on the PFun API response."""
        return await self.generate_platform()

    @property
    def bbox(self):
        """Returns the bounding box of the generated platform."""
        if not self.pieces:
            return None
        min_x = min(piece.x for piece in self.pieces)
        max_x = max(piece.x + piece.width for piece in self.pieces)
        min_y = min(piece.y for piece in self.pieces)
        max_y = max(piece.y + piece.height for piece in self.pieces)
        return (min_x, min_y, max_x, max_y)


class PFunWaveGenerator(PFunGenerator):
    """Generates a wave based on the PFun API response."""

    def __init__(self, ndays: int = 1, model_params: Optional[CMAModelParams] = None, wave_params: Optional[WaveParams] = None):
        super().__init__(ndays, model_params)
        self.pieces = []
        self.wave_params = wave_params if wave_params is not None else WaveParams()

    async def generate_wave(self):
        """Generates a wave based on the PFun API response."""
        api_response = await self.query_pfun()
        # Process the API response
        self._day += 1
        return self.pieces[-1]

    async def generate(self):
        """Generates a wave based on the PFun API response."""
        return await self.generate_wave()
