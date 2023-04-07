import pandas

def extractTimeTracker(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        in_timeTracker = False
        times = []
        number = []
        activity = []
        duration = []
        for line in lines:
            if (line.strip() == ''):
                continue
            if (in_timeTracker):
                if (line.strip() == "---"):
                    df = pandas.DataFrame({"Start Time":times, "Number":number, "Activity":activity, "Duration":duration})
                    return(df)
                else:
                    splits = line.split('|')
                    if not (splits[1].strip() in ["Start Time", "----------"]):
                        times.append(splits[1].strip())
                        number.append(splits[2].strip())
                        activity.append(splits[3].strip())
                        duration.append(splits[4].strip())
            if (line.strip() == "### Time Tracker"):
                in_timeTracker = True