import numpy as np
import pandas as pd
import math
from collections import OrderedDict

offer_customer= pd.read_csv("offer_customer.csv", encoding = "ISO-8859-1")

offer_customer.index = offer_customer['customerId']
all_offers = np.array(offer_customer['offerId'].drop_duplicates())

sorted_offers =[item for item in sorted(all_offers)]
offer_list=[]
labels = ['offer_key', '1st','2nd','3rd','4th','5th']

for offer in sorted_offers:
    offerId_key = offer
    # array contains all the users that have rated, explored offerId_key
    offer1_users = np.array(offer_customer.loc[offer_customer['offerId']==offerId_key]['customerId'].drop_duplicates())
    n = len(offer1_users)
    dct = OrderedDict()
    for offer2 in all_offers:
        if offer2 != offerId_key:
            # creating array of users (those who has rated or explored offer2) for other offers
            offer_users = np.array(offer_customer.loc[offer_customer['offerId']==offer2]['customerId'].drop_duplicates())
            # getting users that are common in both offer and offer2
            common_users = np.intersect1d(offer1_users,offer_users)
            total_common_users = len(common_users)
            #  calculating cosine similarity between offer and offer2 (item-to-item-collaborative_filtering)
            cosine_similarity = total_common_users/(math.sqrt(n)*math.sqrt(len(offer1_users)))
            # condition to stop irrevelent recommandations (i.e. no similarity)
            if cosine_similarity > 0.0:
                dct[offer2] = cosine_similarity

    lst = [offer for offer, cosine_similarity in sorted(dct.items(), key = lambda x:x[1], reverse=True)]
    # If you want to generate the table of similar items(offers) with the offerId with its cosine_similarity to the offerId_key
    #  comment the above line and uncomment the underneath line
    # lst = [(offer,cosine_similarity) for offer,cosine_similarity in sorted(dct.items(), key = lambda x:x[1], reverse=True)]
    lst.insert(0,offerId_key)
    offer_list.append(tuple(lst[:6]))
similar_item_table_test = pd.DataFrame(offer_list, columns=labels)
# creating table for user recommendations lookup
similar_item_table_test.to_csv('similar_item_table_test.csv', sep=',', encoding='utf-8')
print("similar_item_table_test.csv created successfully!")
