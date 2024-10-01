from log import LogFIleMixin, LogPrintMixin

l1 = LogFIleMixin()
l2 = LogPrintMixin()
l1.log_error('Mensagem de erro')
l1.log_sucesso('Mensagem de sucesso')
l2.log_error('Mensagem de erro')
l2.log_sucesso('Mensagem de sucesso')