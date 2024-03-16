import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "dW8jO2fotN4UmealjrourFr5ay06RWLsdI471u0MXePiFNvBq9RwGqV7l23Nyb4ZRtmrUjpiCvNNBsswnGJypA=="
org = "Threat-detection"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="Threat-detection"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(20):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="Threat-detection", record=point)
  time.sleep(1) # separate points by 1 second