import asyncio
import logging
import sys
SERVER_ADDRESS = ("localhost", 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s: %(messages)s",
    stream=sys.stderr,
)

log = logging.getLogger("main")
event_loop = asyncio.get_event_loop()

class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log = logging.getLogger("EchoServer_{}_{}".format(*self.address))
        self.log.debug("Connetion accepted")