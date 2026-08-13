from db import db  

class Game(db.Model):  
    __tablename__ = 'alunos'  

    nome = db.Column(db.String(80), nullable=False)
    genero = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.String(80), nullable=False)

    def json(self):  
        return {
            'nome': self.nome,
            'genero': self.genero,
            'endereco': self.endereco,
            'idade': self.idade
        }
    