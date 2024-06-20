class SuccessUrlToItselfMixin:
    def get_success_url(self):
        return self.request.path
