from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mode_shapes.mode_shapes_request_builder import ModeShapesRequestBuilder
    from .natural_frequencies.natural_frequencies_request_builder import NaturalFrequenciesRequestBuilder

class DynamicRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/dynamic
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DynamicRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/dynamic", path_parameters)
    
    @property
    def mode_shapes(self) -> ModeShapesRequestBuilder:
        """
        The modeShapes property
        """
        from .mode_shapes.mode_shapes_request_builder import ModeShapesRequestBuilder

        return ModeShapesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def natural_frequencies(self) -> NaturalFrequenciesRequestBuilder:
        """
        The naturalFrequencies property
        """
        from .natural_frequencies.natural_frequencies_request_builder import NaturalFrequenciesRequestBuilder

        return NaturalFrequenciesRequestBuilder(self.request_adapter, self.path_parameters)
    

