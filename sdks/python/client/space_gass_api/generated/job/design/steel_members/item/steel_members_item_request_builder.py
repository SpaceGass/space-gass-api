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
    from .....models.delete_result import DeleteResult
    from .....models.error_response import ErrorResponse
    from .....models.expand_option import ExpandOption
    from .....models.steel_member import SteelMember
    from .....models.steel_member_update import SteelMemberUpdate

class SteelMembersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design/steel-members/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SteelMembersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design/steel-members/{id}{?expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeleteResult]:
        """
        Deletes the entity with the supplied Id. Returns 404 if no entity with that Id exists.            For entities whose delete cascades (Nodes, Members, Plates), returns 200 with aSpaceGassApi.Models.Dtos.Entity.DeleteResultDto listing every row removed — the entity itself, child rowsthat referenced it (loads, restraints, offsets, plate cuts, …), and any nodes leftdisconnected by the removal. Cleanup is best-effort, not transactional across datasheets:on failure the affected datasheets are reloaded from disk and the request fails.            For all other entities, returns 204 No Content and removes only the entity's own row.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeleteResult]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.delete_result import DeleteResult

        return await self.request_adapter.send_async(request_info, DeleteResult, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
    ) -> Optional[SteelMember]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[SteelMembersItemRequestBuilderGetQueryParameters]] = None) -> Optional[SteelMember]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[SteelMembersItemRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[SteelMember]:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SteelMember]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.steel_member import SteelMember

        return await self.request_adapter.send_async(request_info, SteelMember, error_mapping)
    
    async def patch(self,body: SteelMemberUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SteelMember]:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for updating an existing steel member design data entity (design group).All fields are nullable to support partial updates — omit a field to keep its current value.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SteelMember]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.steel_member import SteelMember

        return await self.request_adapter.send_async(request_info, SteelMember, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the entity with the supplied Id. Returns 404 if no entity with that Id exists.            For entities whose delete cascades (Nodes, Members, Plates), returns 200 with aSpaceGassApi.Models.Dtos.Entity.DeleteResultDto listing every row removed — the entity itself, child rowsthat referenced it (loads, restraints, offsets, plate cuts, …), and any nodes leftdisconnected by the removal. Cleanup is best-effort, not transactional across datasheets:on failure the affected datasheets are reloaded from disk and the request fails.            For all other entities, returns 204 No Content and removes only the entity's own row.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SteelMembersItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SteelMemberUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for updating an existing steel member design data entity (design group).All fields are nullable to support partial updates — omit a field to keep its current value.
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
    
    def with_url(self,raw_url: str) -> SteelMembersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SteelMembersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SteelMembersItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SteelMembersItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SteelMembersItemRequestBuilderGetQueryParameters():
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        """
        # Sub-resource expansion. Defaults to `all`; pass `none` to suppress sub-resource hydration.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class SteelMembersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SteelMembersItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SteelMembersItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

