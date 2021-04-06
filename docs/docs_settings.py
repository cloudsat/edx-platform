"""
Django settings for use when generating API documentation.
Basically the LMS devstack settings plus a few items needed to successfully
import all the Studio code.
"""


import os
# Turn on all the boolean feature flags, so that conditionally included
# API endpoints will be found.
for key, value in FEATURES.items():
    if value is False:
        FEATURES[key] = True

# Settings that will fail if we enable them, and we don't need them for docs anyway.
FEATURES['RUN_AS_ANALYTICS_SERVER_ENABLED'] = False

INSTALLED_APPS.extend([
    'cms.djangoapps.contentstore.apps.ContentstoreConfig',
    'cms.djangoapps.course_creators',
    'cms.djangoapps.xblock_config.apps.XBlockConfig',
    'lms.djangoapps.lti_provider'
])


COMMON_TEST_DATA_ROOT = ''
