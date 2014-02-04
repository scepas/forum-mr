#!/usr/local/bin/python

import sys
import csv
from datetime import datetime

# Expected input; tab separated file with enclosing double quotes.
# 19 fields:
#"id"   "title" "tagnames"  "author_id" "body"  "node_type" "parent_id" "abs_parent_id" "added_at"  "score" 
#"state_string" "last_edited_id"    "last_activity_by_id"   "last_activity_at"  "active_revision_id"    "extra" 
#"extra_ref_id" "extra_count"   "marked"

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n\r')

for line in reader:
    #if it's the header, we skip it
    if line[0] == "id":
        continue

    #make sure none of the expected fields is missing
    if (len(line) != 19):
        continue

    author_id = line[3]
    #the date has the format 2012-02-25 08:09:06.787181+00
    added_at = line[8][11:13]
    
    print("{0}\t{1}".format(author_id, added_at))