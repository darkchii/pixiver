class PixivError(Exception):
    """ Base pixiv exception. """


class DateError(PixivError):
    """ Date range exception. """


class AjaxRequestError(PixivError):
    """ Some unexpected errors may occur. """


class AutheVerifyError(PixivError):
    """ Cookie or token verification error. """
