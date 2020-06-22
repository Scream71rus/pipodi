
import cerberus


class ValidatorErrorHandler(cerberus.errors.BasicErrorHandler):

    @property
    def error_messages(self):
        if hasattr(self, "_error_messages"):
            return self._error_messages

        else:
            return "Some error"

    def format_message(self, field, error):
        if self.error_messages:
            return self.error_messages.get(
                field, self._default_message)

        else:
            return error


class ExtendValidator(cerberus.Validator):

    def _validate_type_numeral(self, value):
        if isinstance(value, str) and value.replace(".", "0").isdigit():
            return True

        # if isinstance(value, str) and value == "":
        #     return True

        if not isinstance(value, str) and isinstance(value, (int, float, complex)):
            return True
