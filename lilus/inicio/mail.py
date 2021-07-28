from lilus.mail import Email

class contactoMail(Email):
    # En el context se le tiene que pasar plan y every
    template = 'inicio/plantillasMail/contacto.html'
    template_text = 'inicio/plantillasMail/contacto.ttx'
    title = 'Formulario de contacto enviado'
