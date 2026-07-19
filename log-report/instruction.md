Your task is to analyze the access log located at /app/access.log.

Success criteria:

1. Read every entry in /app/access.log.

2. Generate a file named /app/report.json.

3. The report must be valid JSON.

4. The report must contain exactly these fields:
   - total_requests
   - unique_ips
   - top_path

5. The values must accurately summarize the contents of the access log:
   - total_requests = 6
   - unique_ips = 3
   - top_path = "/index.html"