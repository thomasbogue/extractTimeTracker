import extractTimeTrackerLib
import pandas
import sys
import re

if len(sys.argv) == 1:
    print("Usage:")
    print(f"python {sys.argv[0]} LessonPlan.md")
    exit()

for infilename in sys.argv[1:]:
    tracker = extractTimeTrackerLib.extractTimeTracker(infilename)
    outfilename = re.sub(r'.md$', '.xlsx', infilename)
    tracker.to_excel(outfilename, sheet_name="Time Tracker")
    #tracker.to_csv(outfilename)
