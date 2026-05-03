leads=[{"name":"ramees","days_since_enquiry":5,"budget_mentioned":True}
       ,{"name":"suresh","days_since_enquiry":10,"budget_mentioned":False}
         ,{"name":"Malabar IT solutions","days_since_enquiry":15,"budget_mentioned":True}
            ,{"name":" ","days_since_enquiry":20,"budget_mentioned":False}
                ,{"name":"arun","days_since_enquiry":25,"budget_mentioned":True}
                    ,{"name":"suresh","days_since_enquiry":30,"budget_mentioned":False}]

for lead in leads:
    if lead["name"].strip()=="":
        print("DATA ERROR:Skipping the lead with empty name")
        continue

    days=lead["days_since_enquiry"]
    budget=lead["budget_mentioned"]

    if days<=7 and budget==True:
        status="Hot"
    else:
        status="Cold"
    print(f"processed:{lead["name"]} | status:{status}")        