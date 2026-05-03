leads=[{"name":"ramees","days_since_enquiry":5,"budget_mentioned":True}
       ,{"name":"suresh","days_since_enquiry":10,"budget_mentioned":False}
         ,{"name":"Malabar IT solutions","days_since_enquiry":15,"budget_mentioned":True}
            ,{"name":" ","days_since_enquiry":20,"budget_mentioned":False}
                ,{"days_since_enquiry":25,"budget_mentioned":True}
                    ,{"name":"suresh","days_since_enquiry":30,"budget_mentioned":False}]

import logging
logging.basicConfig(filename='app.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
def score_lead(lead):
    try:   
        if lead["name"].strip()=="":
            logging.warning("DATA ERROR:Skipping the lead with empty name")
            return "DATA ERROR:Skipping the lead with empty name"
        
        days=lead["days_since_enquiry"]  
        budget=lead["budget_mentioned"]

        if days<=7 and budget==True:
            status="Hot"
        elif days<=15:
            status="Warm"
        else:
            status="cold"    
        logging.info(f"processed | {lead["name"]}:{status}")
        return(f"processed | {lead["name"]}:{status}")
    except KeyError:
        logging.error(f"CRITICAL ERROR:A required data key is missing from the lead.")
        return(f"CRITICAL ERROR:A required data key is missing from the lead.")
    except TypeError:
        logging.error(f"TYPE ERROR:Data for {lead.get("name","Unknown")} is malformed.")
        return(f"TYPE ERROR:Data for {lead.get("name","Unknown")} is malformed.")

for person in leads:
    result=score_lead(person)
    print(result)


                           

    
    


        