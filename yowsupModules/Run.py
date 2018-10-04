from yowsupModules.Layer import EchoLayer
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.stacks import YowStackBuilder
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.env import YowsupEnv
import base64
from yowsup.layers.auth import AuthError


# def decode_base64(data):
#     missing_padding = len(data) % 4
#     if missing_padding != 0:
#         data += '=' * (4 - missing_padding)
#     print('pure data: ', data)
#     print('data encode: ', base64.b64decode(data))
#     return base64.encodestring(data)


# d/DUKMTn5h++1ifz/IE4cYIrPQg=

credentials = ('number_phone', 'otp_code')


class YowsupEchoStack(object):
    def __init__(self, credentials, encryptionEnabled=True):
        stackBuilder = YowStackBuilder()

        self.stack = stackBuilder \
            .pushDefaultLayers(encryptionEnabled) \
            .push(EchoLayer) \
            .build()

        self.stack.setCredentials(credentials)

    def start(self):
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop()
        except AuthError as e:
            print('Authentication Error: %s' %e.message)
            print('Authentication: ', e)

    # print('decode: ', base64.decodestring('d/DUKMTn5h++1ifz/IE4cYIrPQg='))  # 817013
    # stackBuilder = YowStackBuilder()
    #
    # stack = stackBuilder.pushDefaultLayers(True).push(EchoLayer).build()
    #
    # stack.setCredentials(credentials)
    #
    # stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, credentials)  # setting credentials
    # stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])  # whatsapp server address
    # stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    # stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())  # info about us as WhatsApp client
    #
    # stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))  # sending the connect signal
    # stack.loop()  # this is the program mainloop
