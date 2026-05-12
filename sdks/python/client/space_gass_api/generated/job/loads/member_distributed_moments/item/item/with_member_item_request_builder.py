from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_sub_load_item_request_builder import WithSubLoadItemRequestBuilder

class WithMemberItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/member-distributed-moments/{caseId}/{memberId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithMemberItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/member-distributed-moments/{caseId}/{memberId}", path_parameters)
    
    def by_sub_load_id(self,sub_load_id: int) -> WithSubLoadItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.memberDistributedMoments.item.item.item collection
        param sub_load_id: The sub-load number
        Returns: WithSubLoadItemRequestBuilder
        """
        if sub_load_id is None:
            raise TypeError("sub_load_id cannot be null.")
        from .item.with_sub_load_item_request_builder import WithSubLoadItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subLoadId"] = sub_load_id
        return WithSubLoadItemRequestBuilder(self.request_adapter, url_tpl_params)
    

