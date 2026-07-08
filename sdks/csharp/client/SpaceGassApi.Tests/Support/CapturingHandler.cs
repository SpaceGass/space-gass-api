using System.Net;
using System.Text;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace SpaceGassApi.Tests.Support;

/// <summary>
/// Test double standing in for the SPACE GASS service: records every outgoing
/// request and answers with canned JSON, so tests can assert what actually
/// goes on the wire without a live service.
/// </summary>
public sealed class CapturingHandler : HttpMessageHandler
{
    public sealed record CapturedRequest(HttpMethod Method, Uri Uri, string? ContentType, byte[] Body)
    {
        public string BodyText => Encoding.UTF8.GetString(Body);
    }

    private readonly Func<HttpRequestMessage, HttpResponseMessage> _respond;

    public CapturingHandler(Func<HttpRequestMessage, HttpResponseMessage>? respond = null)
        => _respond = respond ?? (_ => Json("{}"));

    public List<CapturedRequest> Requests { get; } = [];

    public CapturedRequest Last => Requests[^1];

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request, CancellationToken cancellationToken)
    {
        var body = request.Content is null
            ? Array.Empty<byte>()
            : await request.Content.ReadAsByteArrayAsync(cancellationToken);
        Requests.Add(new CapturedRequest(
            request.Method,
            request.RequestUri!,
            request.Content?.Headers.ContentType?.ToString(),
            body));
        return _respond(request);
    }

    public static HttpResponseMessage Json(string json, HttpStatusCode status = HttpStatusCode.OK)
        => new(status) { Content = new StringContent(json, Encoding.UTF8, "application/json") };

    /// <summary>
    /// A <see cref="SpaceGassApiClient"/> whose HTTP traffic is captured by the
    /// returned handler instead of hitting the network.
    /// </summary>
    public static (SpaceGassApiClient Client, CapturingHandler Handler) CreateMockedClient(
        Func<HttpRequestMessage, HttpResponseMessage>? respond = null)
    {
        var handler = new CapturingHandler(respond);
        var adapter = new HttpClientRequestAdapter(
            new AnonymousAuthenticationProvider(),
            httpClient: new HttpClient(handler))
        {
            BaseUrl = "http://localhost:34560/api/v1",
        };
        return (new SpaceGassApiClient(adapter), handler);
    }
}
