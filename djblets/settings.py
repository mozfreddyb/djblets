#
# Settings for djblets.
#
# This is meant for internal use only. We use it primarily for building
# static media to bundle with djblets.
#
# This should generally not be used in a project.
import os


SECRET_KEY = '47157c7ae957f904ab809d8c5b77e0209221d4c0'

DEBUG = False
DJBLETS_ROOT = os.path.abspath(os.path.dirname(__file__))
HTDOCS_ROOT = os.path.join(DJBLETS_ROOT, 'htdocs')
STATIC_ROOT = os.path.join(HTDOCS_ROOT, 'static')
STATIC_URL = '/'

STATICFILES_DIRS = (
    os.path.join(DJBLETS_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_JS = {
    'djblets-datagrid': {
        'source_filenames': ('djblets/js/datagrid.js',),
        'output_filename': 'djblets/js/datagrid.min.js',
    },
    'djblets-extensions': {
        'source_filenames': ('djblets/js/extensions.js',),
        'output_filename': 'djblets/js/extensions.min.js',
    },
    'djblets-gravy': {
        'source_filenames': ('djblets/js/jquery.gravy.js',),
        'output_filename': 'djblets/js/jquery.gravy.min.js',
    },
}

PIPELINE_CSS = {
    'djblets-admin': {
        'source_filenames': (
            'djblets/css/admin.less',
            'djblets/css/extensions.less',
        ),
        'output_filename': 'djblets/css/admin.min.css',
    },
    'djblets-datagrid': {
        'source_filenames': (
            'djblets/css/datagrid.less',
        ),
        'output_filename': 'djblets/css/datagrid.min.css',
    },
}

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'djblets.auth',
    'djblets.datagrid',
    'djblets.extensions',
    'djblets.feedview',
    'djblets.gravatars',
    'djblets.log',
    'djblets.pipeline',
    'djblets.siteconfig',
    'djblets.testing',
    'djblets.util',
    'djblets.webapi',
]

PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

# On production (site-installed) builds, we always want to use the pre-compiled
# versions. We want this regardless of the DEBUG setting (since they may
# turn DEBUG on in order to get better error output).
#
# On a build running out of a source tree, for testing purposes, we want to
# use the raw .less and JavaScript files when DEBUG is set. When DEBUG is
# turned off in a non-production build, though, we want to be able to play
# with the built output, so treat it like a production install.

if not DEBUG or os.getenv('FORCE_BUILD_MEDIA', ''):
    PIPELINE_COMPILERS = ['pipeline.compilers.less.LessCompiler']
    PIPELINE = True
elif DEBUG:
    PIPELINE_COMPILERS = []
    PIPELINE = False
