# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:48:44 2020

@author: leiya
"""


select P.FirstName, P.LastName, A.City, A.State
from Person as P left outer join Address as A
on P.PersonId = A.PersonId;