"""
Hand-maintained helpers for steel member design
(``/job/design/steel-member/...``) — parity with the C# SDK's
``Utils/SteelMemberDesignExtensions.cs``.

Every design code (AS 4100, NZS 3404, Eurocode 3, AISC, ...) has its own
settings object. The spec models "one of these" as a oneOf, so Kiota wraps
them in composed types with one attribute per code:

- ``SteelMemberDesignRunCheckRequest_codeSettings``  (``run-check`` body)
- ``SteelMemberDesignRunDesignRequest_codeSettings`` (``run-design`` body)
- ``SettingsPatchRequestBody`` / ``SettingsGetResponse`` (``{code}/settings``)

All the per-code classes derive from ``SteelMemberDesignSettingsBase`` /
``SteelMemberDesignSettingsBaseUpdate``, so these helpers are generic — they
work for every code, including ones added in later builds::

    from space_gass_api import steel_member
    import space_gass_api.models as models

    as4100 = steel_member.for_code(client, models.DesignCode.As4100)

    # Pass the code's own settings object straight in
    run = await as4100.run_check.post(steel_member.run_check_request(
        code_settings=models.SteelMemberDesignSettingsAs4100Update(slenderness_ratio_check=True)))

    # Read / update the stored settings, typed
    settings = await steel_member.get_settings(as4100, models.SteelMemberDesignSettingsAs4100)
    settings = await steel_member.patch_settings(
        as4100, models.SteelMemberDesignSettingsAs4100Update(use_kt_factor_for_tension=True),
        models.SteelMemberDesignSettingsAs4100)

The ``code`` discriminator never needs setting: the API defaults it to the
route's design code.

Lives outside ``generated/`` so it survives Kiota's ``--clean-output``.
"""

from __future__ import annotations

import dataclasses
import re
from typing import TYPE_CHECKING, Optional, TypeVar, Union, overload

from .generated.job.design.steel_member.item.settings.settings_patch_request_body import (
    SettingsPatchRequestBody,
)
from .generated.job.design.steel_member.item.with_code_item_request_builder import (
    WithCodeItemRequestBuilder,
)
from .generated.models.design_code import DesignCode
from .generated.models.steel_member_design_general_settings_update import (
    SteelMemberDesignGeneralSettingsUpdate,
)
from .generated.models.steel_member_design_iteration_settings_update import (
    SteelMemberDesignIterationSettingsUpdate,
)
from .generated.models.steel_member_design_run_check_request import SteelMemberDesignRunCheckRequest
from .generated.models.steel_member_design_run_check_request_code_settings import (
    SteelMemberDesignRunCheckRequest_codeSettings,
)
from .generated.models.steel_member_design_run_design_request import SteelMemberDesignRunDesignRequest
from .generated.models.steel_member_design_run_design_request_code_settings import (
    SteelMemberDesignRunDesignRequest_codeSettings,
)
from .generated.models.steel_member_design_settings_base import SteelMemberDesignSettingsBase
from .generated.models.steel_member_design_settings_base_update import (
    SteelMemberDesignSettingsBaseUpdate,
)

if TYPE_CHECKING:
    from .space_gass_api_client import SpaceGassApiClient

__all__ = [
    "code_settings_body",
    "for_code",
    "get_settings",
    "patch_settings",
    "run_check_request",
    "run_design_request",
]

TSettings = TypeVar("TSettings", bound=SteelMemberDesignSettingsBase)

_OPTIONAL = re.compile(r"Optional\[(\w+)\]")


def _wrapper_field(wrapper_cls: type, value_cls: type) -> Optional[str]:
    """The wrapper attribute typed as ``Optional[<value class>]`` (Kiota's convention)."""
    for f in dataclasses.fields(wrapper_cls):
        m = _OPTIONAL.fullmatch(str(f.type))
        if m and m.group(1) == value_cls.__name__:
            return f.name
    return None


def _wrap(wrapper_cls, update: Optional[SteelMemberDesignSettingsBaseUpdate]):
    if update is None:
        return None
    attr = _wrapper_field(wrapper_cls, type(update))
    if attr is None:
        raise TypeError(
            f"{type(update).__name__} is not a design code settings type {wrapper_cls.__name__} "
            "accepts. Use the code's own class, e.g. SteelMemberDesignSettingsAs4100Update."
        )
    return wrapper_cls(**{attr: update})


def _unwrap(wrapper) -> Optional[SteelMemberDesignSettingsBase]:
    if wrapper is None:
        return None
    for f in dataclasses.fields(wrapper):
        value = getattr(wrapper, f.name, None)
        if isinstance(value, SteelMemberDesignSettingsBase):
            return value
    return None


def _expect(value: Optional[SteelMemberDesignSettingsBase], expect: Optional[type]):
    if value is not None and expect is not None and not isinstance(value, expect):
        raise TypeError(f"The design code returned {type(value).__name__}, not {expect.__name__}.")
    return value


def for_code(client: "SpaceGassApiClient", code: Union[DesignCode, str]) -> WithCodeItemRequestBuilder:
    """The endpoints for one design code — ``run_check``, ``run_design``, ``settings``.

    Equivalent to ``client.job.design.steel_member.by_code("As4100")`` but takes the
    ``DesignCode`` enum.
    """
    return client.job.design.steel_member.by_code(code.value if isinstance(code, DesignCode) else code)


def run_check_request(
    *,
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None,
    code_settings: Optional[SteelMemberDesignSettingsBaseUpdate] = None,
) -> SteelMemberDesignRunCheckRequest:
    """Body for ``POST /job/design/steel-member/{code}/run-check``.

    ``code_settings`` is the design code's own update object (e.g.
    ``SteelMemberDesignSettingsAs4100Update``); Kiota's wrapper is built for you.
    """
    return SteelMemberDesignRunCheckRequest(
        settings=settings,
        code_settings=_wrap(SteelMemberDesignRunCheckRequest_codeSettings, code_settings),
    )


def run_design_request(
    *,
    update_sections: Optional[bool] = None,
    design_iteration_settings: Optional[SteelMemberDesignIterationSettingsUpdate] = None,
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None,
    code_settings: Optional[SteelMemberDesignSettingsBaseUpdate] = None,
) -> SteelMemberDesignRunDesignRequest:
    """Body for ``POST /job/design/steel-member/{code}/run-design``.

    ``code_settings`` is the design code's own update object (e.g.
    ``SteelMemberDesignSettingsAs4100Update``); Kiota's wrapper is built for you.
    """
    return SteelMemberDesignRunDesignRequest(
        update_sections=update_sections,
        design_iteration_settings=design_iteration_settings,
        settings=settings,
        code_settings=_wrap(SteelMemberDesignRunDesignRequest_codeSettings, code_settings),
    )


def code_settings_body(update: SteelMemberDesignSettingsBaseUpdate) -> SettingsPatchRequestBody:
    """Body for ``PATCH /job/design/steel-member/{code}/settings`` from the code's own update object."""
    return _wrap(SettingsPatchRequestBody, update)


@overload
async def get_settings(code: WithCodeItemRequestBuilder) -> Optional[SteelMemberDesignSettingsBase]: ...
@overload
async def get_settings(code: WithCodeItemRequestBuilder, expect: type[TSettings]) -> Optional[TSettings]: ...


async def get_settings(code, expect=None):
    """Reads a design code's stored settings as its own object.

    ``code`` is ``for_code(client, DesignCode.As4100)``. Pass ``expect`` (e.g.
    ``models.SteelMemberDesignSettingsAs4100``) to get a typed result; a different
    type coming back raises ``TypeError``.
    """
    return _expect(_unwrap(await code.settings.get()), expect)


@overload
async def patch_settings(
    code: WithCodeItemRequestBuilder, update: SteelMemberDesignSettingsBaseUpdate
) -> Optional[SteelMemberDesignSettingsBase]: ...
@overload
async def patch_settings(
    code: WithCodeItemRequestBuilder, update: SteelMemberDesignSettingsBaseUpdate, expect: type[TSettings]
) -> Optional[TSettings]: ...


async def patch_settings(code, update, expect=None):
    """Partially updates a design code's stored settings and returns the updated settings."""
    return _expect(_unwrap(await code.settings.patch(code_settings_body(update))), expect)
