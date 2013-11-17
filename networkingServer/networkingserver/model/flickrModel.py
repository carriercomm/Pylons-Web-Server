import httplib, urllib
import json

class flickrModel():
  def getPictures(self, keyword, numResults):
    flickrConnection = httplib.HTTPConnection("api.flickr.com")
    #flickrConnection.set_debuglevel(1)

    params = urllib.urlencode({
        'method': 'flickr.photos.search',
        'api_key': 'a71d836638f387d9815a0be9afe69813',
        'tags': keyword,
        'per_page': numResults,
        'format': 'json',
        'nojsoncallback': 1
    })
    url = "/services/rest/?%s" % params
    #return params
    flickrConnection.request("GET", url)
    response = flickrConnection.getresponse()

    return self.translateResponse(response.read())

  def translateResponse(self, response):
    jsonObject = json.loads(response)
    photos = []
    if ("photos" in jsonObject):
      for photo in jsonObject["photos"]["photo"]:
          # http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
          photoUrl = "http://farm%s.static.flickr.com/%s/%s_%s_m.jpg" % (photo["farm"], photo["server"], photo["id"], photo["secret"])
          newPhoto = {"url": photoUrl}
          photos.append(newPhoto)
      return json.dumps(photos)
    else:
      return json.dumps({'message': jsonObject['message']})