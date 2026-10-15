using System.Threading;
using System.Threading.Tasks;
using SpaceGassApi.Job.Design.SteelDesign.Item.Settings;
using SpaceGassApi.Models;

// ---------------------------------------------------------------------
// Hand-maintained smoothing over the steel member design surface.
//
// The per-code settings (AS 4100, NZS 3404, ...) are a oneOf in the spec,
// so Kiota wraps them in composed types — one per place they appear:
//
//   SteelDesignRunCheckRequest.SteelDesignRunCheckRequest_codeSettings
//   SteelDesignRunDesignRequest.SteelDesignRunDesignRequest_codeSettings
//   SettingsRequestBuilder.SettingsPatchRequestBody / SettingsGetResponse
//
// Raw usage means nesting the code's update object inside the wrapper and
// repeating the discriminator (`Code = "As4100"`). The partial classes and
// extensions below let callers pass the code's own settings object
// directly and fill the discriminator in for them:
//
//   await client.Job.Design.SteelDesign["As4100"].RunCheck.PostAsync(
//       new SteelDesignRunCheckRequest
//       {
//           CodeSettings = new SteelMemberDesignSettingsAS4100Update { SlendernessRatioCheck = true },
//       });
//
//   var s = await client.Job.Design.SteelDesign["As4100"].Settings.PatchAs4100Async(
//       new SteelMemberDesignSettingsAS4100Update { UseKtFactorForTension = true });
//
// Lives in Utils/ so it survives Kiota's --clean-output.
// ---------------------------------------------------------------------

namespace SpaceGassApi.Models
{
    public partial class SteelDesignRunCheckRequest
    {
        public partial class SteelDesignRunCheckRequest_codeSettings
        {
            /// <summary>Wraps AS 4100 settings as the run's code settings.</summary>
            public static implicit operator SteelDesignRunCheckRequest_codeSettings(SteelMemberDesignSettingsAS4100Update settings)
                => new() { SteelMemberDesignSettingsAS4100Update = settings.WithCode() };

            /// <summary>Wraps NZS 3404 settings as the run's code settings.</summary>
            public static implicit operator SteelDesignRunCheckRequest_codeSettings(SteelMemberDesignSettingsNZS3404Update settings)
                => new() { SteelMemberDesignSettingsNZS3404Update = settings.WithCode() };
        }
    }

    public partial class SteelDesignRunDesignRequest
    {
        public partial class SteelDesignRunDesignRequest_codeSettings
        {
            /// <summary>Wraps AS 4100 settings as the run's code settings.</summary>
            public static implicit operator SteelDesignRunDesignRequest_codeSettings(SteelMemberDesignSettingsAS4100Update settings)
                => new() { SteelMemberDesignSettingsAS4100Update = settings.WithCode() };

            /// <summary>Wraps NZS 3404 settings as the run's code settings.</summary>
            public static implicit operator SteelDesignRunDesignRequest_codeSettings(SteelMemberDesignSettingsNZS3404Update settings)
                => new() { SteelMemberDesignSettingsNZS3404Update = settings.WithCode() };
        }
    }
}

namespace SpaceGassApi.Job.Design.SteelDesign.Item.Settings
{
    public partial class SettingsRequestBuilder
    {
        public partial class SettingsPatchRequestBody
        {
            /// <summary>Wraps AS 4100 settings as a <c>steel-design/{code}/settings</c> PATCH body.</summary>
            public static implicit operator SettingsPatchRequestBody(SteelMemberDesignSettingsAS4100Update settings)
                => new() { SteelMemberDesignSettingsAS4100Update = settings.WithCode() };

            /// <summary>Wraps NZS 3404 settings as a <c>steel-design/{code}/settings</c> PATCH body.</summary>
            public static implicit operator SettingsPatchRequestBody(SteelMemberDesignSettingsNZS3404Update settings)
                => new() { SteelMemberDesignSettingsNZS3404Update = settings.WithCode() };
        }
    }
}

namespace SpaceGassApi
{
    /// <summary>
    /// Typed accessors for the per-design-code settings endpoint
    /// <c>GET/PATCH /job/design/steel-design/{code}/settings</c>, so callers
    /// get the code's own settings object back instead of a oneOf wrapper.
    /// </summary>
    public static class SteelDesignExtensions
    {
        /// <summary>The route segment for AS 4100 — <c>client.Job.Design.SteelDesign[As4100]</c>.</summary>
        public const string As4100 = "As4100";

        /// <summary>The route segment for NZS 3404 — <c>client.Job.Design.SteelDesign[Nzs3404]</c>.</summary>
        public const string Nzs3404 = "Nzs3404";

        /// <summary>Reads the AS 4100 settings. Use on <c>SteelDesign[SteelDesignExtensions.As4100].Settings</c>.</summary>
        public static async Task<SteelMemberDesignSettingsAS4100?> GetAs4100Async(
            this SettingsRequestBuilder builder, CancellationToken cancellationToken = default)
            => (await builder.GetAsSettingsGetResponseAsync(cancellationToken: cancellationToken).ConfigureAwait(false))
                ?.SteelMemberDesignSettingsAS4100;

        /// <summary>Reads the NZS 3404 settings. Use on <c>SteelDesign[SteelDesignExtensions.Nzs3404].Settings</c>.</summary>
        public static async Task<SteelMemberDesignSettingsNZS3404?> GetNzs3404Async(
            this SettingsRequestBuilder builder, CancellationToken cancellationToken = default)
            => (await builder.GetAsSettingsGetResponseAsync(cancellationToken: cancellationToken).ConfigureAwait(false))
                ?.SteelMemberDesignSettingsNZS3404;

        /// <summary>Partially updates the AS 4100 settings and returns the updated settings.</summary>
        public static async Task<SteelMemberDesignSettingsAS4100?> PatchAs4100Async(
            this SettingsRequestBuilder builder, SteelMemberDesignSettingsAS4100Update settings, CancellationToken cancellationToken = default)
            => (await builder.PatchAsSettingsPatchResponseAsync(settings, cancellationToken: cancellationToken).ConfigureAwait(false))
                ?.SteelMemberDesignSettingsAS4100;

        /// <summary>Partially updates the NZS 3404 settings and returns the updated settings.</summary>
        public static async Task<SteelMemberDesignSettingsNZS3404?> PatchNzs3404Async(
            this SettingsRequestBuilder builder, SteelMemberDesignSettingsNZS3404Update settings, CancellationToken cancellationToken = default)
            => (await builder.PatchAsSettingsPatchResponseAsync(settings, cancellationToken: cancellationToken).ConfigureAwait(false))
                ?.SteelMemberDesignSettingsNZS3404;

        // The discriminator is fixed per type, so fill it in when the caller didn't.
        internal static SteelMemberDesignSettingsAS4100Update WithCode(this SteelMemberDesignSettingsAS4100Update settings)
        {
            settings.Code ??= As4100;
            return settings;
        }

        internal static SteelMemberDesignSettingsNZS3404Update WithCode(this SteelMemberDesignSettingsNZS3404Update settings)
        {
            settings.Code ??= Nzs3404;
            return settings;
        }
    }
}
