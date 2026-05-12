using System.Net.Http;
using Microsoft.Kiota.Abstractions;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;
using Microsoft.Kiota.Http.HttpClientLibrary.Middleware.Options;

namespace SpaceGassApi;

/// <summary>
/// SPACE GASS API client.
/// Extends the Kiota-generated <see cref="BaseSpaceGassApiClient"/> with a
/// convenience factory. Use <see cref="CreateClient"/> to get a fully
/// configured instance.
/// </summary>
/// <remarks>
/// This file lives outside the <c>Generated/</c> folder and is safe
/// from <c>--clean-output</c> during Kiota regeneration.
/// </remarks>
public class SpaceGassApiClient : BaseSpaceGassApiClient
{
    private const string ApiPath = "/api/v1";

    /// <summary>
    /// Default base URL for the SPACE GASS API running locally.
    /// </summary>
    public const string DefaultBaseUrl = "http://localhost:34560";

    /// <summary>
    /// Initialises a new <see cref="SpaceGassApiClient"/>.
    /// </summary>
    /// <param name="requestAdapter">The request adapter to use.</param>
    public SpaceGassApiClient(IRequestAdapter requestAdapter)
        : base(requestAdapter)
    {
    }

    /// <summary>
    /// Create a <see cref="SpaceGassApiClient"/> with default settings.
    /// </summary>
    /// <param name="baseUrl">
    /// Root URL of the SPACE GASS API (without <c>/api/v1</c>).
    /// Defaults to <c>http://localhost:34560</c>.
    /// Use <c>https://</c> for HTTPS connections.
    /// </param>
    /// <returns>A configured client ready to make API calls.</returns>
    /// <remarks>
    /// The local SPACE GASS API may serve HTTPS with a self-signed
    /// certificate, so SSL verification is disabled by default.
    /// HTTP-to-HTTPS redirects are also allowed so either scheme
    /// works for the same port.
    /// </remarks>
    public static SpaceGassApiClient CreateClient(string baseUrl = DefaultBaseUrl)
    {
        // Accept self-signed certificates from the local API.
        var handler = new HttpClientHandler
        {
            ServerCertificateCustomValidationCallback =
                HttpClientHandler.DangerousAcceptAnyServerCertificateValidator,
        };

        // Allow HTTP ↔ HTTPS redirects (the local API may redirect).
        var httpClient = KiotaClientFactory.Create(
            handler,
            [
                new RedirectHandlerOption
                {
                    AllowRedirectOnSchemeChange = true,
                },
            ]);

        var adapter = new HttpClientRequestAdapter(
            new AnonymousAuthenticationProvider(),
            httpClient: httpClient);
        adapter.BaseUrl = baseUrl.TrimEnd('/') + ApiPath;
        return new SpaceGassApiClient(adapter);
    }
}
