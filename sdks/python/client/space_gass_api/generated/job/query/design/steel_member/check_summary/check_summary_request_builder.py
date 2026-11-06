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
    from ......models.result_sort_order import ResultSortOrder
    from ......models.steel_check_summary_query_result import SteelCheckSummaryQueryResult
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class CheckSummaryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/design/steel-member/check-summary
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CheckSummaryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/design/steel-member/check-summary{?distinctBy*,failure*,limit*,maxAbsLoadFactor*,maxAbsSegmentLength*,maxAbsTotalLength*,maxAbsYield*,maxCriticalCase*,maxLoadFactor*,maxSegmentLength*,maxTotalLength*,maxYield*,minAbsLoadFactor*,minAbsSegmentLength*,minAbsTotalLength*,minAbsYield*,minCriticalCase*,minLoadFactor*,minSegmentLength*,minTotalLength*,minYield*,offset*,order*,section*,sectionDiffersFromModel*,sort*,status*,steelMembers*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        failure: Optional[str] = None,
        limit: Optional[int] = None,
        max_abs_load_factor: Optional[float] = None,
        max_abs_segment_length: Optional[float] = None,
        max_abs_total_length: Optional[float] = None,
        max_abs_yield: Optional[float] = None,
        max_critical_case: Optional[float] = None,
        max_load_factor: Optional[float] = None,
        max_segment_length: Optional[float] = None,
        max_total_length: Optional[float] = None,
        max_yield: Optional[float] = None,
        min_abs_load_factor: Optional[float] = None,
        min_abs_segment_length: Optional[float] = None,
        min_abs_total_length: Optional[float] = None,
        min_abs_yield: Optional[float] = None,
        min_critical_case: Optional[float] = None,
        min_load_factor: Optional[float] = None,
        min_segment_length: Optional[float] = None,
        min_total_length: Optional[float] = None,
        min_yield: Optional[float] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        section: Optional[str] = None,
        section_differs_from_model: Optional[str] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        steel_members: Optional[str] = None,
    ) -> Optional[SteelCheckSummaryQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[CheckSummaryRequestBuilderGetQueryParameters]] = None) -> Optional[SteelCheckSummaryQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[CheckSummaryRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[SteelCheckSummaryQueryResult]:
        """
        Gets the steel member design check summary: one row per steel member (design group,GET /job/design/steel-members), keyed by its Id in `steelMember`, optionallyfiltered by steel member Id. `status` is the check outcome, `section` thesection checked or selected, and `sectionDiffersFromModel` whether thatsection differs from the one the model carries.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SteelCheckSummaryQueryResult]
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
        from ......models.steel_check_summary_query_result import SteelCheckSummaryQueryResult

        return await self.request_adapter.send_async(request_info, SteelCheckSummaryQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CheckSummaryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets the steel member design check summary: one row per steel member (design group,GET /job/design/steel-members), keyed by its Id in `steelMember`, optionallyfiltered by steel member Id. `status` is the check outcome, `section` thesection checked or selected, and `sectionDiffersFromModel` whether thatsection differs from the one the model carries.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CheckSummaryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CheckSummaryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CheckSummaryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CheckSummaryRequestBuilderGetQueryParameters():
        """
        Gets the steel member design check summary: one row per steel member (design group,GET /job/design/steel-members), keyed by its Id in `steelMember`, optionallyfiltered by steel member Id. `status` is the check outcome, `section` thesection checked or selected, and `sectionDiffersFromModel` whether thatsection differs from the one the model carries.
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
            if original_name == "max_abs_load_factor":
                return "maxAbsLoadFactor"
            if original_name == "max_abs_segment_length":
                return "maxAbsSegmentLength"
            if original_name == "max_abs_total_length":
                return "maxAbsTotalLength"
            if original_name == "max_abs_yield":
                return "maxAbsYield"
            if original_name == "max_critical_case":
                return "maxCriticalCase"
            if original_name == "max_load_factor":
                return "maxLoadFactor"
            if original_name == "max_segment_length":
                return "maxSegmentLength"
            if original_name == "max_total_length":
                return "maxTotalLength"
            if original_name == "max_yield":
                return "maxYield"
            if original_name == "min_abs_load_factor":
                return "minAbsLoadFactor"
            if original_name == "min_abs_segment_length":
                return "minAbsSegmentLength"
            if original_name == "min_abs_total_length":
                return "minAbsTotalLength"
            if original_name == "min_abs_yield":
                return "minAbsYield"
            if original_name == "min_critical_case":
                return "minCriticalCase"
            if original_name == "min_load_factor":
                return "minLoadFactor"
            if original_name == "min_segment_length":
                return "minSegmentLength"
            if original_name == "min_total_length":
                return "minTotalLength"
            if original_name == "min_yield":
                return "minYield"
            if original_name == "section_differs_from_model":
                return "sectionDiffersFromModel"
            if original_name == "steel_members":
                return "steelMembers"
            if original_name == "failure":
                return "failure"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "section":
                return "section"
            if original_name == "sort":
                return "sort"
            if original_name == "status":
                return "status"
            return original_name
        
        # Identity fields: steelMember. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Keep rows whose failure is one of the given values. One or more values, comma-separated, matched case-insensitively.
        failure: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Keep rows whose loadFactor has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_load_factor: Optional[float] = None

        # Keep rows whose segmentLength has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_segment_length: Optional[float] = None

        # Keep rows whose totalLength has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_total_length: Optional[float] = None

        # Keep rows whose yield has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_yield: Optional[float] = None

        # Keep rows whose criticalCase is at most this value (in the field's unit, see GET /job/units).
        max_critical_case: Optional[float] = None

        # Keep rows whose loadFactor is at most this value (in the field's unit, see GET /job/units).
        max_load_factor: Optional[float] = None

        # Keep rows whose segmentLength is at most this value (in the field's unit, see GET /job/units).
        max_segment_length: Optional[float] = None

        # Keep rows whose totalLength is at most this value (in the field's unit, see GET /job/units).
        max_total_length: Optional[float] = None

        # Keep rows whose yield is at most this value (in the field's unit, see GET /job/units).
        max_yield: Optional[float] = None

        # Keep rows whose loadFactor has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_load_factor: Optional[float] = None

        # Keep rows whose segmentLength has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_segment_length: Optional[float] = None

        # Keep rows whose totalLength has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_total_length: Optional[float] = None

        # Keep rows whose yield has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_yield: Optional[float] = None

        # Keep rows whose criticalCase is at least this value (in the field's unit, see GET /job/units).
        min_critical_case: Optional[float] = None

        # Keep rows whose loadFactor is at least this value (in the field's unit, see GET /job/units).
        min_load_factor: Optional[float] = None

        # Keep rows whose segmentLength is at least this value (in the field's unit, see GET /job/units).
        min_segment_length: Optional[float] = None

        # Keep rows whose totalLength is at least this value (in the field's unit, see GET /job/units).
        min_total_length: Optional[float] = None

        # Keep rows whose yield is at least this value (in the field's unit, see GET /job/units).
        min_yield: Optional[float] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Keep rows whose section is one of the given values. One or more values, comma-separated, matched case-insensitively.
        section: Optional[str] = None

        # Keep rows whose sectionDiffersFromModel is one of the given values. true or false.
        section_differs_from_model: Optional[str] = None

        # Sortable fields: steelMember, yield, totalLength, segmentLength, criticalCase, loadFactor. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

        # Keep rows whose status is one of the given values. One or more of: Passed, PassedWithWarnings, Failed (comma-separated, case-insensitive).
        status: Optional[str] = None

        # Steel member (design group) Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all. The former name `members` is rejected with a 400.
        steel_members: Optional[str] = None

    
    @dataclass
    class CheckSummaryRequestBuilderGetRequestConfiguration(RequestConfiguration[CheckSummaryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

