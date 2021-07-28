from django.core.mail import send_mail
from django.template.loader import render_to_string
from multiprocessing import Process

#import logging
#logger = logging.getLogger('jabali.chat')

class Email(Process):
    template = None
    template_text = None
    title = None
    def __init__(self, context, to=None):
        super().__init__()
        self.to = to if to else (context['to'] if 'to' in context else False)
        self.context = context

    def render(self, context=None):
        context = context if context else self.context
        return render_to_string(self.template, context=context)

    def text(self, context=None):
        context = context if context else self.context
        return render_to_string(self.template_text, context=context)

    def send(self, to=None, context=None, title=None, sender='noreply@lilus.es'):
        if self.to or to:
            to = to if to else self.to
            send_mail(
                title if title else self.title,
                self.text(context),
                sender,
                [to] if isinstance(to, str) else to,
                html_message=self.render(context),
                fail_silently=True,
            )
            #logger.info(f"Mail sent[to={[to] if isinstance(to, str) else to};title={title if title else self.title}]")
            return True
        else:
            return False

    def run(self, to=None, context=None, title=None, sender='noreply@lilus.es'):
        self.send(to, context, title, sender)
