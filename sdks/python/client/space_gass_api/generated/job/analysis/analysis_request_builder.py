from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .buckling.buckling_request_builder import BucklingRequestBuilder
    from .dynamic_frequency.dynamic_frequency_request_builder import DynamicFrequencyRequestBuilder
    from .runs.runs_request_builder import RunsRequestBuilder
    from .static.static_request_builder import StaticRequestBuilder

class AnalysisRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/analysis
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AnalysisRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/analysis", path_parameters)
    
    @property
    def buckling(self) -> BucklingRequestBuilder:
        """
        The buckling property
        """
        from .buckling.buckling_request_builder import BucklingRequestBuilder

        return BucklingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dynamic_frequency(self) -> DynamicFrequencyRequestBuilder:
        """
        The dynamicFrequency property
        """
        from .dynamic_frequency.dynamic_frequency_request_builder import DynamicFrequencyRequestBuilder

        return DynamicFrequencyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def runs(self) -> RunsRequestBuilder:
        """
        The runs property
        """
        from .runs.runs_request_builder import RunsRequestBuilder

        return RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def static(self) -> StaticRequestBuilder:
        """
        The static property
        """
        from .static.static_request_builder import StaticRequestBuilder

        return StaticRequestBuilder(self.request_adapter, self.path_parameters)
    

