import requests

apiBaseUrl = "https://jsonplaceholder.typicode.com"
authorisationToken = "token123"

apis_dic = {'posts': '/posts',
        'posts1': '/posts1'}

response_dic = {}
all_response_dic = {}

for apiKey in apis_dic:
    print(apiKey, '->', apis_dic[apiKey])

    responseFromApiGet = requests.get(apiBaseUrl + apis_dic[apiKey],
                                      headers={
       "authorisation": authorisationToken
     }
                                      )

    for id in responseFromApiGet.json():
        print(id['id'])
        detailedResponseGet = requests.get(apiBaseUrl + apis_dic[apiKey] + "/" + str(id['id']))

        print(detailedResponseGet.json())
        response_dic[id['id']] = detailedResponseGet.json()
    all_response_dic[apiKey] = response_dic
    response_dic = {}

#for key1 in response_dic:
#    print(key1, '->', response_dic[key1])

for responseKey in all_response_dic:
    print(responseKey, '-->', all_response_dic[responseKey])
    for jsonKey in all_response_dic[responseKey]:
        jsonToSend = all_response_dic[responseKey][jsonKey]
        del jsonToSend['id']  #delete id element, not needed in POST request
        print("json_to_send: " + str(jsonToSend))
        print("endpoint: " + apiBaseUrl + apis_dic[responseKey])
        responsePost = requests.post(apiBaseUrl + apis_dic[responseKey],
                                     json=jsonToSend,
                                     headers={
                                 "authorisation": authorisationToken
                             }
                                     )
        print("status code: " + str(responsePost.status_code))
        print("response: " + responsePost.text)
        #print(json_key, '--->', json_to_send)


