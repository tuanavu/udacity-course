# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 20:11:31 2014

@author: tvu
"""

#!/usr/bin/python

###
### in poiFlagEmail() below, write code that returns a boolean
### indicating if a given emails is from a POI
###

import sys
import reader
import poi_emails

def getToFromStrings(f):
    f.seek(0)
    to_string, from_string, cc_string   = reader.getAddresses(f)
    to_emails   = reader.parseAddresses( to_string )
    from_emails = reader.parseAddresses( from_string )
    cc_emails   = reader.parseAddresses( cc_string )

    return to_emails, from_emails, cc_emails


### POI flag an email

def poiFlagEmail(f):
    """ given an email file f,
        return a trio of booleans for whether that email is
        to, from, or cc'ing a poi """

    to_emails, from_emails, cc_emails = getToFromStrings(f)

    ### list of email addresses of all the POIs
    poi_email_list = poi_emails.poiEmails()

    to_poi = False
    from_poi = False
    cc_poi   = False

    ### to_poi and cc_poi are related functions, which flag whether
    ### the email under inspection is addressed to a POI, or if a POI is in cc
    ### you don't have to change this code at all

    ### there can be many "to" emails, but only one "from", so the
    ### "to" processing needs to be a little more complicated
    if to_emails:
        ctr = 0
        while not to_poi and ctr < len(to_emails):
            if to_emails[ctr] in poi_email_list:
                to_poi = True
            ctr += 1
    if cc_emails:
        ctr = 0
        while not to_poi and ctr < len(cc_emails):
            if cc_emails[ctr] in poi_email_list:
                cc_poi = True
            ctr += 1


    #################################
    ######## your code below ########
    ### set from_poi to True if #####
    ### the email is from a POI #####
    #################################
#    if from_emails:
#        ctr = 0
#        while not from_poi and ctr < len(from_emails):
#            if from_emails[ctr] in poi_email_list:
#                from_poi = True
#            ctr += 1
    if from_emails and from_emails[0] in poi_email_list:
        from_poi = True
    
    
    

    #################################
    return to_poi, from_poi, cc_poi