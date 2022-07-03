class PositipsObject:

        def __init__(self, id,title, homePageImage, category, textImage, description, text, hiddenText):
          strip_character = "/"
          self.id = id
          self.title = title
          if homePageImage == None:
            self.homePageImage = 'Image Not Provided by Admin!'
          else:
            self.homePageImage = 'https://static.wixstatic.com/media/' + strip_character.join(homePageImage.split(strip_character)[3 :4])
          self.category = category
          if textImage == None:
            self.textImage = 'Image Not Provided by Admin!'
          else:
            self.textImage = 'https://static.wixstatic.com/media/' + strip_character.join(textImage.split(strip_character)[3 :4])
          self.description = description
          self.text = text
          self.hiddenText = hiddenText