from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    
    #For multiple runs
    Game.query.delete()

    #Add sample game data
    monopoly = Game(name='Monopoly', description='test game 1')
    cards_against_humanity = Game(name='Cards Against Humanity', description='test game 2')
    drinking_game = Game(name='Drinking Game', description='test game 3')

    db.session.add_all([monopoly, cards_against_humanity, drinking_game])
    db.session.commit()

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
