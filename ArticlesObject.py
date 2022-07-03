class ArticlesObject:

  def __init__(self, id,title,homePageImage, articleImage, description):
    strip_character =  "/"
    self.id = id
    self.title = title
    if homePageImage == None:
      self.homePageImage = 'Image Not Provided by Admin!'
    else:
      self.homePageImage = 'https://static.wixstatic.com/media/' + strip_character.join(homePageImage.split(strip_character)[3 :4])
    if articleImage == None:
      self.articleImage = 'Image Not Provided by Admin!'
    else:
      self.articleImage = 'https://static.wixstatic.com/media/' + strip_character.join(articleImage.split(strip_character)[3 :4])
    self.description = description


