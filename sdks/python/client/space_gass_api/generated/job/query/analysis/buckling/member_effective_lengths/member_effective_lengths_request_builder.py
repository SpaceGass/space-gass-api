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
    from ......models.buckling_effective_length_query_result import BucklingEffectiveLengthQueryResult
    from ......models.error_response import ErrorResponse
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberEffectiveLengthsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/buckling/member-effective-lengths
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberEffectiveLengthsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/buckling/member-effective-lengths{?distinctBy*,exclusionReason*,limit*,loadCases*,maxAbsLength*,maxAbsLy*,maxAbsLz*,maxAbsPcr*,maxLength*,maxLy*,maxLz*,maxPcr*,members*,minAbsLength*,minAbsLy*,minAbsLz*,minAbsPcr*,minLength*,minLy*,minLz*,minPcr*,modes*,offset*,order*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        exclusion_reason: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_length: Optional[float] = None,
        max_abs_ly: Optional[float] = None,
        max_abs_lz: Optional[float] = None,
        max_abs_pcr: Optional[float] = None,
        max_length: Optional[float] = None,
        max_ly: Optional[float] = None,
        max_lz: Optional[float] = None,
        max_pcr: Optional[float] = None,
        members: Optional[str] = None,
        min_abs_length: Optional[float] = None,
        min_abs_ly: Optional[float] = None,
        min_abs_lz: Optional[float] = None,
        min_abs_pcr: Optional[float] = None,
        min_length: Optional[float] = None,
        min_ly: Optional[float] = None,
        min_lz: Optional[float] = None,
        min_pcr: Optional[float] = None,
        modes: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
    ) -> Optional[BucklingEffectiveLengthQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None) -> Optional[BucklingEffectiveLengthQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[BucklingEffectiveLengthQueryResult]:
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BucklingEffectiveLengthQueryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.buckling_effective_length_query_result import BucklingEffectiveLengthQueryResult

        return await self.request_adapter.send_async(request_info, BucklingEffectiveLengthQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MemberEffectiveLengthsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberEffectiveLengthsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberEffectiveLengthsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberEffectiveLengthsRequestBuilderGetQueryParameters():
        """
        Gets buckling effective length results, optionally filtered by load cases, members and modes.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "distinct_by":
                return "distinctBy"
            if original_name == "exclusion_reason":
                return "exclusionReason"
            if original_name == "load_cases":
                return "loadCases"
            if original_name == "max_abs_length":
                return "maxAbsLength"
            if original_name == "max_abs_ly":
                return "maxAbsLy"
            if original_name == "max_abs_lz":
                return "maxAbsLz"
            if original_name == "max_abs_pcr":
                return "maxAbsPcr"
            if original_name == "max_length":
                return "maxLength"
            if original_name == "max_ly":
                return "maxLy"
            if original_name == "max_lz":
                return "maxLz"
            if original_name == "max_pcr":
                return "maxPcr"
            if original_name == "min_abs_length":
                return "minAbsLength"
            if original_name == "min_abs_ly":
                return "minAbsLy"
            if original_name == "min_abs_lz":
                return "minAbsLz"
            if original_name == "min_abs_pcr":
                return "minAbsPcr"
            if original_name == "min_length":
                return "minLength"
            if original_name == "min_ly":
                return "minLy"
            if original_name == "min_lz":
                return "minLz"
            if original_name == "min_pcr":
                return "minPcr"
            if original_name == "limit":
                return "limit"
            if original_name == "members":
                return "members"
            if original_name == "modes":
                return "modes"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            return original_name
        
        # Identity fields: loadCase, mode, member. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Keep rows whose exclusionReason is one of the given values. One or more values, comma-separated, matched case-insensitively.
        exclusion_reason: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose length has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_length: Optional[float] = None

        # Keep rows whose ly has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_ly: Optional[float] = None

        # Keep rows whose lz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_lz: Optional[float] = None

        # Keep rows whose pcr has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_pcr: Optional[float] = None

        # Keep rows whose length is at most this value (in the field's unit, see GET /job/units).
        max_length: Optional[float] = None

        # Keep rows whose ly is at most this value (in the field's unit, see GET /job/units).
        max_ly: Optional[float] = None

        # Keep rows whose lz is at most this value (in the field's unit, see GET /job/units).
        max_lz: Optional[float] = None

        # Keep rows whose pcr is at most this value (in the field's unit, see GET /job/units).
        max_pcr: Optional[float] = None

        # Member Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        members: Optional[str] = None

        # Keep rows whose length has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_length: Optional[float] = None

        # Keep rows whose ly has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_ly: Optional[float] = None

        # Keep rows whose lz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_lz: Optional[float] = None

        # Keep rows whose pcr has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_pcr: Optional[float] = None

        # Keep rows whose length is at least this value (in the field's unit, see GET /job/units).
        min_length: Optional[float] = None

        # Keep rows whose ly is at least this value (in the field's unit, see GET /job/units).
        min_ly: Optional[float] = None

        # Keep rows whose lz is at least this value (in the field's unit, see GET /job/units).
        min_lz: Optional[float] = None

        # Keep rows whose pcr is at least this value (in the field's unit, see GET /job/units).
        min_pcr: Optional[float] = None

        # Buckling mode numbers in SG list format (e.g. `"1-3"`). Omit to return all.
        modes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, mode, member, pcr, length, ly, lz. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class MemberEffectiveLengthsRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberEffectiveLengthsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

