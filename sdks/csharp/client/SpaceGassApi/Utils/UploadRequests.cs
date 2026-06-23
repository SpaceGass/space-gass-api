using System.IO;
using Microsoft.Kiota.Abstractions;

namespace SpaceGassApi
{
    /// <summary>
    /// Multipart request body for <c>POST /job/new-from-template</c>. Construct
    /// it from a template file path and pass it straight to the endpoint:
    /// <code>
    /// await client.Job.NewFromTemplate.PostAsync(new NewFromTemplateRequest(path));
    /// </code>
    /// </summary>
    /// <remarks>
    /// A <see cref="MultipartBody"/> with a single <c>template</c> part. The
    /// request builder attaches the request adapter at send time, so none is
    /// needed here.
    /// </remarks>
    public sealed class NewFromTemplateRequest : MultipartBody
    {
        /// <param name="filePath">
        /// Path to the SPACE GASS template (<c>.sgbase</c>/<c>.SG</c>) file to upload.
        /// </param>
        public NewFromTemplateRequest(string filePath) => UploadPart.AddFile(this, "template", filePath);
    }

    /// <summary>
    /// Multipart request body for <c>POST /job/import/txt</c>. Construct it from
    /// a text file path and pass it straight to the endpoint:
    /// <code>
    /// await client.Job.Import.Txt.PostAsync(new ImportTxtRequest(path));
    /// </code>
    /// </summary>
    /// <remarks>
    /// A <see cref="MultipartBody"/> with a single <c>file</c> part. The request
    /// builder attaches the request adapter at send time, so none is needed here.
    /// </remarks>
    public sealed class ImportTxtRequest : MultipartBody
    {
        /// <param name="filePath">Path to the SPACE GASS text (<c>.txt</c>) file to upload.</param>
        public ImportTxtRequest(string filePath) => UploadPart.AddFile(this, "file", filePath);
    }

    // Shared helper: read a file and add it as a single multipart/form-data part.
    internal static class UploadPart
    {
        internal static void AddFile(MultipartBody body, string partName, string filePath)
        {
            if (!File.Exists(filePath))
                throw new FileNotFoundException($"File not found: {filePath}", filePath);

            body.AddOrReplacePart(
                partName,
                "application/octet-stream",
                File.ReadAllBytes(filePath),
                Path.GetFileName(filePath));
        }
    }
}
