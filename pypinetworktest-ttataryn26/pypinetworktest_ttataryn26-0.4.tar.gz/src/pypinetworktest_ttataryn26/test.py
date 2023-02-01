import feedparser
import datetime
from datetime import timedelta

# d = feedparser.parse("https://pypi.org/rss/packages.xml")
# for entry in d.entries:
#     # dPub = entry.published
#     title = entry.title
#     date = entry.published
#     projectName = title.split("added")[0]
#     with open("tester.txt") as myfile:
#         # myfile.write(projectName + "\n")
#         content=myfile.read()
#         if projectName in content:
#             pass
#         else:
#             with open("newProjects.txt", "a") as myfile:
#                 myfile.write(projectName + ", "+ date + "\n")
#             print("new addition")
#
with open("tester.txt") as myfile:
        # myfile.write(projectName + "\n")
        for project in myfile:
            # project = project.split(",")[0]
            # print(project)
            today = datetime.datetime.now()
            date = project.split(",")[2]
            date = date.replace("GMT","")
            date = date.replace("\n","")
            date = datetime.datetime.strptime(date," %d %b %Y %H:%M:%S " )
            # print(date)
            date = date - timedelta(hours=6)
            diff = today - date
            print("Time of project upload:" + str(date))
            hoursDiff = diff/timedelta(hours=1)
            if hoursDiff < 36:
                print("new package")
