__author__ = 'alexcomu'
from sum_bandwith_per_day import MRSumBandwithPerDay, MRSumBandwithPerDayPerSlot
import json, logging

logging.basicConfig(level=logging.INFO)


mr_job = MRSumBandwithPerDayPerSlot()
mr_job.stdin = open('../MY/MY.csv')

result = {}
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        app_name, kbyte_transf = mr_job.parse_output_line(line)
        day, slot = app_name.split("_")
        if not day in result:
            result[day] = {}
        result[day][slot] = kbyte_transf[:-1]

print json.dumps(result)
