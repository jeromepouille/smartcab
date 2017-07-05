# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 12:28:45 2017

@author: TO95871
"""

tries={None:0, 'Left':0, 'Right':10,'Forward':8}
maxi=max(tries.values())
action_to_choose_from=[]
for cle in tries.keys():
    if tries[cle]==maxi:
        action_to_choose_from.append(cle)
        
action=random.choice(action_to_choose_from)        
