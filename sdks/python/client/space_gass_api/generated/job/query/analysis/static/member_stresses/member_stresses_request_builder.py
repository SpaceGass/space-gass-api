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
    from ......models.member_stress_query_result import MemberStressQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class MemberStressesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/member-stresses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberStressesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/member-stresses{?distinctBy*,limit*,loadCases*,maxAbsMx*,maxAbsMyBtm*,maxAbsMyTop*,maxAbsMzBtm*,maxAbsMzTop*,maxAbsN*,maxAbsNMyBtm*,maxAbsNMyTop*,maxAbsNMzBtm*,maxAbsNMzTop*,maxAbsPosition*,maxAbsVy*,maxAbsVz*,maxMx*,maxMyBtm*,maxMyTop*,maxMzBtm*,maxMzTop*,maxN*,maxNMyBtm*,maxNMyTop*,maxNMzBtm*,maxNMzTop*,maxPosition*,maxStation*,maxVy*,maxVz*,members*,minAbsMx*,minAbsMyBtm*,minAbsMyTop*,minAbsMzBtm*,minAbsMzTop*,minAbsN*,minAbsNMyBtm*,minAbsNMyTop*,minAbsNMzBtm*,minAbsNMzTop*,minAbsPosition*,minAbsVy*,minAbsVz*,minMx*,minMyBtm*,minMyTop*,minMzBtm*,minMzTop*,minN*,minNMyBtm*,minNMyTop*,minNMzBtm*,minNMzTop*,minPosition*,minStation*,minVy*,minVz*,offset*,order*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_mx: Optional[float] = None,
        max_abs_my_btm: Optional[float] = None,
        max_abs_my_top: Optional[float] = None,
        max_abs_mz_btm: Optional[float] = None,
        max_abs_mz_top: Optional[float] = None,
        max_abs_n: Optional[float] = None,
        max_abs_n_my_btm: Optional[float] = None,
        max_abs_n_my_top: Optional[float] = None,
        max_abs_n_mz_btm: Optional[float] = None,
        max_abs_n_mz_top: Optional[float] = None,
        max_abs_position: Optional[float] = None,
        max_abs_vy: Optional[float] = None,
        max_abs_vz: Optional[float] = None,
        max_mx: Optional[float] = None,
        max_my_btm: Optional[float] = None,
        max_my_top: Optional[float] = None,
        max_mz_btm: Optional[float] = None,
        max_mz_top: Optional[float] = None,
        max_n: Optional[float] = None,
        max_n_my_btm: Optional[float] = None,
        max_n_my_top: Optional[float] = None,
        max_n_mz_btm: Optional[float] = None,
        max_n_mz_top: Optional[float] = None,
        max_position: Optional[float] = None,
        max_station: Optional[float] = None,
        max_vy: Optional[float] = None,
        max_vz: Optional[float] = None,
        members: Optional[str] = None,
        min_abs_mx: Optional[float] = None,
        min_abs_my_btm: Optional[float] = None,
        min_abs_my_top: Optional[float] = None,
        min_abs_mz_btm: Optional[float] = None,
        min_abs_mz_top: Optional[float] = None,
        min_abs_n: Optional[float] = None,
        min_abs_n_my_btm: Optional[float] = None,
        min_abs_n_my_top: Optional[float] = None,
        min_abs_n_mz_btm: Optional[float] = None,
        min_abs_n_mz_top: Optional[float] = None,
        min_abs_position: Optional[float] = None,
        min_abs_vy: Optional[float] = None,
        min_abs_vz: Optional[float] = None,
        min_mx: Optional[float] = None,
        min_my_btm: Optional[float] = None,
        min_my_top: Optional[float] = None,
        min_mz_btm: Optional[float] = None,
        min_mz_top: Optional[float] = None,
        min_n: Optional[float] = None,
        min_n_my_btm: Optional[float] = None,
        min_n_my_top: Optional[float] = None,
        min_n_mz_btm: Optional[float] = None,
        min_n_mz_top: Optional[float] = None,
        min_position: Optional[float] = None,
        min_station: Optional[float] = None,
        min_vy: Optional[float] = None,
        min_vz: Optional[float] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
    ) -> Optional[MemberStressQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[MemberStressesRequestBuilderGetQueryParameters]] = None) -> Optional[MemberStressQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[MemberStressesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[MemberStressQueryResult]:
        """
        Gets stress results for members, grouped by load case and member.Each result contains stress values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberStressQueryResult]
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
        from ......models.member_stress_query_result import MemberStressQueryResult

        return await self.request_adapter.send_async(request_info, MemberStressQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MemberStressesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets stress results for members, grouped by load case and member.Each result contains stress values at stations along the member.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MemberStressesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MemberStressesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MemberStressesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MemberStressesRequestBuilderGetQueryParameters():
        """
        Gets stress results for members, grouped by load case and member.Each result contains stress values at stations along the member.
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
            if original_name == "max_abs_mx":
                return "maxAbsMx"
            if original_name == "max_abs_my_btm":
                return "maxAbsMyBtm"
            if original_name == "max_abs_my_top":
                return "maxAbsMyTop"
            if original_name == "max_abs_mz_btm":
                return "maxAbsMzBtm"
            if original_name == "max_abs_mz_top":
                return "maxAbsMzTop"
            if original_name == "max_abs_n":
                return "maxAbsN"
            if original_name == "max_abs_n_my_btm":
                return "maxAbsNMyBtm"
            if original_name == "max_abs_n_my_top":
                return "maxAbsNMyTop"
            if original_name == "max_abs_n_mz_btm":
                return "maxAbsNMzBtm"
            if original_name == "max_abs_n_mz_top":
                return "maxAbsNMzTop"
            if original_name == "max_abs_position":
                return "maxAbsPosition"
            if original_name == "max_abs_vy":
                return "maxAbsVy"
            if original_name == "max_abs_vz":
                return "maxAbsVz"
            if original_name == "max_mx":
                return "maxMx"
            if original_name == "max_my_btm":
                return "maxMyBtm"
            if original_name == "max_my_top":
                return "maxMyTop"
            if original_name == "max_mz_btm":
                return "maxMzBtm"
            if original_name == "max_mz_top":
                return "maxMzTop"
            if original_name == "max_n":
                return "maxN"
            if original_name == "max_n_my_btm":
                return "maxNMyBtm"
            if original_name == "max_n_my_top":
                return "maxNMyTop"
            if original_name == "max_n_mz_btm":
                return "maxNMzBtm"
            if original_name == "max_n_mz_top":
                return "maxNMzTop"
            if original_name == "max_position":
                return "maxPosition"
            if original_name == "max_station":
                return "maxStation"
            if original_name == "max_vy":
                return "maxVy"
            if original_name == "max_vz":
                return "maxVz"
            if original_name == "min_abs_mx":
                return "minAbsMx"
            if original_name == "min_abs_my_btm":
                return "minAbsMyBtm"
            if original_name == "min_abs_my_top":
                return "minAbsMyTop"
            if original_name == "min_abs_mz_btm":
                return "minAbsMzBtm"
            if original_name == "min_abs_mz_top":
                return "minAbsMzTop"
            if original_name == "min_abs_n":
                return "minAbsN"
            if original_name == "min_abs_n_my_btm":
                return "minAbsNMyBtm"
            if original_name == "min_abs_n_my_top":
                return "minAbsNMyTop"
            if original_name == "min_abs_n_mz_btm":
                return "minAbsNMzBtm"
            if original_name == "min_abs_n_mz_top":
                return "minAbsNMzTop"
            if original_name == "min_abs_position":
                return "minAbsPosition"
            if original_name == "min_abs_vy":
                return "minAbsVy"
            if original_name == "min_abs_vz":
                return "minAbsVz"
            if original_name == "min_mx":
                return "minMx"
            if original_name == "min_my_btm":
                return "minMyBtm"
            if original_name == "min_my_top":
                return "minMyTop"
            if original_name == "min_mz_btm":
                return "minMzBtm"
            if original_name == "min_mz_top":
                return "minMzTop"
            if original_name == "min_n":
                return "minN"
            if original_name == "min_n_my_btm":
                return "minNMyBtm"
            if original_name == "min_n_my_top":
                return "minNMyTop"
            if original_name == "min_n_mz_btm":
                return "minNMzBtm"
            if original_name == "min_n_mz_top":
                return "minNMzTop"
            if original_name == "min_position":
                return "minPosition"
            if original_name == "min_station":
                return "minStation"
            if original_name == "min_vy":
                return "minVy"
            if original_name == "min_vz":
                return "minVz"
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

        # Keep rows whose mx has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_mx: Optional[float] = None

        # Keep rows whose myBtm has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_my_btm: Optional[float] = None

        # Keep rows whose myTop has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_my_top: Optional[float] = None

        # Keep rows whose mzBtm has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_mz_btm: Optional[float] = None

        # Keep rows whose mzTop has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_mz_top: Optional[float] = None

        # Keep rows whose n has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_n: Optional[float] = None

        # Keep rows whose nMyBtm has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_n_my_btm: Optional[float] = None

        # Keep rows whose nMyTop has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_n_my_top: Optional[float] = None

        # Keep rows whose nMzBtm has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_n_mz_btm: Optional[float] = None

        # Keep rows whose nMzTop has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_n_mz_top: Optional[float] = None

        # Keep rows whose position has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_position: Optional[float] = None

        # Keep rows whose vy has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_vy: Optional[float] = None

        # Keep rows whose vz has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_vz: Optional[float] = None

        # Keep rows whose mx is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_mx: Optional[float] = None

        # Keep rows whose myBtm is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_my_btm: Optional[float] = None

        # Keep rows whose myTop is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_my_top: Optional[float] = None

        # Keep rows whose mzBtm is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_mz_btm: Optional[float] = None

        # Keep rows whose mzTop is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_mz_top: Optional[float] = None

        # Keep rows whose n is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_n: Optional[float] = None

        # Keep rows whose nMyBtm is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_n_my_btm: Optional[float] = None

        # Keep rows whose nMyTop is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_n_my_top: Optional[float] = None

        # Keep rows whose nMzBtm is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_n_mz_btm: Optional[float] = None

        # Keep rows whose nMzTop is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_n_mz_top: Optional[float] = None

        # Keep rows whose position is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_position: Optional[float] = None

        # Keep rows whose station is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_station: Optional[float] = None

        # Keep rows whose vy is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_vy: Optional[float] = None

        # Keep rows whose vz is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_vz: Optional[float] = None

        # Member Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        members: Optional[str] = None

        # Keep rows whose mx has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_mx: Optional[float] = None

        # Keep rows whose myBtm has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_my_btm: Optional[float] = None

        # Keep rows whose myTop has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_my_top: Optional[float] = None

        # Keep rows whose mzBtm has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_mz_btm: Optional[float] = None

        # Keep rows whose mzTop has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_mz_top: Optional[float] = None

        # Keep rows whose n has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_n: Optional[float] = None

        # Keep rows whose nMyBtm has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_n_my_btm: Optional[float] = None

        # Keep rows whose nMyTop has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_n_my_top: Optional[float] = None

        # Keep rows whose nMzBtm has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_n_mz_btm: Optional[float] = None

        # Keep rows whose nMzTop has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_n_mz_top: Optional[float] = None

        # Keep rows whose position has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_position: Optional[float] = None

        # Keep rows whose vy has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_vy: Optional[float] = None

        # Keep rows whose vz has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_vz: Optional[float] = None

        # Keep rows whose mx is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_mx: Optional[float] = None

        # Keep rows whose myBtm is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_my_btm: Optional[float] = None

        # Keep rows whose myTop is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_my_top: Optional[float] = None

        # Keep rows whose mzBtm is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_mz_btm: Optional[float] = None

        # Keep rows whose mzTop is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_mz_top: Optional[float] = None

        # Keep rows whose n is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_n: Optional[float] = None

        # Keep rows whose nMyBtm is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_n_my_btm: Optional[float] = None

        # Keep rows whose nMyTop is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_n_my_top: Optional[float] = None

        # Keep rows whose nMzBtm is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_n_mz_btm: Optional[float] = None

        # Keep rows whose nMzTop is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_n_mz_top: Optional[float] = None

        # Keep rows whose position is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_position: Optional[float] = None

        # Keep rows whose station is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_station: Optional[float] = None

        # Keep rows whose vy is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_vy: Optional[float] = None

        # Keep rows whose vz is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_vz: Optional[float] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, member, station, position, n, vy, vz, mx, myTop, myBtm, mzTop, mzBtm, nMyTop, nMyBtm, nMzTop, nMzBtm. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class MemberStressesRequestBuilderGetRequestConfiguration(RequestConfiguration[MemberStressesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

