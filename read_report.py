from glob import glob
import json

import pandas as pd

reports = glob('./reports/*.json')

errors_fh = []
for report in reports:
    get_urls = report.split("_")
    testbrowse = get_urls[-2:-1][0]
    url = "/".join(get_urls[:-2]).replace("./reports/","")
    with open(report, 'r') as fh:
        data = json.load(fh)

    for d in data['incomplete']:
        for node in d['nodes']:
            errors_fh.append([url, testbrowse,d['description'], d['id'], node['failureSummary'], node['html'], node['impact'], "incomplete" ])

    for d in data['violations']:
        for node in d['nodes']:
            errors_fh.append([url, testbrowse,d['description'], d['id'], node['failureSummary'], node['html'], node['impact'], "violations" ])

columns=['url', 'browser', 'description', 'id', 'summary', 'html', 'impact', 'state']
errors_df = pd.DataFrame(errors_fh,columns=columns)
errors_df.to_csv('access_error.csv')