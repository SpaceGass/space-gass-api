from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_summary.check_summary_request_builder import CheckSummaryRequestBuilder

class SteelMemberRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/design/steel-member
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SteelMemberRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/design/steel-member", path_parameters)
    
    @property
    def check_summary(self) -> CheckSummaryRequestBuilder:
        """
        The checkSummary property
        """
        from .check_summary.check_summary_request_builder import CheckSummaryRequestBuilder

        return CheckSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    

