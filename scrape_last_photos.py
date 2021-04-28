import requests
from bs4 import BeautifulSoup


# Create Variables
class PhotoUrls:

    def __init__(self, handle):
        self.handle = handle

    def get_last_url(self):
        base_url = "https://www.picuki.com/profile/" + self.handle
        print(f"User URL = {base_url}")
        r = requests.get(base_url,
                         headers={
                             'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        last_loc = soup.find_all("div", {"class": "photo"})
        #print(last_loc[0])
        last_location_url = last_loc[0].find('a').get('href')
        #print(last_location_url)
        return last_location_url
        #print(last_location)

    def photo_links(self):
        base_url = self.get_last_url()
        print(f"POST URL = {base_url}")
        r = requests.get(base_url,
                         headers={
                             'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        last_loc = soup.find_all("div", {"class": "item"})
        #print(last_loc)
        #print(len(last_loc))
        photos = []
        # Add unique locations to list

        for i in range(0, len(last_loc), 1):
            x = last_loc[i].find('img').get('src')
            prefix = "https://www.picuki.com"
            xx = prefix + x
            if xx not in photos:
                if xx != '':
                    photos.append(xx)
                else:
                    pass
            else:
                pass

        #last_location_url = last_loc[0].find('img').get('src')
        print(f"First Photo: {photos[0]}")
        print(f"Last Photo: {photos[-1]}")
        #for links in photos:
            #print(f"Photo URL: {photos[i]}")

        # return last_location_url
        #print(last_location)
        print("-----------------")

        return photos



if __name__ == "__main__":
    #handle = str(input("Please enter handle of user: ") or '4x4theboiz')
    handle = '4x4theboiz'
    print(handle)
    #point1 = PhotoUrls(handle=handle)
    #url = point1.get_last_url()
    print("*************")
    photos = PhotoUrls(handle=handle).photo_links()
