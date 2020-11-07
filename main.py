import requests

apis = {'posts': '/posts',
        'posts1': '/posts1'}
response_dic = {}
all_response_dic = {}

for key in apis:
    print(key, '->', apis[key])

    response = requests.get("https://jsonplaceholder.typicode.com" + apis[key],
     headers={
       "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
       "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
     }
    )

    for id in response.json():
        print(id['id'])
        response2 = requests.get("https://jsonplaceholder.typicode.com" + apis[key] + "/" + str(id['id']))

        print(response2.json())
        response_dic[id['id']] = response2.json()
    all_response_dic[key] = response_dic
    response_dic = {}

#for key1 in response_dic:
#    print(key1, '->', response_dic[key1])

for response_key in all_response_dic:
    print(response_key, '-->', all_response_dic[response_key])
    for json_key in all_response_dic[response_key]:
        json_to_send = all_response_dic[response_key][json_key]
        del json_to_send['id']  #delete id element, not needed in POST request
        print("json_to_send: " + str(json_to_send))
        print("endpoint: " + "https://jsonplaceholder.typicode.com" + apis[response_key])
        resp = requests.post("https://jsonplaceholder.typicode.com" + apis[response_key],
                             json=json_to_send)
        print("status code: " + str(resp.status_code))
        print("response: " + resp.text)
        #print(json_key, '--->', json_to_send)


