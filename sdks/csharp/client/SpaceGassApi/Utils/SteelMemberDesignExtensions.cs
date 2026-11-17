using System;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Kiota.Abstractions.Serialization;
using SpaceGassApi.Job.Design.SteelMember;
using SpaceGassApi.Job.Design.SteelMember.Item;
using SpaceGassApi.Job.Design.SteelMember.Item.Settings;
using SpaceGassApi.Models;

// ---------------------------------------------------------------------
// Hand-maintained smoothing over the steel member design surface
// (/job/design/steel-member/...).
//
// Every design code (AS 4100, NZS 3404, Eurocode 3, AISC, ...) has its own
// settings object. The spec models "one of these" as a oneOf, so Kiota
// wraps them in composed types with one property per code:
//
//   SteelMemberDesignRunCheckRequest.SteelMemberDesignRunCheckRequest_codeSettings
//   SteelMemberDesignRunDesignRequest.SteelMemberDesignRunDesignRequest_codeSettings
//   SettingsRequestBuilder.SettingsPatchRequestBody / SettingsGetResponse / SettingsPatchResponse
//
// All the per-code classes derive from SteelMemberDesignSettingsBase /
// SteelMemberDesignSettingsBaseUpdate, so the helpers below are generic —
// they work for every code, including ones added in later builds:
//
//   var as4100 = client.Job.Design.SteelMember.ForCode(DesignCode.As4100);
//
//   // Pass the code's own settings object straight in
//   await as4100.RunCheck.PostAsync(new SteelMemberDesignRunCheckRequest
//   {
//       CodeSettings = new SteelMemberDesignSettingsAs4100Update { SlendernessRatioCheck = true },
//   });
//
//   // Read / update the stored settings, typed
//   var settings = await as4100.Settings.GetAsync<SteelMemberDesignSettingsAs4100>();
//   settings = await as4100.Settings.PatchAsync<SteelMemberDesignSettingsAs4100>(
//       new SteelMemberDesignSettingsAs4100Update { UseKtFactorForTension = true });
//
// The `code` discriminator never needs setting: the API defaults it to
// the route's design code.
//
// Lives in Utils/ so it survives Kiota's --clean-output.
// ---------------------------------------------------------------------

namespace SpaceGassApi.Models
{
    public partial class SteelMemberDesignRunCheckRequest
    {
        public partial class SteelMemberDesignRunCheckRequest_codeSettings
        {
            /// <summary>Wraps any design code's settings update as the run's code settings.</summary>
            public static implicit operator SteelMemberDesignRunCheckRequest_codeSettings(SteelMemberDesignSettingsBaseUpdate settings)
                => SteelMemberDesignExtensions.Wrap<SteelMemberDesignRunCheckRequest_codeSettings>(settings);
        }
    }

    public partial class SteelMemberDesignRunDesignRequest
    {
        public partial class SteelMemberDesignRunDesignRequest_codeSettings
        {
            /// <summary>Wraps any design code's settings update as the run's code settings.</summary>
            public static implicit operator SteelMemberDesignRunDesignRequest_codeSettings(SteelMemberDesignSettingsBaseUpdate settings)
                => SteelMemberDesignExtensions.Wrap<SteelMemberDesignRunDesignRequest_codeSettings>(settings);
        }
    }
}

namespace SpaceGassApi.Job.Design.SteelMember.Item.Settings
{
    public partial class SettingsRequestBuilder
    {
        public partial class SettingsPatchRequestBody
        {
            /// <summary>Wraps any design code's settings update as a <c>steel-member/{code}/settings</c> PATCH body.</summary>
            public static implicit operator SettingsPatchRequestBody(SteelMemberDesignSettingsBaseUpdate settings)
                => SteelMemberDesignExtensions.Wrap<SettingsPatchRequestBody>(settings);
        }
    }
}

namespace SpaceGassApi
{
    /// <summary>
    /// Helpers for steel member design: pick a design code by enum, and read or
    /// update a code's settings as its own typed object instead of a oneOf wrapper.
    /// </summary>
    public static class SteelMemberDesignExtensions
    {
        /// <summary>
        /// The endpoints for one design code — <c>RunCheck</c>, <c>RunDesign</c>, <c>Settings</c>.
        /// Equivalent to <c>SteelMember["As4100"]</c> but with the <see cref="DesignCode"/> enum.
        /// </summary>
        public static WithCodeItemRequestBuilder ForCode(this SteelMemberRequestBuilder builder, DesignCode code)
            => builder[code.ToString()];

        /// <summary>
        /// Reads the design code's stored settings as its own type, e.g.
        /// <c>Settings.GetAsync&lt;SteelMemberDesignSettingsAs4100&gt;()</c>.
        /// </summary>
        /// <exception cref="InvalidCastException">
        /// The route's design code returned a different settings type than <typeparamref name="TSettings"/>.
        /// </exception>
        public static async Task<TSettings?> GetAsync<TSettings>(
            this SettingsRequestBuilder builder, CancellationToken cancellationToken = default)
            where TSettings : SteelMemberDesignSettingsBase
            => Unwrap<TSettings>(
                await builder.GetAsSettingsGetResponseAsync(cancellationToken: cancellationToken).ConfigureAwait(false));

        /// <summary>
        /// Partially updates the design code's stored settings and returns them as their own type, e.g.
        /// <c>Settings.PatchAsync&lt;SteelMemberDesignSettingsAs4100&gt;(new SteelMemberDesignSettingsAs4100Update { ... })</c>.
        /// </summary>
        public static async Task<TSettings?> PatchAsync<TSettings>(
            this SettingsRequestBuilder builder, SteelMemberDesignSettingsBaseUpdate settings, CancellationToken cancellationToken = default)
            where TSettings : SteelMemberDesignSettingsBase
            => Unwrap<TSettings>(
                await builder.PatchAsSettingsPatchResponseAsync(settings, cancellationToken: cancellationToken).ConfigureAwait(false));

        /// <summary>
        /// Wraps a per-code settings object in a Kiota composed-type wrapper, in the
        /// wrapper property whose type is the object's class.
        /// </summary>
        public static TWrapper Wrap<TWrapper>(SteelMemberDesignSettingsBaseUpdate settings)
            where TWrapper : IComposedTypeWrapper, new()
        {
            if (settings == null) throw new ArgumentNullException(nameof(settings));
            var type = settings.GetType();
            var property = typeof(TWrapper).GetProperties(BindingFlags.Public | BindingFlags.Instance)
                    .FirstOrDefault(p => p.PropertyType == type)
                ?? throw new ArgumentException(
                    $"{type.Name} is not a design code settings type {typeof(TWrapper).Name} accepts. " +
                    "Use the code's own class, e.g. SteelMemberDesignSettingsAs4100Update.", nameof(settings));

            var wrapper = new TWrapper();
            property.SetValue(wrapper, settings);
            return wrapper;
        }

        private static TSettings? Unwrap<TSettings>(IComposedTypeWrapper? wrapper)
            where TSettings : SteelMemberDesignSettingsBase
        {
            if (wrapper == null) return null;
            var value = wrapper.GetType()
                .GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => typeof(SteelMemberDesignSettingsBase).IsAssignableFrom(p.PropertyType))
                .Select(p => p.GetValue(wrapper))
                .FirstOrDefault(v => v != null);

            if (value == null) return null;
            return value as TSettings
                ?? throw new InvalidCastException(
                    $"The design code returned {value.GetType().Name}, not {typeof(TSettings).Name}.");
        }
    }
}
