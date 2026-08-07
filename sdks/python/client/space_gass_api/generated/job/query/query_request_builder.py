from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analysis.analysis_request_builder import AnalysisRequestBuilder
    from .design.design_request_builder import DesignRequestBuilder
    from .geometry.geometry_request_builder import GeometryRequestBuilder

class QueryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new QueryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query", path_parameters)
    
    @property
    def analysis(self) -> AnalysisRequestBuilder:
        """
        The analysis property
        """
        from .analysis.analysis_request_builder import AnalysisRequestBuilder

        return AnalysisRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def design(self) -> DesignRequestBuilder:
        """
        The design property
        """
        from .design.design_request_builder import DesignRequestBuilder

        return DesignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def geometry(self) -> GeometryRequestBuilder:
        """
        The geometry property
        """
        from .geometry.geometry_request_builder import GeometryRequestBuilder

        return GeometryRequestBuilder(self.request_adapter, self.path_parameters)
    

