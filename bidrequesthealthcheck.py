import argparse
import subprocess
import time
import json
import datetime

bidder_id = [
    {"id": 51, "name": "Test DSP"},
    {"id": 2711, "name": "EO Tech Media"},
    {"id": 22, "name": "Exponential (APAC Only)"},
    {"id": 15, "name": "Exponential"},
    {"id": 365, "name": "MobileFuse"},
    {"id": 56, "name": "OneTag"},
    {"id": 148, "name": "Boldwin"},
    {"id": 53, "name": "MadHive"},
    {"id": 181, "name": "Vidstart"},
    {"id": 2655, "name": "StackAdapt"},
    {"id": 2905, "name": "Zemanta"},
    {"id": 3554, "name": "Zemanta oRTB"},
    {"id": 182, "name": "152 Media"},
    {"id": 358, "name": "Admixer DSP"},
    {"id": 608, "name": "Dailyhunt"},
    {"id": 49, "name": "LKQD"},
    {"id": 146, "name": "DistrictM"},
    {"id": 2469, "name": "Smartclip Spain"},
    {"id": 1861, "name": "AcuityAds"},
    {"id": 17, "name": "Id5"},
    {"id": 16, "name": "DV 360 - inactive"},
    {"id": 33, "name": "Beeswax (APAC Traffic ONLY)"},
    {"id": 14, "name": "Torrential"},
    {"id": 21, "name": "Vuble"},
    {"id": 11, "name": "MediaSmart"},
    {"id": 26, "name": "Vpon"},
    {"id": 34, "name": "LoopMe inApp"},
    {"id": 42, "name": "deprecated"},
    {"id": 40, "name": "Get Intent"},
    {"id": 44, "name": "Index Exchange - Mobile Web - Integration"},
    {"id": 31, "name": "SOMO audience"},
    {"id": 37, "name": "LODEO"},
    {"id": 47, "name": "Beachfront Integration"},
    {"id": 38, "name": "OpenX - Deprecated"},
    {"id": 2375, "name": "AppNexus AudioAds"},
    {"id": 7, "name": "AppNexus"},
    {"id": 10, "name": "MediaMath"},
    {"id": 27, "name": "Freewheel"},
    {"id": 2404, "name": "Freewheel oRTB"},
    {"id": 24, "name": "Pubmatic"},
    {"id": 39, "name": "SpotX"},
    {"id": 18, "name": "Adotmob"},
    {"id": 25, "name": "Bidswitch"},
    {"id": 1, "name": "Loopme"},
    {"id": 32, "name": "InMobi"},
    {"id": 23, "name": "OpenX"},
    {"id": 2, "name": "Dynadmic"},
    {"id": 28, "name": "Dynadmic (MENA Traffic Only)"},
    {"id": 1669, "name": "SAPO"},
    {"id": 1003, "name": "Pulsepoint"},
    {"id": 1501, "name": "GumGum Inc"},
    {"id": 1530, "name": "Adyoulike"},
    {"id": 8, "name": "Yahoo DSP"},
    {"id": 3005, "name": "Magnite via Nexx360"},
    {"id": 2728, "name": "Magnite AudioAds"},
    {"id": 36, "name": "Rubicon EU"},
    {"id": 35, "name": "Magnite"},
    {"id": 2443, "name": "Magnite xAPI test bidder"},
    {"id": 50, "name": "Verizon Media SSP"},
    {"id": 43, "name": "Index Exchange"},
    {"id": 1326, "name": "Targetspot"},
    {"id": 1548, "name": "Smartclip Germany"},
    {"id": 1585, "name": "AdsWizz"},
    {"id": 3091, "name": "TripleLift via Nexx360"},
    {"id": 1653, "name": "TripleLift"},
    {"id": 3164, "name": "ShareThrough via Nexx360"},
    {"id": 1532, "name": "ShareThrough"},
    {"id": 2471, "name": "SoundCast"},
    {"id": 1561, "name": "Choueiri Group via Magnite"},
    {"id": 2882, "name": "Choueiri Group via Equativ"},
    {"id": 2467, "name": "Minute Media"},
    {"id": 3229, "name": "Tappx AudioAds"},
    {"id": 2604, "name": "Tappx"},
    {"id": 2640, "name": "adWMG"},
    {"id": 2623, "name": "Hawk AudioAds"},
    {"id": 2358, "name": "Hawk"},
    {"id": 2533, "name": "Blockboard"},
    {"id": 41, "name": "DV 360"},
    {"id": 2764, "name": "DV 360 AudioAds"},
    {"id": 48, "name": "EMX Digital"},
    {"id": 2430, "name": "Bidscube"},
    {"id": 3080, "name": "Adform via Nexx360"},
    {"id": 2606, "name": "Adform"},
    {"id": 2660, "name": "Xapads"},
    {"id": 2376, "name": "The Trade Desk AudioAds"},
    {"id": 19, "name": "The Trade Desk"},
    {"id": 2942, "name": "WebAds Netherlands"},
    {"id": 2607, "name": "WebAds SouthEurope"},
    {"id": 2712, "name": "IQzone"},
    {"id": 2701, "name": "Media.net"},
    {"id": 2726, "name": "Stailamedia"},
    {"id": 2762, "name": "Bulletin"},
    {"id": 2770, "name": "Opera"},
    {"id": 2806, "name": "Eskimi"},
    {"id": 2811, "name": "Alliance Gravity"},
    {"id": 6, "name": "Beeswax"},
    {"id": 46, "name": "RhythmOne"},
    {"id": 2702, "name": "RichAudience"},
    {"id": 2605, "name": "Goldbach Group Germany - Magnite test"},
    {"id": 2423, "name": "Goldbach Group Germany"},
    {"id": 2740, "name": "Audienzz"},
    {"id": 2509, "name": "RTBHouse"},
    {"id": 2808, "name": "Media Square"},
    {"id": 45, "name": "Basis Technologies"},
    {"id": 2651, "name": "BLIINK"},
    {"id": 2659, "name": "Leo Direct"},
    {"id": 2842, "name": "Qortex"},
    {"id": 2957, "name": "OnCore Digital"},
    {"id": 2945, "name": "Vidazoo"},
    {"id": 2867, "name": "Fuel Digital Media"},
    {"id": 3008, "name": "Insticator"},
    {"id": 3048, "name": "Undertone"},
    {"id": 1868, "name": "Amazon"},
    {"id": 470, "name": "Amazon (Bidswitch)"},
    {"id": 2733, "name": "Netpoint"},
    {"id": 9, "name": "TubeMogul"},
    {"id": 2383, "name": "Sonobi"},
    {"id": 3231, "name": "Instreamatic"},
    {"id": 3246, "name": "Instreamatic AudioAds"},
    {"id": 3278, "name": "Smaato, Inc."},
    {"id": 3527, "name": "Yieldmo"},
    {"id": 3221, "name": "Risecodes"},
    {"id": 3408, "name": "VRTCAL Markets Inc"},
    {"id": 1521, "name": "Criteo"},
    {"id": 20, "name": "Appier"},
    {"id": 1323, "name": "Improve Digital"},
    {"id": 2425, "name": "Next Millennium Media"},
    {"id": 3228, "name": "Equativ AudioAds"},
    {"id": 3121, "name": "Equativ LATAM"},
    {"id": 3075, "name": "Equativ via Nexx360"},
    {"id": 1679, "name": "Smart AdServer"},
    {"id": 55, "name": "Smart AdServer integration"},
    {"id": 2487, "name": "Mediakeys Technology"},
    {"id": 1560, "name": "Goldbach Group AG"}
]
bidder_name_to_id = {b['name']: b['id'] for b in bidder_id}
bidder_id_to_name = {b['id']: b['name'] for b in bidder_id}
# --- Bidder list END ---

allPossibleParamList = [
    "id", "imp.id", "imp.tagid", "imp.instl", "imp.secure", "imp.bidfloor", "imp.banner.w", "imp.banner.h", "imp.banner.format", "imp.banner.pos", "imp.video.mimes", "imp.video.minduration", "imp.video.maxduration", "imp.video.placement", "imp.video.plcmt", "imp.video.linearity", "imp.video.protocols", "imp.video.w", "imp.video.h", "imp.video.startdelay", "imp.video.skip", "imp.video.skipmin", "imp.video.skipafter", "imp.video.playbackmethod", "imp.ext.gpid", "imp.ext.third_party_tags", "site.id", "site.name", "site.domain", "site.page", "site.ref", "site.cat", "site.publisher.id", "site.publisher.name", "app.id", "app.name", "app.bundle", "app.storeurl", "app.publisher.id", "app.publisher.name", "device.ua", "device.ip", "device.ipv6", "device.language", "device.dnt", "device.lmt", "device.ifa", "device.didsha1", "device.didmd5", "device.dpidsha1", "device.dpidmd5", "device.macsha1", "device.macmd5", "device.geo.lat", "device.geo.lon", "device.geo.country", "device.geo.region", "device.geo.city", "device.geo.zip", "device.make", "device.model", "device.os", "device.osv", "device.devicetype", "device.connectiontype", "device.carrier", "user.id", "user.buyeruid", "user.yob", "user.gender", "user.geo.lat", "user.geo.lon", "user.geo.country", "user.ext.consent", "user.ext.eids", "regs.coppa", "regs.ext.gdpr", "regs.ext.us_privacy", "source.tid", "source.ext.schain", "tmax", "cur", "at", "test", "bcat", "badv"
]

clusterUrlsMap = {
    "FR":     "https://exchange-prod-onprem-dc3.kube.dm.gg/vlog",
    "EU":     "https://exchange-prod-onprem-ix7.kube.dm.gg/vlog",
    "USEAST": "https://exchange-prod-aws-us-east-2.k8s.dm.gg/vlog",
    "APAC":   "https://exchange-prod-aws-ap-south-1.k8s.dm.gg/vlog",
    "USWEST": "https://exchange-prod-aws-us-west-2.k8s.dm.gg/vlog"
}

def cluster(clr):
    return clusterUrlsMap.get(clr, '')

def executeLeoPyCommand(bidRequestCluster, bidRequestNb):
    cmd = ["leo.py", "bidrequests", "--url", cluster(bidRequestCluster).strip(), "--count", bidRequestNb.strip()]
    try:
        return subprocess.check_output(cmd).decode(), None
    except subprocess.CalledProcessError as e:
        return None, e

def get_nested_value(d, key_path):
    keys = key_path.split('.')
    def extract(obj, keys):
        if not keys:
            return [obj]
        key = keys[0]
        rest = keys[1:]
        results = []
        if isinstance(obj, list):
            for item in obj:
                results.extend(extract(item, keys))
        elif isinstance(obj, dict):
            if key in obj:
                results.extend(extract(obj[key], rest))
        return results
    value = extract(d, keys)
    return value if value else None

def cleanBidRequests(requests):
    bid_requests = []
    for line in requests.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            bid_requests.append(json.loads(line))
        except Exception as e:
            print(f"Failed to parse line as JSON: {line}\nError: {e}")
    return bid_requests

def createAndWriteFile(name, writeStr):
    with open(name, 'w') as file:
        file.write(writeStr)

def filter_bidrequests_with_param(bid_requests, param):
    filtered = []
    for br in bid_requests:
        value = get_nested_value(br, param)
        if value and any(v not in [None, "", [], {}] for v in value):
            filtered.append(br)
    return filtered

def parse_timeout(timeout_str):
    if timeout_str.endswith('m'):
        return int(timeout_str[:-1]) * 60
    elif timeout_str.endswith('s'):
        return int(timeout_str[:-1])
    else:
        return int(timeout_str)

def build_useneed_filename(paramsToSearchFor):
    if paramsToSearchFor:
        param_items = [f"{k.replace('.', '_')}_{v.replace('.', '_')}" for k, v in paramsToSearchFor.items()]
        param_part = "_".join(param_items)
    else:
        param_part = "no_param"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"bidRequests_{param_part}_{timestamp}.txt"

def is_onsite(domain):
    if not isinstance(domain, str):
        return False
    return domain.strip().lower() == "dailymotion.com"

def is_offsite(domain):
    if not isinstance(domain, str):
        return True
    norm = domain.strip().lower()
    return norm != "" and norm != "dailymotion.com"

def main():
    emptyParamsInBidRequest = []
    bidRequestMatchingUserInput = []
    totalBidRequests = 0
    totalBidRequestsFromUserFiltering = 0

    parser = argparse.ArgumentParser(description="BidRequest HealthCheck")
    parser.add_argument('--nbr', default="1", help='Number of requests to parse')
    parser.add_argument('--cluster', default="FR", help='Cluster to use')
    parser.add_argument('--paramName', default="", help='Param(s) name to filter on, comma separated')
    parser.add_argument('--paramValue', default="FR", help='Param value to filter on, comma separated')
    parser.add_argument('--listParams', action='store_true', help='Display all possible params')
    parser.add_argument('--listClusters', action='store_true', help='Display all clusters')
    parser.add_argument('--onsite', choices=['true', 'false'], help='Show stats for onsite (site.domain == dailymotion.com) or offsite')
    # Accept both --Bidder and --bidder (case-insensitive)
    parser.add_argument('--Bidder', '--bidder', default="", help='Bidder name or ID to filter on')
    parser.add_argument('--listBidders', action='store_true', help='Display all bidders')
    parser.add_argument('--filterMode', action='store_true', help='If set, fetch until N requests match filters')
    parser.add_argument('--timeout', default="5m", help='Timeout for fetching requests (e.g., 1m, 30s, default 5m)')

    args = parser.parse_args()

    if args.listParams:
        for param in allPossibleParamList:
            print(param)
        exit(0)

    # Enable filterMode by default if --Bidder is used
    if args.Bidder and not args.filterMode:
        args.filterMode = True

    if args.listClusters:
        for k, v in clusterUrlsMap.items():
            print(f"{k}: {v}")
        exit(0)

    if args.listBidders:
        for name, id_ in bidder_name_to_id.items():
            print(f"{id_}: {name}")
        exit(0)

    bidder_id = None
    if args.Bidder:
        # Accept any bidder ID or name, do not restrict to the static list
        if args.Bidder.isdigit():
            bidder_id = int(args.Bidder)
        else:
            bidder_id = args.Bidder  # Pass as string for leo.py to handle

    # Lowercase all param names and values for case-insensitive matching
    paramNameSlice = [k.lower() for k in args.paramName.split(",")] if args.paramName else []
    paramValueSlice = [v.lower() for v in args.paramValue.split(",")] if args.paramValue else []
    paramsToSearchFor = dict(zip(paramNameSlice, paramValueSlice))

    timeout_seconds = parse_timeout(args.timeout)
    start_time = time.time()

    print("[leo.py] Fetching requests...")

    def get_nested_value_case_insensitive(d, key_path):
        keys = key_path.lower().split('.')
        def extract(obj, keys):
            if not keys:
                return [obj]
            key = keys[0]
            rest = keys[1:]
            results = []
            if isinstance(obj, list):
                for item in obj:
                    results.extend(extract(item, keys))
            elif isinstance(obj, dict):
                # Find the key in obj that matches case-insensitively
                for k in obj:
                    if k.lower() == key:
                        results.extend(extract(obj[k], rest))
            return results
        value = extract(d, keys)
        return value if value else None


    if not args.filterMode:
        # Sample mode: fetch N, then filter
        stdout, err = executeLeoPyCommand(args.cluster, str(args.nbr))
        if err:
            print(f"[Error] leo.py: {err}")
            return

        bid_requests = cleanBidRequests(stdout)
        sampleFileName = f"bidRequestsSample_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        createAndWriteFile(sampleFileName, '\n'.join(json.dumps(br) for br in bid_requests))

        filtered = []
        for br in bid_requests:
            if bidder_id is not None:
                br_id = br.get("id", "")
                if "_" in br_id:
                    try:
                        br_bidder_id = int(br_id.split("_")[-1])
                        if br_bidder_id != bidder_id:
                            continue
                    except ValueError:
                        continue
                else:
                    continue    
            match = True
            tmpEmptyParamsInBidRequest = []
            for k, v in paramsToSearchFor.items():
                values = get_nested_value_case_insensitive(br, k)
                def flatten(l):
                    for el in l:
                        if isinstance(el, list):
                            yield from flatten(el)
                        else:
                            yield el
                flat_values = list(flatten(values)) if values else []
                wanted_values = [x.strip() for x in v.split(",")]
                value_matched = False
                for wanted in wanted_values:
                    if wanted == "null":
                        if not flat_values or all(val in [None, "", [], {}] for val in flat_values):
                            value_matched = True
                            break
                    else:
                        if flat_values and any(str(val).lower() == wanted for val in flat_values):
                            value_matched = True
                            break
                if not value_matched:
                    match = False
                if not flat_values or all(val in [None, "", [], {}] for val in flat_values):
                    tmpEmptyParamsInBidRequest.append(k)
            # --- ONSITE/OFFSITE FILTER ---
            if match and args.onsite:
                site = br.get('site', {})
                domain = site.get('domain') if isinstance(site, dict) else None
                if args.onsite == 'true' and not is_onsite(domain):
                    continue
                if args.onsite == 'false' and not is_offsite(domain):
                    continue
            # --- END ONSITE/OFFSITE FILTER ---
            if match:
                filtered.append(br)
                emptyParamsInBidRequest.extend(tmpEmptyParamsInBidRequest)

        bidRequestMatchingUserInput = [json.dumps(br) for br in filtered]
        totalBidRequestsFromUserFiltering = len(filtered)
        totalBidRequests = len(bid_requests)
        original_requests = bid_requests
    else:
        # Filter mode: fetch until enough results or timeout
        target_nbr = int(args.nbr)
        collected_requests = []
        total_fetched = 0
        all_fetched_requests = []
        while len(collected_requests) < target_nbr:
            if time.time() - start_time > timeout_seconds:
                print(f"[Timeout] {timeout_seconds} seconds reached.")
                break
            fetch_nbr = max(target_nbr * 2, 100)
            stdout, err = executeLeoPyCommand(args.cluster, str(fetch_nbr))
            if err:
                print(f"[Error] leo.py: {err}")
                return

            bid_requests = cleanBidRequests(stdout)
            total_fetched += len(bid_requests)
            all_fetched_requests.extend(bid_requests)

            filtered = []
            for br in bid_requests:
                if bidder_id is not None:
                    br_id = br.get("id", "")
                    if "_" in br_id:
                        try:
                            br_bidder_id = int(br_id.split("_")[-1])
                            if br_bidder_id != bidder_id:
                                continue
                        except ValueError:
                            continue
                    else:
                        continue
                match = True
                tmpEmptyParamsInBidRequest = []
                for k, v in paramsToSearchFor.items():
                    values = get_nested_value_case_insensitive(br, k)
                    def flatten(l):
                        for el in l:
                            if isinstance(el, list):
                                yield from flatten(el)
                            else:
                                yield el
                    flat_values = list(flatten(values)) if values else []
                    wanted_values = [x.strip() for x in v.split(",")]
                    value_matched = False
                    for wanted in wanted_values:
                        if wanted == "null":
                            if not flat_values or all(val in [None, "", [], {}] for val in flat_values):
                                value_matched = True
                                break
                        else:
                            if flat_values and any(str(val).lower() == wanted for val in flat_values):
                                value_matched = True
                                break
                    if not value_matched:
                        match = False
                    if not flat_values or all(val in [None, "", [], {}] for val in flat_values):
                        tmpEmptyParamsInBidRequest.append(k)
                # --- ONSITE/OFFSITE FILTER ---
                if match and args.onsite:
                    site = br.get('site', {})
                    domain = site.get('domain') if isinstance(site, dict) else None
                    if args.onsite == 'true' and not is_onsite(domain):
                        continue
                    if args.onsite == 'false' and not is_offsite(domain):
                        continue
                # --- END ONSITE/OFFSITE FILTER ---
                if match:
                    filtered.append(br)
                    emptyParamsInBidRequest.extend(tmpEmptyParamsInBidRequest)
                    if len(collected_requests) + len(filtered) >= target_nbr:
                        break

            collected_requests.extend(filtered)
            collected_requests = collected_requests[:target_nbr]
            print(f"\r[Progress] {len(collected_requests)}/{target_nbr} matches ({total_fetched} fetched)", end='', flush=True)

        print()
        if 'collected_requests' not in locals():
            collected_requests = []
        bidRequestMatchingUserInput = [json.dumps(br) for br in collected_requests]
        totalBidRequestsFromUserFiltering = len(collected_requests)
        totalBidRequests = total_fetched
        original_requests = all_fetched_requests

    # Empty param stats
    empty_param_counts = {param: emptyParamsInBidRequest.count(param) for param in set(emptyParamsInBidRequest)}
    param_percentage_empty = {
        param: (count / totalBidRequestsFromUserFiltering) * 100 if totalBidRequestsFromUserFiltering else 0
        for param, count in empty_param_counts.items()
    }

    if param_percentage_empty:
        print("\n[Empty params]")
        for k, v in param_percentage_empty.items():
            print(f"  {k}: {v:.2f}% empty")

    bidRequestMatchingUserNeedFromLeoPy = build_useneed_filename(paramsToSearchFor)

    # Clean summary output
    print()
    if not args.filterMode:
        print(f"        File Sample:   {sampleFileName}")
    print(f"        File:  {bidRequestMatchingUserNeedFromLeoPy}")

    if args.filterMode and totalBidRequestsFromUserFiltering:
        print(f"\n        Matches: {totalBidRequestsFromUserFiltering} / {totalBidRequestsFromUserFiltering}  (100%)")
    elif totalBidRequests:
        percent_matched = (totalBidRequestsFromUserFiltering / totalBidRequests) * 100
        print(f"\n          Matches: {totalBidRequestsFromUserFiltering} / {totalBidRequests}  ({percent_matched:.1f}%)")

    # Onsite/offsite stats and debug (always show both percentages)
    requests_to_check = filtered if not args.filterMode else collected_requests

    # Always show imp.video.plcmt == 1 percentage
    plcmt1_count = 0
    for br in requests_to_check:
        values = get_nested_value(br, "imp.video.plcmt")
        if values and any(str(val) == "1" for val in values):
            plcmt1_count += 1
    plcmt1_percent = (plcmt1_count / totalBidRequestsFromUserFiltering * 100) if totalBidRequestsFromUserFiltering else 0
    print(f"        plcmt=1: {plcmt1_count} / {totalBidRequestsFromUserFiltering} ({plcmt1_percent:.1f}%)")

    # Onsite/offsite stats and debug (always show both percentages)
    onsite_count = 0
    offsite_count = 0
    for br in requests_to_check:
        site = br.get('site', {})
        domain = site.get('domain') if isinstance(site, dict) else None
        if is_onsite(domain):
            onsite_count += 1
        if is_offsite(domain):
            offsite_count += 1

    onsite_percent = (onsite_count / totalBidRequestsFromUserFiltering * 100) if totalBidRequestsFromUserFiltering else 0
    offsite_percent = (offsite_count / totalBidRequestsFromUserFiltering * 100) if totalBidRequestsFromUserFiltering else 0

    print(f"        Onsite: {onsite_count} / {totalBidRequestsFromUserFiltering} ({onsite_percent:.1f}%)")
    print(f"        Offsite: {offsite_count} / {totalBidRequestsFromUserFiltering} ({offsite_percent:.1f}%)")

    # Debug print after percentage (optional, only for offsite mode)
    if args.onsite == 'false':
        debug_requests = []
        for br in original_requests:
            site = br.get('site', {})
            domain = site.get('domain') if isinstance(site, dict) else None
            # Only log requests where domain is missing, empty, or not a string
            if not isinstance(domain, str) or domain.strip() == "":
                debug_requests.append(br)
        if debug_requests:
            debug_filename = f"debug_missing_domain_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(debug_filename, "w") as f:
                for br in debug_requests:
                    f.write(json.dumps(br) + "\n")
            print(f"[Debug] {len(debug_requests)} filtered out bid requests with missing or empty domain saved to {debug_filename}")
        else:
            print("[Debug] None found.")

    # Output file (always prompt at the end)
    response = input(f"\nDo you want to save the file(s)? (y/n): ").strip().lower()
    if response == 'y':
        createAndWriteFile(bidRequestMatchingUserNeedFromLeoPy, '\n'.join(bidRequestMatchingUserInput))
        print(f"    Matches:  {bidRequestMatchingUserNeedFromLeoPy}")
    else:
        print("     File creation skipped by user.")

if __name__ == "__main__":
    main()
