from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_member_key_item_request_builder import WithMemberKeyItemRequestBuilder

class WithCaseKeyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/member-prestress-loads/{caseKey}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCaseKeyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/member-prestress-loads/{caseKey}", path_parameters)
    
    def by_member_key(self,member_key: int) -> WithMemberKeyItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.memberPrestressLoads.item.item collection
        param member_key: The member number
        Returns: WithMemberKeyItemRequestBuilder
        """
        if member_key is None:
            raise TypeError("member_key cannot be null.")
        from .item.with_member_key_item_request_builder import WithMemberKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["memberKey"] = member_key
        return WithMemberKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

