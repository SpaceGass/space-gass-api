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
    from ......models.member_intermediate_displacement_query_result import MemberIntermediateDisplacementQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberIntermediateDisplacementsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/member-intermediate-displacements
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberIntermediateDisplacementsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/member-intermediate-displacements{?distinctBy*,limit*,loadCases*,maxAbsLocation*,maxAbsTxGlobal*,maxAbsTxLocal*,maxAbsTyGlobal*,maxAbsTyLocal*,maxAbsTzGlobal*,maxAbsTzLocal*,maxLocation*,maxStation*,maxTxGlobal*,maxTxLocal*,maxTyGlobal*,maxTyLocal*,maxTzGlobal*,maxTzLocal*,members*,minAbsLocation*,minAbsTxGlobal*,minAbsTxLocal*,minAbsTyGlobal*,minAbsTyLocal*,minAbsTzGlobal*,minAbsTzLocal*,minLocation*,minStation*,minTxGlobal*,minTxLocal*,minTyGlobal*,minTyLocal*,minTzGlobal*,minTzLocal*,offset*,order*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_location: Optional[float] = None,
        max_abs_tx_global: Optional[float] = None,
        max_abs_tx_local: Optional[float] = None,
        max_abs_ty_global: Optional[float] = None,
        max_abs_ty_local: Optional[float] = None,
        max_abs_tz_global: Optional[float] = None,
        max_abs_tz_local: Optional[float] = None,
        max_location: Optional[float] = None,
        max_station: Optional[float] = None,
        max_tx_global: Optional[float] = None,
        max_tx_local: Optional[float] = None,
        max_ty_global: Optional[float] = None,
        max_ty_local: Optional[float] = None,
        max_tz_global: Optional[float] = None,
        max_tz_local: Optional[float] = None,
        members: Optional[str] = None,
        min_abs_location: Optional[float] = None,
        min_abs_tx_global: Optional[float] = None,
        min_abs_tx_local: Optional[float] = None,
        min_abs_ty_global: Optional[float] = None,
        min_abs_ty_local: Optional[float] = None,
        min_abs_tz_global: Optional[float] = None,
        min_abs_tz_local: Optional[float] = None,
        min_location: Optional[float] = None,
        min_station: Optional[float] = None,
        min_tx_global: Optional[float] = None,
        min_tx_local: Optional[float] = None,
        min_ty_global: Optional[float] = None,
        min_ty_local: Optional[float] = None,
        min_tz_global: Optional[float] = None,
        min_tz_local: Optional[float] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
    ) -> Optional[MemberIntermediateDisplacementQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberIntermediateDisplacementsRequestBuilderGetQueryParameters]] = None) -> Optional[MemberIntermediateDisplacementQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberIntermediateDisplacementsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[MemberIntermediateDisplacementQueryResult]:
        """
        Gets intermediate displacement results for members, grouped by load case and member.Each result contains global and local displacement values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberIntermediateDisplacementQueryResult]
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
        from ......models.member_intermediate_displacement_query_result import MemberIntermediateDisplacementQueryResult

        return await self.request_adapter.send_async(request_info, MemberIntermediateDisplacementQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberIntermediateDisplacementsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets intermediate displacement results for members, grouped by load case and member.Each result contains global and local displacement values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MemberIntermediateDisplacementsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberIntermediateDisplacementsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberIntermediateDisplacementsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberIntermediateDisplacementsRequestBuilderGetQueryParameters():
        """
        Gets intermediate displacement results for members, grouped by load case and member.Each result contains global and local displacement values at stations along the member.
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
            if original_name == "load_cases":
                return "loadCases"
            if original_name == "max_abs_location":
                return "maxAbsLocation"
            if original_name == "max_abs_tx_global":
                return "maxAbsTxGlobal"
            if original_name == "max_abs_tx_local":
                return "maxAbsTxLocal"
            if original_name == "max_abs_ty_global":
                return "maxAbsTyGlobal"
            if original_name == "max_abs_ty_local":
                return "maxAbsTyLocal"
            if original_name == "max_abs_tz_global":
                return "maxAbsTzGlobal"
            if original_name == "max_abs_tz_local":
                return "maxAbsTzLocal"
            if original_name == "max_location":
                return "maxLocation"
            if original_name == "max_station":
                return "maxStation"
            if original_name == "max_tx_global":
                return "maxTxGlobal"
            if original_name == "max_tx_local":
                return "maxTxLocal"
            if original_name == "max_ty_global":
                return "maxTyGlobal"
            if original_name == "max_ty_local":
                return "maxTyLocal"
            if original_name == "max_tz_global":
                return "maxTzGlobal"
            if original_name == "max_tz_local":
                return "maxTzLocal"
            if original_name == "min_abs_location":
                return "minAbsLocation"
            if original_name == "min_abs_tx_global":
                return "minAbsTxGlobal"
            if original_name == "min_abs_tx_local":
                return "minAbsTxLocal"
            if original_name == "min_abs_ty_global":
                return "minAbsTyGlobal"
            if original_name == "min_abs_ty_local":
                return "minAbsTyLocal"
            if original_name == "min_abs_tz_global":
                return "minAbsTzGlobal"
            if original_name == "min_abs_tz_local":
                return "minAbsTzLocal"
            if original_name == "min_location":
                return "minLocation"
            if original_name == "min_station":
                return "minStation"
            if original_name == "min_tx_global":
                return "minTxGlobal"
            if original_name == "min_tx_local":
                return "minTxLocal"
            if original_name == "min_ty_global":
                return "minTyGlobal"
            if original_name == "min_ty_local":
                return "minTyLocal"
            if original_name == "min_tz_global":
                return "minTzGlobal"
            if original_name == "min_tz_local":
                return "minTzLocal"
            if original_name == "limit":
                return "limit"
            if original_name == "members":
                return "members"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            return original_name
        
        # Identity fields: loadCase, member. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose location has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_location: Optional[float] = None

        # Keep rows whose txGlobal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tx_global: Optional[float] = None

        # Keep rows whose txLocal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tx_local: Optional[float] = None

        # Keep rows whose tyGlobal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_ty_global: Optional[float] = None

        # Keep rows whose tyLocal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_ty_local: Optional[float] = None

        # Keep rows whose tzGlobal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tz_global: Optional[float] = None

        # Keep rows whose tzLocal has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tz_local: Optional[float] = None

        # Keep rows whose location is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_location: Optional[float] = None

        # Keep rows whose station is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_station: Optional[float] = None

        # Keep rows whose txGlobal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tx_global: Optional[float] = None

        # Keep rows whose txLocal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tx_local: Optional[float] = None

        # Keep rows whose tyGlobal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_ty_global: Optional[float] = None

        # Keep rows whose tyLocal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_ty_local: Optional[float] = None

        # Keep rows whose tzGlobal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tz_global: Optional[float] = None

        # Keep rows whose tzLocal is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tz_local: Optional[float] = None

        # Member Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        members: Optional[str] = None

        # Keep rows whose location has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_location: Optional[float] = None

        # Keep rows whose txGlobal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tx_global: Optional[float] = None

        # Keep rows whose txLocal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tx_local: Optional[float] = None

        # Keep rows whose tyGlobal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_ty_global: Optional[float] = None

        # Keep rows whose tyLocal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_ty_local: Optional[float] = None

        # Keep rows whose tzGlobal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tz_global: Optional[float] = None

        # Keep rows whose tzLocal has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tz_local: Optional[float] = None

        # Keep rows whose location is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_location: Optional[float] = None

        # Keep rows whose station is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_station: Optional[float] = None

        # Keep rows whose txGlobal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tx_global: Optional[float] = None

        # Keep rows whose txLocal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tx_local: Optional[float] = None

        # Keep rows whose tyGlobal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_ty_global: Optional[float] = None

        # Keep rows whose tyLocal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_ty_local: Optional[float] = None

        # Keep rows whose tzGlobal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tz_global: Optional[float] = None

        # Keep rows whose tzLocal is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tz_local: Optional[float] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, member, station, location, txGlobal, tyGlobal, tzGlobal, txLocal, tyLocal, tzLocal. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class MemberIntermediateDisplacementsRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberIntermediateDisplacementsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

