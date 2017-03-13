#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from setuptools import setup

setup(
    name='WebhookNotificationPlugin',
    version='0.2.1',
    description='Plugin to post Trac changes to a webhook',
    author='Li-Miao',
    author_email='lm3783@gmail.com',
    url='https://github.com/lm3783/trac-webhook-plugin',
    license='BSD',
    packages=['webhook_notification'],
    install_requires=[
        "requests",
    ],
    classifiers=[
        'Framework :: Trac',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'trac.plugins': 'webhook_notification = webhook_notification'
    }
)
