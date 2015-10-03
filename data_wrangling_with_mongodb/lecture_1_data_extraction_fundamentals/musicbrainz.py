# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:58:55 2015

@author: tvu
"""

# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    artist_id = results["artists"][1]["id"]
    print "\nARTIST:"
    pretty_print(results["artists"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print "\nALL TITLES:"
    for t in release_titles:
        print t


if __name__ == '__main__':
    main()
    
q1 = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
q1_count = 0
for artist in q1["artists"]:
    if artist["score"] == "100":
        q1_count += 1
print "Q1: Number of bands 'FIRST AID KIT' that had score == 100"
print q1_count

q2 = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
begin_area = q2["artists"][0]["begin-area"]["name"]
print "Q2: Begin area for Queen"
print begin_area

q3 = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
aliases = q3["artists"][0]["aliases"]
for a in aliases:
    if a["locale"] == "es":
        alias = a["name"]
print "Q3: Spanish alias for Beatles"
print alias
#pretty_print(q3)

q4 = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
disam = q4["artists"][0]["disambiguation"]
print "Q4: Disambiguation Nirvana"
print disam

q5 = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
begin_date = q5["artists"][0]["life-span"]["begin"]
print "Q5: One Direction begin"
print begin_date
