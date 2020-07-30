from app import db
from app.models import Offers

db.create_all()

sample = Offers(job='Vicepresidente Ejecutivo', 
                company='Compu-Global-Hyper-Mega-Net', 
                description='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan, 
                metus ultrices eleifend gravida, nulla nunc varius lectus, 
                nec rutrum justo nibh eu lectus. Ut vulputate semper dui. Fusce erat odio,
                sollicitudin vel erat vel, interdum mattis neque.''',
                salary='40000',
                localization='Springfield',
                requirements='Python, Flask, CSS3',
                extra='Kiwis, café',
                contact='jsalvador.me',
                approbed = None
            )

db.session.add(sample)
db.session.commit()