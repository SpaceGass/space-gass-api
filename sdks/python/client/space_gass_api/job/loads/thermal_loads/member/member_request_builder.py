from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_case_key_item_request_builder import WithCaseKeyItemRequestBuilder

class MemberRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/thermal-loads/member
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/thermal-loads/member", path_parameters)
    
    def by_case_key(self,case_key: int) -> WithCaseKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.thermalLoads.member.item collection
        param case_key: The load case number
        Returns: WithCaseKeyItemRequestBuilder
        """
        if case_key is None:
            raise TypeError("case_key cannot be null.")
        from .item.with_case_key_item_request_builder import WithCaseKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseKey"] = case_key
        return WithCaseKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

