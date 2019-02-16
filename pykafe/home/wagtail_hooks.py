from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def make_h1_default(features):
    features.default_features.append('h1')
