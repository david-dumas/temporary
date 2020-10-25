#App route wijzigbare opslag NAW gegevens:
@app.route('/updateNaw/', methods = ['POST'])
def updateNaw():
  if request.method == 'POST':
      updateNaw = NAW(volleNaam = request.form['volleNaam'], adres = request.form['adres'], woonplaats = request.form['woonplaats'], studiejaar = request.form['studiejaar'], beroepsvoorkeur = request.form['beroepsvoorkeur'], introductie = request.form['introductie'])
      session.add(updateNaw)
      session.commit()
      return redirect(url_for('projecten', NAW = NAW))


class NAW(Base):
   volleNaam = Column(String(20), nullable = False)
   adres = Column(String(50), nullable = False)
   woonplaats = Column(String(20), nullable = False)
   studiejaar = Column(Integer, nullable = False)
   beroepsvoorkeur = Column(String(30), nullable = False)
   introductie =  Column(String(500), nullable = False)

# html
<section id="updateNaw">
    <h1>Wijzig NAW-gegevens:</h1>
    <form action="/updateNAW/" method="POST">
    <div class="form-group">
        <label for="volleNaam">Naam:</label>
        <input type="text" maxlength="100" name="volleNaam" placeholder="Volledige naam">

        <label for="adres">Adres:</label>
        <input maxlength="100" name="adres" placeholder="Straatnaam en postcode">

        <label for="woonplaats">Woonplaats:</label>
        <input maxlength="250" name="woonplaats" placeholder="Woonplaats">

        <label for="studiejaar">Studiejaar:</label>
        <input maxlength="250" name="studiejaar" placeholder="Studiejaar">

        <label for="beroepsvoorkeur">Beroepsvoorkeur:</label>
        <input maxlength="250" name="beroepsvoorkeur" placeholder="Beroepsvoorkeur">
        
        <label for="introductie">Introductie:</label>
        <input maxlength="250" name="introductie" placeholder="Beroepsvoorkeur">

        <button type="submit">Wijzig</button>
    </div>
</form>

</section>
