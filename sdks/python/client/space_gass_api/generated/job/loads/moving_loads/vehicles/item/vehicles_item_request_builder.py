from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union, overload
from warnings import warn

if TYPE_CHECKING:
    from ......models.error_response import ErrorResponse
    from ......models.expand_option import ExpandOption
    from ......models.moving_load_vehicle import MovingLoadVehicle
    from ......models.moving_load_vehicle_update import MovingLoadVehicleUpdate
    from .library.library_request_builder import LibraryRequestBuilder

class VehiclesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads/vehicles/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VehiclesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads/vehicles/{id}{?expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a catalog item. Only unused items can be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
    ) -> Optional[MovingLoadVehicle]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[VehiclesItemRequestBuilderGetQueryParameters]] = None) -> Optional[MovingLoadVehicle]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[VehiclesItemRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[MovingLoadVehicle]:
        """
        Gets a single catalog item by Id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadVehicle]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.moving_load_vehicle import MovingLoadVehicle

        return await self.request_adapter.send_async(request_info, MovingLoadVehicle, error_mapping)
    
    async def patch(self,body: MovingLoadVehicleUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MovingLoadVehicle]:
        """
        Partially updates a catalog item; omitted fields keep their current value.
        param body: Partial update for a user-defined vehicle. All properties are optional; omitted propertieskeep their current value. A library vehicle's source and library cannot be changed here, andload units are fixed at create and intentionally not updatable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadVehicle]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.moving_load_vehicle import MovingLoadVehicle

        return await self.request_adapter.send_async(request_info, MovingLoadVehicle, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a catalog item. Only unused items can be deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VehiclesItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a single catalog item by Id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MovingLoadVehicleUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates a catalog item; omitted fields keep their current value.
        param body: Partial update for a user-defined vehicle. All properties are optional; omitted propertieskeep their current value. A library vehicle's source and library cannot be changed here, andload units are fixed at create and intentionally not updatable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> VehiclesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VehiclesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VehiclesItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def library(self) -> LibraryRequestBuilder:
        """
        The library property
        """
        from .library.library_request_builder import LibraryRequestBuilder

        return LibraryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VehiclesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VehiclesItemRequestBuilderGetQueryParameters():
        """
        Gets a single catalog item by Id.
        """
        # Whether to hydrate the item's sub-resources inline. Defaults to All for a single fetch.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class VehiclesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[VehiclesItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class VehiclesItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

