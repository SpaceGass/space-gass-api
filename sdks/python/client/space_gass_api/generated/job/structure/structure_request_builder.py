from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .materials.materials_request_builder import MaterialsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .member_offsets.member_offsets_request_builder import MemberOffsetsRequestBuilder
    from .nodes.nodes_request_builder import NodesRequestBuilder
    from .node_constraints.node_constraints_request_builder import NodeConstraintsRequestBuilder
    from .node_restraints.node_restraints_request_builder import NodeRestraintsRequestBuilder
    from .plates.plates_request_builder import PlatesRequestBuilder
    from .plate_cuts.plate_cuts_request_builder import PlateCutsRequestBuilder
    from .plate_strips.plate_strips_request_builder import PlateStripsRequestBuilder
    from .sections.sections_request_builder import SectionsRequestBuilder

class StructureRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StructureRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure", path_parameters)
    
    @property
    def materials(self) -> MaterialsRequestBuilder:
        """
        The materials property
        """
        from .materials.materials_request_builder import MaterialsRequestBuilder

        return MaterialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_offsets(self) -> MemberOffsetsRequestBuilder:
        """
        The memberOffsets property
        """
        from .member_offsets.member_offsets_request_builder import MemberOffsetsRequestBuilder

        return MemberOffsetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        The members property
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_constraints(self) -> NodeConstraintsRequestBuilder:
        """
        The nodeConstraints property
        """
        from .node_constraints.node_constraints_request_builder import NodeConstraintsRequestBuilder

        return NodeConstraintsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_restraints(self) -> NodeRestraintsRequestBuilder:
        """
        The nodeRestraints property
        """
        from .node_restraints.node_restraints_request_builder import NodeRestraintsRequestBuilder

        return NodeRestraintsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nodes(self) -> NodesRequestBuilder:
        """
        The nodes property
        """
        from .nodes.nodes_request_builder import NodesRequestBuilder

        return NodesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_cuts(self) -> PlateCutsRequestBuilder:
        """
        The plateCuts property
        """
        from .plate_cuts.plate_cuts_request_builder import PlateCutsRequestBuilder

        return PlateCutsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_strips(self) -> PlateStripsRequestBuilder:
        """
        The plateStrips property
        """
        from .plate_strips.plate_strips_request_builder import PlateStripsRequestBuilder

        return PlateStripsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plates(self) -> PlatesRequestBuilder:
        """
        The plates property
        """
        from .plates.plates_request_builder import PlatesRequestBuilder

        return PlatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> SectionsRequestBuilder:
        """
        The sections property
        """
        from .sections.sections_request_builder import SectionsRequestBuilder

        return SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    

