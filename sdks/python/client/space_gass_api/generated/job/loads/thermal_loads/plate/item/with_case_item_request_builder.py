from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_plate_item_request_builder import WithPlateItemRequestBuilder

class WithCaseItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/thermal-loads/plate/{caseId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/thermal-loads/plate/{caseId}", path_parameters)
    
    def by_plate_id(self,plate_id: int) -> WithPlateItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.thermalLoads.plate.item.item collection
        param plate_id: The plate number
        Returns: WithPlateItemRequestBuilder
        """
        if plate_id is None:
            raise TypeError("plate_id cannot be null.")
        from .item.with_plate_item_request_builder import WithPlateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plateId"] = plate_id
        return WithPlateItemRequestBuilder(self.request_adapter, url_tpl_params)
    

