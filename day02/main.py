file = open("day02/data.txt")
data = file.read()

reports = data.split("\n")
safe_report_count = len(reports)

# part 1
for report in reports:
    report = report.split()
    prev = int(report[0])
    difference_sum = 0
    absolute_difference_sum = 0
    for i in range(1,len(report)):
        current = int(report[i])
        difference = current - prev
        absolute_difference = abs(difference)
        if  absolute_difference > 3 or absolute_difference < 1:
            safe_report_count -= 1
            print(f"too big of a difference: {absolute_difference}")
            break
        
        difference_sum += difference
        absolute_difference_sum += absolute_difference
        if abs(difference_sum) != absolute_difference_sum:
            safe_report_count -= 1
            print("ordering changed")
            break

        prev = current
print(f"Number of safe reports: {safe_report_count}")

#part 2
def checkReport(report):
    prev = int(report[0])
    difference_sum = 0
    absolute_difference_sum = 0
    for i in range(1,len(report)):
        current = int(report[i])
        difference = current - prev
        absolute_difference = abs(difference)
        if  absolute_difference > 3 or absolute_difference < 1:
            return False
        
        difference_sum += difference
        absolute_difference_sum += absolute_difference
        if abs(difference_sum) != absolute_difference_sum:
            return False

        prev = current

    return True

safe_report_count = len(reports)
for report in reports:
    report = report.split()

    if checkReport(report):
        break
    
    unsafe_report = True
    for i in range(len(report)):
        modifed_report = list(report)
        modifed_report.pop(i)

        if checkReport(modifed_report):
            unsafe_report = False
    
    if unsafe_report:
        safe_report_count -= 1


print(f"Number of safe reports: {safe_report_count}")