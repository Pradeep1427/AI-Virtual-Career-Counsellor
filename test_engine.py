
from career_engine import recommend_careers

message = input("Describe your interests and skills: ")

recommendations = recommend_careers(message)

if recommendations:
    print("\nYour personalized career suggestions:")

    for item in recommendations:
        print("\nDomain:", item["domain"])
        print("Matched interests:", ", ".join(item["matched_keywords"]))
        print("Why:", item["reason"])
        print("Career options:")

        for career in item["careers"]:
            print("-", career)
else:
    print("\nI need more information about your interests.")
    print("Try describing your skills, favorite subjects, or activities.")
