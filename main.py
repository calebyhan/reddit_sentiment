# from decouple import config
# from googleapiclient.discovery import build
#
# TOKEN = config("TOKEN")
# CX = config("CX")
#
#
# def google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res['items']
#
#
# results = google_search('"collegeboard', TOKEN, CX, num=100)
# for result in results:
#     print(result)

from search_engine_parser import GoogleSearch

def google(query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    print(*search_args)
    gresults = gsearch.search(*search_args)
    return gresults['titles']

print(google('collegeboard bad'))