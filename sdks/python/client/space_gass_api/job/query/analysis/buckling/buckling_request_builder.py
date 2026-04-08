from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_factors.load_factors_request_builder import LoadFactorsRequestBuilder
    from .member.member_request_builder import MemberRequestBuilder

class BucklingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/buckling
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BucklingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/buckling", path_parameters)
    
    @property
    def load_factors(self) -> LoadFactorsRequestBuilder:
        """
        The loadFactors property
        """
        from .load_factors.load_factors_request_builder import LoadFactorsRequestBuilder

        return LoadFactorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member(self) -> MemberRequestBuilder:
        """
        The member property
        """
        from .member.member_request_builder import MemberRequestBuilder

        return MemberRequestBuilder(self.request_adapter, self.path_parameters)
    

