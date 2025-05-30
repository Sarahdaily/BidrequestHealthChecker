# BidrequestHealthChecker
---

## Overview

The **BidRequest HealthCheck** tool is a Python script for analyzing, filtering, and summarizing OpenRTB bid requests. It is designed for ad-tech engineers, QA, and data analysts who need to inspect, filter, and validate bid request data from Dailymotion’s exchange clusters.

## Prerequisites
Before using this script, make sure you have the following prerequisites:

- **Python 3.7+ is required.**  
  You need to have Python installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)
- **leo.py must be installed and available in your PATH**   
  You need to have access and have installed leo.py on your system. You can download it from the repository [leo.py documentation](https://github.com/dailymotion/leo-exchange/tree/master/tools/leo-py)
- Make sure you have access to the clusters you want to query (VPN, credentials, etc.).

Here’s a **complete, copy-paste-ready Wiki Installation section** focused only on installing the tool and its Python dependencies (not Python or leo.py).  
This is suitable for a GitHub Wiki page or a `README.md`/`INSTALL.md` file.

---

# Installation

## 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/your-org/bidRequestHealthCheck.git
cd bidRequestHealthCheck
```

## 2. (Recommended) Create a Virtual Environment

It’s best practice to use a Python virtual environment to avoid dependency conflicts:

```sh
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Python Dependencies

Install all required Python packages using the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

If you do not have `pip` installed, you may need to install it first.

## 4. (Optional) Check Your Installation

You can check that the tool is installed and dependencies are available by running:

```sh
python3 bidrequesthealthcheck.py --help
```

You should see the tool’s help message with available options.

---

## Notes



---

## Next Steps

- See the Usage section for example commands and advanced options.
- For troubleshooting or more details, refer to the main documentation or contact the maintainers.

---

**You are now ready to use the BidRequest HealthCheck tool!**

---
## Features

- **Fetch bid requests** from various Dailymotion clusters using `leo.py`.
- **Flexible filtering** by parameter name/value, required parameters, and bidder.
- **Onsite/offsite filtering** (`site.domain == dailymotion.com` or not).
- **Filter mode**: fetch until N requests match your criteria.
- **Summary statistics**: always shows the percentage of requests with `imp.video.plcmt=1`, as well as onsite/offsite splits.
- **Debug output** for offsite/onsite domain issues.
- **Interactive file saving** for filtered results.
- **Lists** all possible params, clusters, and bidders.
- **Supports multiple parameters and values** for advanced filtering.
- **Timeout control** for long-running fetches.
- **Automatic filter mode** when using `--Bidder`.

---

## Command-Line Parameters

| Parameter         | Description                                                                                          | Example                                      |
|-------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `--nbr`           | Number of bid requests to fetch or match.                                                            | `--nbr 1000`                                 |
| `--cluster`       | Cluster to fetch from.                                                                               | `--cluster FR`                               |
| `--paramName`     | Parameter(s) to filter on (comma-separated, dot notation supported).                                 | `--paramName imp.video.plcmt,site.domain`    |
| `--paramValue`    | Value(s) for the parameters above (comma-separated, order matters).                                  | `--paramValue 1,dailymotion.com`             |
| `--requiredParam` | Only keep requests that have this parameter (dot notation).                                          | `--requiredParam imp.video.mimes`            |
| `--Bidder`        | Filter by bidder name or ID. **Automatically enables filter mode.**                                  | `--Bidder 35` or `--Bidder "Magnite"`        |
| `--onsite`        | Filter for onsite (`true`) or offsite (`false`) requests.                                            | `--onsite true`                              |
| `--filterMode`    | Fetch until N requests match your filters (default if `--Bidder` is used).                           | `--filterMode`                               |
| `--timeout`       | Timeout for fetching requests (e.g., `1m`, `30s`, default `5m`).                                     | `--timeout 2m`                               |
| `--listParams`    | List all possible parameters you can filter on.                                                      | `--listParams`                               |
| `--listClusters`  | List all available clusters.                                                                         | `--listClusters`                             |
| `--listBidders`   | List all supported bidders.                                                                          | `--listBidders`                              |

---

## Output

- **Summary statistics** always include:
  - Number and percentage of requests with `imp.video.plcmt=1`
  - Onsite and offsite request counts and percentages
  - Empty parameter stats (if any)
  - File names for sample and filtered results

- **Debug output**  
  If `--onsite false` is used, prints details for requests that are not offsite.

- **Interactive file saving**  
  At the end, you are prompted to save the filtered results.

---

## Filtering Logic

- **Bidder filtering**: If `--Bidder` is used, only requests for that bidder are collected. Filter mode is enabled automatically.
- **Onsite/offsite filtering**: If `--onsite` is set, only matching requests are collected.
- **Parameter filtering**: Only requests matching all specified parameters/values are collected.
- **Multiple parameters/values**: You can filter on several parameters at once, e.g.:
  ```
  --paramName imp.video.plcmt,site.domain --paramValue 1,dailymotion.com
  ```
- **Filter mode**: The script fetches batches until enough requests match your filters or the timeout is reached.

---

## Example Workflows

### 1. **Find 1000 offsite requests for a specific bidder with `imp.video.plcmt=1`:**
```sh
python bidrequesthealthcheck.py --nbr 1000 --paramName imp.video.plcmt --paramValue 1 --onsite false --Bidder 35
```

### 2. **Show summary for 100 random requests:**
```sh
python bidrequesthealthcheck.py --nbr 100
```

### 3. **Filter for requests with a required parameter:**
```sh
python bidrequesthealthcheck.py --nbr 100 --requiredParam imp.video.mimes
```

### 4. **Filter for multiple parameters and values:**
```sh
python bidrequesthealthcheck.py --nbr 100 --paramName imp.video.plcmt,site.domain --paramValue 1,dailymotion.com
```

### 5. **List all supported bidders:**
```sh
python bidrequesthealthcheck.py --listBidders
```

### 6. **Fetch only requests for a specific bidder (auto filter mode):**
```sh
python bidrequesthealthcheck.py --nbr 50 --Bidder "Magnite"
```

### 7. **Set a custom timeout for fetching:**
```sh
python bidrequesthealthcheck.py --nbr 1000 --Bidder 35 --timeout 10m
```

---

## Advanced Usage

- **Combine filters:**  
  You can combine `--Bidder`, `--onsite`, `--paramName`, `--paramValue`, and `--requiredParam` for very precise filtering.
- **Inspect empty parameters:**  
  The tool will show you which parameters are empty and their percentage in the filtered set.
- **Debug offsite domains:**  
  When using `--onsite false`, the tool will print debug info for requests that are not truly offsite.
- **Interactive file saving:**  
  You can choose whether to save the filtered results at the end of each run.

---

## Parameter Reference

- **All supported parameters:**  
  Run `python bidrequesthealthcheck.py --listParams` to see the full list of filterable parameters (including nested OpenRTB fields).
- **All supported clusters:**  
  Run `python bidrequesthealthcheck.py --listClusters` to see available clusters.
- **All supported bidders:**  
  Run `python bidrequesthealthcheck.py --listBidders` to see all bidder names and IDs.

---

## Notes

- **Domain normalization:** Onsite/offsite checks are robust to whitespace and case.
- **Filter mode** is always enabled if you use `--Bidder`,`--onsite true/false` even if you don’t specify `--filterMode`.
- **imp.video.plcmt=1 percentage** is always shown, regardless of filters.
- **Timeouts:** If your filters are too strict, you may hit the timeout before collecting enough requests.
- **File output:** Output files are timestamped and named according to your filters for easy tracking.

---

## Troubleshooting

- If you see `[Timeout] ... seconds reached.`, try increasing `--timeout` or relaxing your filters.
- If you see `[Error] leo.py: ...`, check your cluster URL or network.
- If you get no matches, try removing or adjusting filters.

---

## See Also

- [leo.py documentation](https://github.com/dailymotion/leo-exchange/tree/master/tools/leo-py) (for the underlying fetch command)
- [OpenRTB Specification](https://iabtechlab.com/standards/openrtb/)

---

*For further details, see the code comments or contact the maintainers.*
