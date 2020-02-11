-- Load URL paths from the file
function load_url_paths_from_file(file)
  lines = {}

  -- Check if the file exists
  -- Resource: http://stackoverflow.com/a/4991602/325852
  local f=io.open(file,"r")
  if f~=nil then
    io.close(f)
  else
    -- Return the empty array
    return lines
  end

  -- If the file exists loop through all its lines
  -- and add them into the lines array
  for line in io.lines(file) do
    if not (line == '') then
      lines[#lines + 1] = line
    end
  end

  return lines
end

-- Load URL paths from file
paths = load_url_paths_from_file("test-small.txt")

-- Check if at least one path was found in the file
if #paths <= 0 then
  print("multiplepaths: No paths found. You have to create a file paths.txt with one path per line")
  os.exit()
end

print("multiplepaths: Found " .. #paths .. " paths")

-- Initialize the paths array iterator
counter = 0

request = function()
  -- Get the next paths array element
  url_path = paths[counter]

  --
  counter = counter + 1

  -- If the counter is longer than the paths array length then reset it
  if counter > #paths then
    counter = 0
  end

  -- Return the request object with the current URL path
  return wrk.format(nil, url_path)
end

done = function(summary, latency, requests)
    file = io.open('result.json', 'w')
    io.output(file)
    io.write(string.format("{\"requests_sec\":%.2f, \"transfer_sec\":\"%.2fMB\", \"avg_latency_ms\":%.2f, \"errors_sum\":%.2f, \"duration\":%.2f,\"requests\":%.2f, \"bytes\":%.2f, \"latency.min\":%.2f, \"latency.max\":%.2f, \"latency.mean\":%.2f, \"latency.stdev\":%.2f}",
            summary.requests/(summary.duration/1000000),
            summary.bytes/(summary.duration*1048576/1000000),
            (latency.mean/1000),
            summary.errors.connect + summary.errors.read + summary.errors.write + summary.errors.status + summary.errors.timeout,
            summary.duration,
            summary.requests,
            summary.bytes,
            latency.min,
            latency.max,
            latency.mean,
            latency.stdev
        )
    )
end