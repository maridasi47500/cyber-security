from render import Render
class Erreur():
  def __init__(self):
    self.route={"/":"Hello#hi"}
    self.figure=Render("erreur 404 non trouvé")
  def err404(self):
    return self.figure
