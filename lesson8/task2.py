import re


with open("log.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    IP_GET_PARSER = re.compile(r'[\S]+')
    DATETIME_GET_PARSER = re.compile(r"\B\[([^\]]+)\]\B")
    REQUEST_TYPE_PARSER = re.compile(r'\B"([A-Z]+)')
    REQUEST_RESOURCES_PARSER = re.compile(r'\B\/(?:[^\"]+)')
    RESPONSE_CODE_SIZE_PARSER = re.compile(r'(?<!\S)[0-9]+(?!\S)')
    while line:
        remote_addr = re.search(IP_GET_PARSER, line).group(0)
        request_datetime = re.search(DATETIME_GET_PARSER, line).group(1)
        request_type = re.search(REQUEST_TYPE_PARSER, line).group(1)
        requested_resource = re.search(REQUEST_RESOURCES_PARSER, line).group(0)
        response_code = re.findall(RESPONSE_CODE_SIZE_PARSER, line)[0]
        response_size = re.findall(RESPONSE_CODE_SIZE_PARSER, line)[1]
        parsed_raw = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
        print(parsed_raw)
        line = f.readline()

