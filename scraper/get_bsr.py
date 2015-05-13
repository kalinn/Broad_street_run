import re
import urllib2
import json

url = "http://results.xacte.com/json/search?eventId=868&subeventId=2034&callback=jQuery183019186991965398192_1431037148770&sEcho=2&iColumns=13&sColumns=&iDisplayStart=10&iDisplayLength=10&mDataProp_0=&mDataProp_1=bib&mDataProp_2=firstname&mDataProp_3=lastname&mDataProp_4=sex&mDataProp_5=age&mDataProp_6=city&mDataProp_7=state&mDataProp_8=country&mDataProp_9=&mDataProp_10=&mDataProp_11=&mDataProp_12=&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=false&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&sSearch_4=&bRegex_4=false&bSearchable_4=true&sSearch_5=&bRegex_5=false&bSearchable_5=true&sSearch_6=&bRegex_6=false&bSearchable_6=true&sSearch_7=&bRegex_7=false&bSearchable_7=true&sSearch_8=&bRegex_8=false&bSearchable_8=true&sSearch_9=&bRegex_9=false&bSearchable_9=true&sSearch_10=&bRegex_10=false&bSearchable_10=true&sSearch_11=&bRegex_11=false&bSearchable_11=false&sSearch_12=&bRegex_12=false&bSearchable_12=false&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=false&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&bSortable_5=true&bSortable_6=true&bSortable_7=true&bSortable_8=true&bSortable_9=false&bSortable_10=false&bSortable_11=false&bSortable_12=false&_=1431037605458"


# string
jquery_content = urllib2.urlopen(url).read()

#print jquery_content

m = re.search('^jQuery[_\d]+\((.+)\);$', jquery_content)
json_str = m.group(1)

json_object = json.loads(json_str)

for runner in json_object['aaData']:
  print runner['firstname'] + "," runner['lastname']
