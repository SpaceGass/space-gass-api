using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SpaceGassApi.Utils
{
    /// <summary>
    /// Extension methods for converting between integer ID collections and
    /// the compact SPACE GASS filter string format (e.g. "1,3-7,10").
    /// </summary>
    public static class ListUtilsExtensions
    {
        /// <summary>
        /// Converts a collection of integer IDs to a compact filter string.
        /// Non-positive values are ignored. The output is sorted and deduplicated.
        /// Runs of 3+ consecutive values collapse to ranges (e.g. "3-7").
        /// </summary>
        public static string ToFilterString(this IEnumerable<int> ids)
        {
            if (ids == null)
                return string.Empty;

            var sorted = ids.Where(id => id > 0).Distinct().OrderBy(id => id).ToList();
            if (sorted.Count == 0)
                return string.Empty;

            var sb = new StringBuilder();
            int runStart = sorted[0];
            int runEnd = sorted[0];

            for (int i = 1; i < sorted.Count; i++)
            {
                if (sorted[i] == runEnd + 1)
                {
                    runEnd = sorted[i];
                }
                else
                {
                    AppendRun(sb, runStart, runEnd);
                    runStart = sorted[i];
                    runEnd = sorted[i];
                }
            }

            AppendRun(sb, runStart, runEnd);
            return sb.ToString();
        }

        /// <summary>
        /// Parses a SPACE GASS filter string into a sorted, distinct array of positive integers.
        /// Ranges like "3-7" expand to all values in the inclusive range.
        /// Reversed ranges like "7-3" are normalised.
        /// Whitespace around tokens is tolerated.
        /// </summary>
        /// <exception cref="FormatException">
        /// Thrown when the string contains non-numeric characters, non-positive values,
        /// or the keyword "all".
        /// </exception>
        public static int[] ToIdArray(this string filter)
        {
            if (string.IsNullOrWhiteSpace(filter))
                return Array.Empty<int>();

            var result = new List<int>();
            var tokens = filter.Split(',');

            foreach (var raw in tokens)
            {
                var token = raw.Trim();
                if (token.Length == 0)
                    continue;

                if (token.Equals("all", StringComparison.OrdinalIgnoreCase))
                    throw new FormatException("The keyword \"all\" is not a valid ID list.");

                var dashIndex = token.IndexOf('-');
                if (dashIndex > 0)
                {
                    var startStr = token.Substring(0, dashIndex).Trim();
                    var endStr = token.Substring(dashIndex + 1).Trim();

                    if (!int.TryParse(startStr, out int start) || !int.TryParse(endStr, out int end))
                        throw new FormatException($"Invalid token in ID list: \"{token}\".");

                    int lo = Math.Min(start, end);
                    int hi = Math.Max(start, end);
                    for (int v = lo; v <= hi; v++)
                        result.Add(v);
                }
                else
                {
                    if (!int.TryParse(token, out int value))
                        throw new FormatException($"Invalid token in ID list: \"{token}\".");

                    result.Add(value);
                }
            }

            var sorted = result.Distinct().OrderBy(id => id).ToArray();

            foreach (var id in sorted)
            {
                if (id <= 0)
                    throw new FormatException($"Non-positive ID \"{id}\" is not valid.");
            }

            return sorted;
        }

        /// <summary>
        /// Convenience wrapper that returns a <see cref="List{T}"/> instead of an array.
        /// </summary>
        public static List<int> ToIdList(this string filter)
        {
            return filter.ToIdArray().ToList();
        }

        private static void AppendRun(StringBuilder sb, int start, int end)
        {
            if (sb.Length > 0)
                sb.Append(',');

            if (end - start >= 2)
                sb.Append(start).Append('-').Append(end);
            else if (end - start == 1)
                sb.Append(start).Append(',').Append(end);
            else
                sb.Append(start);
        }
    }
}
