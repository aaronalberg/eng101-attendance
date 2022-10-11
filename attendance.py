import pandas

date = "DATE"

def combine():
    times = ['3pm', '4pm']
    sections = []
    for time in times:
        section = pandas.read_excel('attendance' + time + '.xlsx')
        del section["Email Address"]
        section.rename(columns={"Illinois Email:":"Email Address"}, inplace=True)
        section['Email Address'] = section['Email Address'].str.lower()
        global date 
        date = pandas.to_datetime(section.iloc[0]["Timestamp"]).date()
        section = section[["Email Address"]]
        sections.append(section)
    
    return pandas.concat(sections)


discussion_mappings = pandas.read_excel('discussion.xlsx')
discussion_mappings['Email Address'] = discussion_mappings['Email Address'].str.lower()



attendance = combine()



# del attendance["Email Address"]
# attendance.rename(columns={"Illinois Email:":"Email Address"}, inplace=True)
# attendance['Email Address'] = attendance['Email Address'].str.lower()
# print(attendance)
# attendance = attendance[["Email Address"]]
discussion_mappings = discussion_mappings[["Email Address", "Name", "Net ID", "Section"]]
merged = attendance.merge(discussion_mappings, on='Email Address', how="inner").set_index('Net ID')
merged.sort_values('Section', inplace=True)
print(date)
merged.to_excel(str(date) + '-eng101-attendance.xlsx')
print(merged)