import pandas as pd
import numpy as np
import math

similar_items = pd.read_csv('similar_item_table_test.csv')

print("----Available option to choose from---")
print(list(similar_items['offer_key']))
print('-----------------------------------------------------------------------')
print("Enter the offer id for which you want to see the recomendations")
offer_id = int(input())
lookup_offer = similar_items[similar_items['offer_key']==offer_id][['offer_key','1st','2nd','3rd','4th','5th']]
print(lookup_offer)
