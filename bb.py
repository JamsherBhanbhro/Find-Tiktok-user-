from TikTokApi import TikTokApi
api = TikTokApi()
with open("wl.txt") as fp:
    for line in fp:
        val = format(line.strip())
        search = api.getUser(val)
        id = search['statusCode']
        if(id==0):
            print(val+" has not been found.")
        else:
            print(val + " hasbeen found.")
