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
    from ......models.natural_frequency_query_result import NaturalFrequencyQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class NaturalFrequenciesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/dynamic/natural-frequencies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NaturalFrequenciesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/dynamic/natural-frequencies{?distinctBy*,limit*,loadCases*,maxAbsFrequencyTolerance*,maxAbsMassPartX*,maxAbsMassPartY*,maxAbsMassPartZ*,maxAbsNaturalFrequency*,maxAbsNaturalPeriod*,maxFrequencyTolerance*,maxIterations*,maxMassPartX*,maxMassPartY*,maxMassPartZ*,maxNaturalFrequency*,maxNaturalPeriod*,minAbsFrequencyTolerance*,minAbsMassPartX*,minAbsMassPartY*,minAbsMassPartZ*,minAbsNaturalFrequency*,minAbsNaturalPeriod*,minFrequencyTolerance*,minIterations*,minMassPartX*,minMassPartY*,minMassPartZ*,minNaturalFrequency*,minNaturalPeriod*,modes*,offset*,order*,sort*,status*,warning*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_frequency_tolerance: Optional[float] = None,
        max_abs_mass_part_x: Optional[float] = None,
        max_abs_mass_part_y: Optional[float] = None,
        max_abs_mass_part_z: Optional[float] = None,
        max_abs_natural_frequency: Optional[float] = None,
        max_abs_natural_period: Optional[float] = None,
        max_frequency_tolerance: Optional[float] = None,
        max_iterations: Optional[float] = None,
        max_mass_part_x: Optional[float] = None,
        max_mass_part_y: Optional[float] = None,
        max_mass_part_z: Optional[float] = None,
        max_natural_frequency: Optional[float] = None,
        max_natural_period: Optional[float] = None,
        min_abs_frequency_tolerance: Optional[float] = None,
        min_abs_mass_part_x: Optional[float] = None,
        min_abs_mass_part_y: Optional[float] = None,
        min_abs_mass_part_z: Optional[float] = None,
        min_abs_natural_frequency: Optional[float] = None,
        min_abs_natural_period: Optional[float] = None,
        min_frequency_tolerance: Optional[float] = None,
        min_iterations: Optional[float] = None,
        min_mass_part_x: Optional[float] = None,
        min_mass_part_y: Optional[float] = None,
        min_mass_part_z: Optional[float] = None,
        min_natural_frequency: Optional[float] = None,
        min_natural_period: Optional[float] = None,
        modes: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        warning: Optional[str] = None,
    ) -> Optional[NaturalFrequencyQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[NaturalFrequenciesRequestBuilderGetQueryParameters]] = None) -> Optional[NaturalFrequencyQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[NaturalFrequenciesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[NaturalFrequencyQueryResult]:
        """
        Gets natural frequency results, optionally filtered by load cases and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NaturalFrequencyQueryResult]
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
        from ......models.natural_frequency_query_result import NaturalFrequencyQueryResult

        return await self.request_adapter.send_async(request_info, NaturalFrequencyQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NaturalFrequenciesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets natural frequency results, optionally filtered by load cases and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> NaturalFrequenciesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NaturalFrequenciesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NaturalFrequenciesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NaturalFrequenciesRequestBuilderGetQueryParameters():
        """
        Gets natural frequency results, optionally filtered by load cases and modes.
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
            if original_name == "max_abs_frequency_tolerance":
                return "maxAbsFrequencyTolerance"
            if original_name == "max_abs_mass_part_x":
                return "maxAbsMassPartX"
            if original_name == "max_abs_mass_part_y":
                return "maxAbsMassPartY"
            if original_name == "max_abs_mass_part_z":
                return "maxAbsMassPartZ"
            if original_name == "max_abs_natural_frequency":
                return "maxAbsNaturalFrequency"
            if original_name == "max_abs_natural_period":
                return "maxAbsNaturalPeriod"
            if original_name == "max_frequency_tolerance":
                return "maxFrequencyTolerance"
            if original_name == "max_iterations":
                return "maxIterations"
            if original_name == "max_mass_part_x":
                return "maxMassPartX"
            if original_name == "max_mass_part_y":
                return "maxMassPartY"
            if original_name == "max_mass_part_z":
                return "maxMassPartZ"
            if original_name == "max_natural_frequency":
                return "maxNaturalFrequency"
            if original_name == "max_natural_period":
                return "maxNaturalPeriod"
            if original_name == "min_abs_frequency_tolerance":
                return "minAbsFrequencyTolerance"
            if original_name == "min_abs_mass_part_x":
                return "minAbsMassPartX"
            if original_name == "min_abs_mass_part_y":
                return "minAbsMassPartY"
            if original_name == "min_abs_mass_part_z":
                return "minAbsMassPartZ"
            if original_name == "min_abs_natural_frequency":
                return "minAbsNaturalFrequency"
            if original_name == "min_abs_natural_period":
                return "minAbsNaturalPeriod"
            if original_name == "min_frequency_tolerance":
                return "minFrequencyTolerance"
            if original_name == "min_iterations":
                return "minIterations"
            if original_name == "min_mass_part_x":
                return "minMassPartX"
            if original_name == "min_mass_part_y":
                return "minMassPartY"
            if original_name == "min_mass_part_z":
                return "minMassPartZ"
            if original_name == "min_natural_frequency":
                return "minNaturalFrequency"
            if original_name == "min_natural_period":
                return "minNaturalPeriod"
            if original_name == "limit":
                return "limit"
            if original_name == "modes":
                return "modes"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            if original_name == "status":
                return "status"
            if original_name == "warning":
                return "warning"
            return original_name
        
        # Identity fields: loadCase, mode. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose frequencyTolerance has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_frequency_tolerance: Optional[float] = None

        # Keep rows whose massPartX has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mass_part_x: Optional[float] = None

        # Keep rows whose massPartY has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mass_part_y: Optional[float] = None

        # Keep rows whose massPartZ has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mass_part_z: Optional[float] = None

        # Keep rows whose naturalFrequency has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_natural_frequency: Optional[float] = None

        # Keep rows whose naturalPeriod has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_natural_period: Optional[float] = None

        # Keep rows whose frequencyTolerance is at most this value (in the field's unit, see GET /job/units).
        max_frequency_tolerance: Optional[float] = None

        # Keep rows whose iterations is at most this value (in the field's unit, see GET /job/units).
        max_iterations: Optional[float] = None

        # Keep rows whose massPartX is at most this value (in the field's unit, see GET /job/units).
        max_mass_part_x: Optional[float] = None

        # Keep rows whose massPartY is at most this value (in the field's unit, see GET /job/units).
        max_mass_part_y: Optional[float] = None

        # Keep rows whose massPartZ is at most this value (in the field's unit, see GET /job/units).
        max_mass_part_z: Optional[float] = None

        # Keep rows whose naturalFrequency is at most this value (in the field's unit, see GET /job/units).
        max_natural_frequency: Optional[float] = None

        # Keep rows whose naturalPeriod is at most this value (in the field's unit, see GET /job/units).
        max_natural_period: Optional[float] = None

        # Keep rows whose frequencyTolerance has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_frequency_tolerance: Optional[float] = None

        # Keep rows whose massPartX has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mass_part_x: Optional[float] = None

        # Keep rows whose massPartY has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mass_part_y: Optional[float] = None

        # Keep rows whose massPartZ has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mass_part_z: Optional[float] = None

        # Keep rows whose naturalFrequency has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_natural_frequency: Optional[float] = None

        # Keep rows whose naturalPeriod has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_natural_period: Optional[float] = None

        # Keep rows whose frequencyTolerance is at least this value (in the field's unit, see GET /job/units).
        min_frequency_tolerance: Optional[float] = None

        # Keep rows whose iterations is at least this value (in the field's unit, see GET /job/units).
        min_iterations: Optional[float] = None

        # Keep rows whose massPartX is at least this value (in the field's unit, see GET /job/units).
        min_mass_part_x: Optional[float] = None

        # Keep rows whose massPartY is at least this value (in the field's unit, see GET /job/units).
        min_mass_part_y: Optional[float] = None

        # Keep rows whose massPartZ is at least this value (in the field's unit, see GET /job/units).
        min_mass_part_z: Optional[float] = None

        # Keep rows whose naturalFrequency is at least this value (in the field's unit, see GET /job/units).
        min_natural_frequency: Optional[float] = None

        # Keep rows whose naturalPeriod is at least this value (in the field's unit, see GET /job/units).
        min_natural_period: Optional[float] = None

        # Mode numbers in SG list format (e.g. `"1-3"`). Omit to return all.
        modes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, mode, naturalFrequency, naturalPeriod, frequencyTolerance, iterations, massPartX, massPartY, massPartZ. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

        # Keep rows whose status is one of the given values. One or more of: Reported, AboveUpperLimit, BelowLowerLimit, Unstable (comma-separated, case-insensitive).
        status: Optional[str] = None

        # Keep rows whose warning is one of the given values. One or more values, comma-separated, matched case-insensitively.
        warning: Optional[str] = None

    
    @dataclass
    class NaturalFrequenciesRequestBuilderGetRequestConfiguration(RequestConfiguration[NaturalFrequenciesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

