from django.forms import ImageField


class keywordObject:
  def __init__(self, title, equivalent, image):
    strip_character = "/"
    self.title = title
    self.equivalent = equivalent
    self.image = 'https://static.wixstatic.com/media/' + strip_character.join(image.split(strip_character)[3 :4])