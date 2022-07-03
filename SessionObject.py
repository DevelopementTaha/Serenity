class SessionObject:

  def __init__(self, id, title,keyword, ambiance, duree , image, video, categorie, imageCategorie, description, audio):
    strip_character = "/"
    self.id = id
    self.title = title
    self.keyword = keyword
    self.ambiance = ambiance
    self.duree = duree
    if image != None:
      self.image = 'https://static.wixstatic.com/media/' + strip_character.join(image.split(strip_character)[3 :4])
    self.video = video
    self.categorie = categorie
    if imageCategorie != None:
      self.imageCategorie = 'https://static.wixstatic.com/media/' + strip_character.join(imageCategorie.split(strip_character)[3 :4])
    self.description = description
    if audio != None:
      self.audio = 'https://static.wixstatic.com/mp3/' + strip_character.join(audio.split(strip_character)[3 :4])
    self.keywordList = []
    
  def addkeywordObject(self, obj):
    self.keywordList.append(obj)

