# log_parser
HTTP Python log parser

Group the logged requests by IP address or HTTP status code (selected by user).
Calculate one of the following (selected by user) for each group:
- Request count
- Request count percentage of all logged requests
- Total number of bytes transferred
- Print the results in descending order.
Note: order the results by values described in (2), not by IP address or HTTP code.
- Optionally limit the number of rows printed (specied by user)
