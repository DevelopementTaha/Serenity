class CollectionObject:

    def __init__(self, id, name, image, description, order, showSession, sessionsOrder,showCollection, showPositip, showArticle):
        strip_character = "/"
        self.id = id
        self.name = name
        if image == None:
            self.image = 'Image Not Provided by Admin!'
        else:
            self.image = 'https://static.wixstatic.com/media/' + strip_character.join(image.split(strip_character)[3 :4])
        self.description = description
        if order == None:
            self.order = 10000000 
        else:
            self.order = order
        ###
        if showSession == None:
            self.showSession = False
        else:
            self.showSession = showSession
        ###
                ###
        if showCollection == None:
            self.showCollection = False
        else:
            self.showCollection = showCollection
        ###

        if showPositip == None:
            self.showPositip = False
        else:
            self.showPositip = showPositip
        ###

        if showArticle == None:
            self.showArticle = False
        else:
            self.showArticle = showArticle
        ###
        if sessionsOrder == None:
            self.sessionsOrder = 10000000 
        else:
            self.sessionsOrder = sessionsOrder
        self.sessionList = []
        self.positipList = []
        self.articleList = []

    def addSessionObject(self, obj):
        self.sessionList.append(obj)

    def addPositipsObject(self, obj):
        self.positipList.append(obj)

    def addArticlesObject(self, obj):
        self.articleList.append(obj)

    def checkValue(self):
        if self.showCollection == True:
            return self