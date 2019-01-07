#
# Python SDK for Xooa
#
# Copyright 2018 Xooa
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License
# for the specific language governing permissions and limitations under the License.
#
# Author: Rahul Kamboj
#
# coding: utf-8

from socketIO_client_nexus import SocketIO


class EventListener(object):

    def subscribe_events(self, client_obj, callback):
        try:
            logger = client_obj.xooa_logger
            host = client_obj.socket_host
            api_token = client_obj.api_token

            logger.info('connecting...1')
            socketIO = SocketIO(host, wait_for_connection=True)
            logger.info('connecting 2...')
            socketIO.on('connect', socketIO.emit('authenticate', {'token': api_token}))
            logger.info('connecting 3...')
            socketIO.on('authenticated', self.authenticated)
            logger.info('authenticated')
            socketIO.on('event', callback)
            socketIO.wait()

        except ConnectionError:

            print('The server is down. Try again later.')
            raise

    def handler(self, data):
        return data

    def on_disconnect(self, data):
        return 'Disconnected'

    def authenticated(self):
        return 'Authenticated'

    def unsubscribe(self):
        socketIO = SocketIO('https://api.ci.xooa.io/subscribe', wait_for_connection=True)
        socketIO.on('disconnect', self.on_disconnect)
