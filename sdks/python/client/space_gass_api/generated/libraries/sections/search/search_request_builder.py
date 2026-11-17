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
    from ....models.error_response import ErrorResponse
    from ....models.library_search_result import LibrarySearchResult

class SearchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /libraries/sections/search
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SearchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/libraries/sections/search{?group*,library*,limit*,offset*,q*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        group: Optional[str] = None,
        library: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        q: Optional[str] = None,
    ) -> Optional[LibrarySearchResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[SearchRequestBuilderGetQueryParameters]] = None) -> Optional[LibrarySearchResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[SearchRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[LibrarySearchResult]:
        """
        Searches section names across the section libraries, case-insensitively andignoring separator characters, with typo tolerance. Returns a summary of the outcome(total matches, strongest match type) plus the matching items, strongest matchfirst. Among equally strong matches, items from the default library (seeGET /job/settings/default-libraries) rank first. Omit q to list names instead of searching: everysection in scope is returned in library order.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LibrarySearchResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.library_search_result import LibrarySearchResult

        return await self.request_adapter.send_async(request_info, LibrarySearchResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SearchRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Searches section names across the section libraries, case-insensitively andignoring separator characters, with typo tolerance. Returns a summary of the outcome(total matches, strongest match type) plus the matching items, strongest matchfirst. Among equally strong matches, items from the default library (seeGET /job/settings/default-libraries) rank first. Omit q to list names instead of searching: everysection in scope is returned in library order.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SearchRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SearchRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SearchRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SearchRequestBuilderGetQueryParameters():
        """
        Searches section names across the section libraries, case-insensitively andignoring separator characters, with typo tolerance. Returns a summary of the outcome(total matches, strongest match type) plus the matching items, strongest matchfirst. Among equally strong matches, items from the default library (seeGET /job/settings/default-libraries) rank first. Omit q to list names instead of searching: everysection in scope is returned in library order.
        """
        # Optional group name (case-insensitive). Only sections in that group are included; an unmatched group returns an empty result. Omit to cover every group
        group: Optional[str] = None

        # Optional library name (case-insensitive). Only that library is searched; omit to cover every library of the type
        library: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # The search text. Omit to list every section in scope
        q: Optional[str] = None

    
    @dataclass
    class SearchRequestBuilderGetRequestConfiguration(RequestConfiguration[SearchRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

