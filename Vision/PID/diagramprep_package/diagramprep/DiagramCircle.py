

class DiagramCircle():

    def __init__(self, radius,x,y):
        this.img = None
        this.radius = radius
        this.x = x
        this.y = y
        this.text = ""

    @property
    def image(self,img):
        this.img = img

    @property
    def text(self,text: str) -> str:
        this.text = text
